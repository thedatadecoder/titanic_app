import subprocess
import sys

with open('requirements.txt') as f:
    packages = f.read().splitlines()

packages_skipped = []

for package in packages:
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
    except: #subprocess.CalledProcessError as e:
        #print(f"Failed to install {package}: {e}")
        packages_skipped.append(package)

print(packages_skipped, "not installed. They are skipped")
