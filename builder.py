import subprocess
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


logo = """
 ____                              
/\  _`\                            
\ \ \L\ \     __       __    ___   
 \ \ ,  /   /'__`\   /'__`\ / __`\ 
  \ \ \\ \ /\ \L\.\_/\  __//\ \L\ \ 
   \ \_\ \_\ \__/.\_\ \____\ \____/
    \/_/\/ /\/__/\/_/\/____/\/___/ 
                                   
"""

print(bcolors.HEADER + logo + bcolors.ENDC)
print(bcolors.OKCYAN + "Made by Areo" + bcolors.ENDC)
print("")
print("")
print("")
input("Press enter to start:")

print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

subprocess.run('pip install -r requirements.txt')
subprocess.run('pip install -U pyinstaller')
subprocess.run('pyinstaller --onefile --noconsole --add-data components;components/  main.py')

print("Finished build")

