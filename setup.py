from setuptools import setup, find_packages

setup(
    name='Contacts',
    version='1.0',
    url='https://github.com/adnan904/YAML_contacts',
    author='Adnan Manzoor',
    description='A Python3 Program from storing contacts in a YAML structured File.',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pycontacts = contacts.contacts:main',
        ]
    },
    install_requires=[
          'PyYAML' , 'argparse'
      ]
)
