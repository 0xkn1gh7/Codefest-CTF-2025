#!/usr/bin/env python3

import tempfile
import subprocess

def banner():
    print('''
    ███████╗███████╗████████╗ ██████╗██╗  ██╗
    ██╔════╝██╔════╝╚══██╔══╝██╔════╝██║  ██║
    █████╗  █████╗     ██║   ██║     ███████║
    ██╔══╝  ██╔══╝     ██║   ██║     ██╔══██║
    ██║     ███████╗   ██║   ╚██████╗██║  ██║
    ╚═╝     ╚══════╝   ╚═╝    ╚═════╝╚═╝  ╚═╝

    A config checker for neofetch

    ''')

banner()
temp = tempfile.NamedTemporaryFile()

print('Paste your neofetch config. Don\'t use empty lines.')
with open(temp.name, 'w') as f:
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line == '':
            break
        f.write(line)
    f.close()

print('neofetch output:\n')
result = subprocess.run(["neofetch", "--config", temp.name], capture_output=True, text=True)
print(result.stdout)