import connexion
import six

from swagger_server.models.cpu import CPU  # noqa: E501
from swagger_server import util
# import get_processor_name

# get_processor_name()
import os, platform, subprocess, re

def get_processor_name():
    if platform.system() == "Windows":
        return platform.processor()
    elif platform.system() == "Darwin":
        command = "/usr/sbin/sysctl -n machdep.cpu.brand_string"
        return subprocess.check_output(command, shell=True).strip()
    elif platform.system() == "Linux":
        command = "cat /proc/cpuinfo"
        all_info = subprocess.check_output(command, shell=True).strip()
        for line in all_info.split("\n"):
            if "model name" in line:
                return re.sub(".*model name.*:", "", line, 1)
    return "cannot find cpuinfo"


def cpu_get():  # noqa: E501
    """cpu_get

    Returns cpu information of the hosting server # noqa: E501


    :rtype: CPU
    """
    return CPU(get_processor_name())

#cpu_get()
