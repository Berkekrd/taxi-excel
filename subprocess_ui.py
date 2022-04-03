import subprocess
subprocess.run('python -m PyQt5.uic.pyuic -x main.ui -o login.py')
subprocess.run('python -m PyQt5.uic.pyuic -x personal.ui -o personal.py')
subprocess.run('python -m PyQt5.uic.pyuic -x general.ui -o general.py')
subprocess.run('python -m PyQt5.uic.pyuic -x personalDataUpdate.ui -o personalDataUpdate.py')