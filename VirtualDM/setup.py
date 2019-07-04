from setuptools import setup

APP = ['VDM.py']
DATA_FILES = ['VDMLogo.icns','graphics.py']
OPTIONS = {
    'iconfile':'VDMLogo.icns',
    'argv_emulation': True,
    #'packages': ['certifi'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app':OPTIONS},
    setup_requires=['py2app'],
)
