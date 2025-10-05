import subprocess as sub
import requests as req
import youth_wed_setup_vars
from jsonpath_ng.ext import parse

class PropresenterEditor():

    def __init__(self):
        self.env_vars = youth_wed_setup_vars.env_vars

    def start_propresenter(self) -> None:
        sub.Popen(self.env_vars['propresenter_exe'])

    def trigger_propresenter_song_macro(self) -> None:
        propresenter_endpoint = self.env_vars['propresenter_endpoint']

        get_macros_url = f'{propresenter_endpoint}/v1/macros'
        response = req.get(get_macros_url)

        macro_id = self.get_songs_macro_uuid(response)
        trigger_macro_url = f'{propresenter_endpoint}/v1/macros/{macro_id}'
        req.post(trigger_macro_url)

    def get_songs_macro_uuid(self, response) -> dict:
        jsonpath_exp = parse('$[?id.name = "Songs"].id.uuid')
        matches = jsonpath_exp.find(response.json())
        macro_id = [match.value for match in matches][0]
        return macro_id
