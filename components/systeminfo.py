import platform
import getpass
import pyscreenshot
import psutil
import wmi

def get_information():
    cpu = wmi.WMI().Win32_Processor()[0].Name
    gpu = wmi.WMI().Win32_VideoController()[0].Name
    system_name = platform.system()
    system_version = platform.release()
    username = getpass.getuser()
    hostname = platform.node()
    disk_info = psutil.disk_usage("/")
    disk_size = disk_info.total / (1024 ** 3)
    disk_name = psutil.disk_partitions

    return [system_name, system_version, username, cpu, gpu, hostname]


def take_screenshot():
    # Machen Sie einen Screenshot des Desktops und speichern Sie ihn in einem PIL-Bild
    screenshot = pyscreenshot.grab()

    # Speichern Sie das Bild in der Datei "screenshot.png"
    screenshot.save("screenshot.png")


