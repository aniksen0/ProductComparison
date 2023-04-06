import os

command1 = "wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"
command2 = "sudo dpkg -i google-chrome-stable_current_amd64.deb"
command3 = "sudo apt-get install wget"
os.system(command3)
os.system(command1)
os.system(command2)
