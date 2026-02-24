import os
import subprocess
import pickle

# 1. Hardcoded password (Security Hotspot)
DB_PASSWORD = "admin123"

# 2. Command Injection (Vulnerability)
def run_command(cmd):
    subprocess.call(cmd, shell=True)

# 3. Use of eval (Critical Vulnerability)
def calculate(expression):
    return eval(expression)

# 4. Insecure deserialization (Critical)
def load_data(data):
    return pickle.loads(data)

# 5. Weak cryptography (Security Hotspot)
import hashlib
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

# 6. Unused variable (Code Smell)
unused_variable = 42