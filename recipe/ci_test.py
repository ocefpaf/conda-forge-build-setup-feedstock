#!/usr/bin/env python


import os
import subprocess
import sys


def main(argv):
    subprocess.check_call([
        "conda",
        "install",
        "--use-local",
        "--offline ",
        "-n", "root",
        "--yes",
        "conda-forge-build-setup"
    ])

    import conda.config

    rc = conda.config.rc

    assert rc.get("show_channel_urls") == True
    assert rc.get("add_pip_as_python_dependency") == False

    if sys.platform == "win32":
        cmd = ["run_conda_forge_build_setup", "&&", "set"]
    else:
        cmd = ["source", "run_conda_forge_build_setup", "&&", "env"]

    env_vars = subprocess.check_output(cmd)
    if sys.version_info[0] >= 3:
        env_vars = env_vars.decode("UTF-8")

    _env_vars = env_vars
    env_vars = {}
    for each_env_vars in _env_vars:
        each_env_var_name, each_env_var_val = each_env_vars.split("=")
        each_env_var_name = each_env_var_name.strip()
        each_env_var_val = each_env_var_val.strip()
        env_vars[each_env_var_name] = each_env_var_val

    if sys.platform == "darwin":
        assert env_vars.get("MAKEFLAGS") == "-j1"
    elif sys.platform == "linux":
        assert env_vars.get("MAKEFLAGS") == "-j2"
    elif sys.platform == "win32":
        assert "MAKEFLAGS" not in env_vars

    assert env_vars.get("PYTHONUNBUFFERED") == "1"


if __name__ == "__main__":
    sys.exit(main(sys.argv))
