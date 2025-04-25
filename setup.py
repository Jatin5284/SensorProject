from setuptools import find_packages , setup # setuptools is a library written specifically for packaging python projects
from typing import List

HYPEN_E_DOT = '-e.' # hyphen e dot is used to indicate editable package

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return a list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n" , "") for req in requirements]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name = 'Fault detection' ,
    version ='0.0.1' ,
    author = 'jatin' ,
    author_mail = 'jatinbansal52846@gmail.com' ,
    install_requirements = get_requirements('requirements.txt') ,
    packages = find_packages()

)