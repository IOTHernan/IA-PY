import subprocess
import platform

def ejecutar_powershell(script_name):
    script_path = 'path/to/scripts/powershell_scripts.ps1'
    result = subprocess.run(['powershell.exe', '-File', script_path, '-scriptName', script_name], capture_output=True, text=True)
    print(result.stdout)

def ejecutar_bash(script_name):
    script_path = 'path/to/scripts/bash_scripts.sh'
    result = subprocess.run(['bash', script_path, script_name], capture_output=True, text=True)
    print(result.stdout)

def ejecutar_script(script_name):
    os_system = platform.system()
    if os_system == "Windows":
        ejecutar_powershell(script_name)
    elif os_system == "Linux":
        ejecutar_bash(script_name)
    else:
        raise Exception("Sistema operativo no soportado")
