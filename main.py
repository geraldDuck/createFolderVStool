import subprocess
import time as t

# This is the path where your file will be saved
# Feel free to change it!
dir:str = str("%USERPROFILE%\\OneDrive\\Desktop")
# (P.S. %USERPROFILE% is the User)

folder_name:str = str(input("Folder name: "))
file_name:str = str(input("File name(e.g. main.py, main.lua): "))

subprocess.run(f"cd %USERPROFILE%\\OneDrive\\Desktop && mkdir {folder_name} && cd {folder_name} && type nul > {file_name} && code .", shell=True)import subprocess
t.sleep(1)
exit()
