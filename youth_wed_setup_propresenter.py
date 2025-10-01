import subprocess as sub
import requests as req
import jsonpath-ng as jpng

def start_propresenter():
    sub.Popen('Propresenter.exe')

def trigger_propresenter_song_macro():
    get_macros_url = 'http://localhost:50001/v1/macros'
    trigger_macro_url = 'http://localhost:50001/v1/macros/{macro_id}'
    response = req.get(get_macros_url)
    macro_id = get_songs_macro_uuid(response)
    req.post(trigger_macro_url.format(macro_id=macro_id))

def get_songs_macro_uuid(response):
    jsonpath_exp = parse('$[?id.name = "Songs"].id.uuid')
    matches = jsonpath_exp.find(response.json())
    values = [match.value for match in matches][0]
