#The setup.py file is a common component in Python projects and is used for packaging and distributing Python packages. It contains metadata about the package and provides instructions to tools like setuptools on how to build, install, and distribute the package.
from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    ''' 
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements =[req.replace("\n","") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
name = 'mlproject',
version = '0.0.1',
author = 'Sujith',
author_email= 'sujithkumara1729@gmail.com',
packages= find_packages(),
install_requires = get_requirements('requirements.txt')
)