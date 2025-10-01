import subprocess as sub

def enable_youth_monitors():
    sub.run('MultiMonitorTool.exe', '/enable', '2')
