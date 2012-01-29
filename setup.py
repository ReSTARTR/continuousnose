from distutils.core import setup
from setuptools import find_packages
import os
os.path.join('src')
SRC_DIR = 'src'
setup(
    name = "continuousnose",
    version = "1.0",
    packages = [''],
    install_requires = ['nose','rednose','watchdog'],
    package_dir = {'':SRC_DIR},
    #packages         = find_packages(SRC_DIR),
    entry_points = {
        'console_scripts': [
            'continuous_nose = continuousnose.ContinuousNose:run',
        ]
    },

)


