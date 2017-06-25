from setuptools import setup

setup(name='WPA2-HalfHandshake-Crack',
      version='0.1',
      description='This is a POC to show it is possible to capture enough of a handshake with a user from a fake AP to crack a WPA2 network without an AP',
      url='https://github.com/alin-dinescu/WPA2-HalfHandshake-Crack',
      author='Alin Dinescu',
      author_email='alindinescu65@yahoo.com',
      license='MIT',
      install_requires=['pypcapfile-master', 'pbkdf2-ctypes-0.99.1', 'pyrcrack-0.1.1'])
