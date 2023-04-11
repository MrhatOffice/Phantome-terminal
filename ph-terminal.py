import subprocess
import platform
import socket
import time
import os
import requests

path = 'C:/'
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print("""
▒█▀▀█ ▒█░▒█ ░░ ▀▀█▀▀ ▒█▀▀▀ ▒█▀▀█ ▒█▀▄▀█ ▀█▀ ▒█▄░▒█ ░█▀▀█ ▒█░░░ 
▒█▄▄█ ▒█▀▀█ ▀▀ ░▒█░░ ▒█▀▀▀ ▒█▄▄▀ ▒█▒█▒█ ▒█░ ▒█▒█▒█ ▒█▄▄█ ▒█░░░ 
▒█░░░ ▒█░▒█ ░░ ░▒█░░ ▒█▄▄▄ ▒█░▒█ ▒█░░▒█ ▄█▄ ▒█░░▀█ ▒█░▒█ ▒█▄▄█""")
print("PH terminal |Version 1.1|")
while True:
    code = input(">>> ")
    if code == 'ping':
        host = input("Enter Website To Ping: ")
        number = input("Enter How Many Times To Ping: ")

        def ping(host):
            param = '-n' if platform.system().lower() == 'windows' else '-c'
            command = ['ping', param, number, host]
            return subprocess.call(command)

        print(ping(host))
    elif code == 'local':
        print("Your Local IPS Is: " + host_ip)
        print("Your Desktop Name Is: " + host_name)
    elif code == 'date':
        print("The Local Date Is: " + time.strftime("%m/%d/%Y"))
    elif code == 'list':
        dir_list = os.listdir(path)
        print("Files and Directories in '", path, "' :")
        print(dir_list)
    elif code == 'list -a':
        file = input("Enter The Direct File Path To Read: ")
        dir_list2 = os.listdir(file)
        print("Files and directories in '", file, "':")
        print(dir_list2)
    elif code.startswith('echo '):
        echo_string = code[5:]
        print(echo_string)
    elif code == 'tasklist':
        result = subprocess.run('tasklist', stdout=subprocess.PIPE)
        print(result.stdout.decode('utf-8'))
    elif code == 'netstat':
        result = subprocess.run('netstat', stdout=subprocess.PIPE)
        print(result.stdout.decode('utf-8'))
    elif code == 'whoami':
        result = subprocess.run('whoami', stdout=subprocess.PIPE)
        print(result.stdout.decode('utf-8'))
    elif code == 'help':
        print("Available commands:")
        print("ping - Ping a website")
        print("local - Display local IP and desktop name")
        print("date - Display local date")
        print("list - Display files and directories in the current path")
        print("list -a - Display files and directories in a specified path")
        print("echo - Print a string to the console")
        print("tasklist - Display a list of running processes")
        print("netstat - Display current network connections")
        print("whoami - Display the current username")
        print("netstat - Display network connections")
        print("tasklist - Display running processes")
    else:
        print("Invalid command. Type 'help' for a list of available commands.")
