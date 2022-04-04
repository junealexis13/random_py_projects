import sys
import subprocess

dependencies = ['tk','pytube']
for packagename in dependencies:
    # implement pip as a subprocess:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install',
    packagename])

    # process output with an API in the subprocess module:
    reqs = subprocess.check_output([sys.executable, '-m', 'pip',
    'freeze'])
    installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

    if packagename in installed_packages:
        print(f"'{packagename}' is now installed.")
    else:
        print('Package is missing.')