import os
import subprocess

def insecure_exec(user_input):
    # ❌ Command Injection (CWE-78)
    os.system("ls " + user_input)

def hardcoded_password():
    # ❌ Hardcoded credential (CWE-259)
    password = "admin123"
    return password

def insecure_subprocess(cmd):
    # ❌ Shell injection
    subprocess.call(cmd, shell=True)

user = input("Enter directory:")
insecure_exec(user)