'''
The setup.py file is a crucial part of a Python project, especially when you want to distribute your project as a package. It contains metadata about your project and instructions on how to install it. Here are some common uses of setup.py:

Package Metadata: It provides information about the package such as name, version, author, license, etc.
Dependencies: It specifies the dependencies required for your project.
Entry Points: It can define entry points for command-line scripts.
Package Data: It includes non-code files within the package.
Installation Requirements: It specifies any additional requirements for installation.
'''

from setuptools import setup, find_packages
from typing import List

def get_requirements(filepath='requirements.txt') -> List[str]:
    '''
    This fucntion will return list of requirements
    '''
    requirement_lst: List[str] = []
    try:

        with open(filepath,'r') as file:
            lines = file.readlines()

            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    
    except FileNotFoundError as e:
        print("requirements.txt not found")

    return requirement_lst


setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='Ritayan Patra',
    author_email='ritayanpatra98@gmail.com',
    description='It is a machine learning project for network security to detect phising data',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/RITS98/Network-Security',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    python_requires='>=3.6',
)