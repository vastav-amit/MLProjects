from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT ='-e .'

def get_requirements(file_path:str)->list[str]:

    '''
    This function will return the list of requirements'''
    requirements = []
    with open(file_path) as file_obj:
        #reading packages for installation from requirements file
        requirements=file_obj.readlines()
        #replacing the \n
        requirements=[req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        return requirements



setup(
name="MLProject",
version='0.0.1',
author='Amit',
author_email='amit.cr92@gmail.com',
packages=find_packages(),
install_requires = get_requirements('requirements.txt')


)