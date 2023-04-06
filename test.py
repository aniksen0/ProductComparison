import os

command1 = "wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"
command2 = "sudo dpkg -i google-chrome-stable_current_amd64.deb"

os.system(command1)
os.system(command2)
