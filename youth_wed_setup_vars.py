import os

def _get_env_vars() -> dict:
    platform_vars = {}
    env_vars = os.environ

    platform_vars['propresenter_endpoint'] = env_vars['PROPRESENTER_ENDPOINT']
    platform_vars['propresenter_exe'] = env_vars['PROPRESENTER_EXE_PATH']
    platform_vars['multi_monitor_script'] = env_vars['MULTI_MONITOR_SCRIPT_PATH']

    return platform_vars

env_vars = _get_env_vars()
