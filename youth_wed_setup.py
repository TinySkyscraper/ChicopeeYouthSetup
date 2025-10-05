from youth_wed_setup_monitors import MonitorEditor
from youth_wed_setup_propresenter import PropresenterEditor

if __name__ == "__main__":
    mon_editor = MonitorEditor()
    mon_editor.enable_youth_monitors()

    pro_editor = PropresenterEditor()
    pro_editor.start_propresenter()
    pro_editor.trigger_propresenter_song_macro()
