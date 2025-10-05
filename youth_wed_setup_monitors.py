import subprocess as sub
import youth_wed_setup_vars

class MonitorEditor():

    def __init__(self):
        self.env_vars = youth_wed_setup_vars.env_vars

    def enable_youth_monitors(self):
        sub.run(self.env_vars["multi_monitor_script"])
