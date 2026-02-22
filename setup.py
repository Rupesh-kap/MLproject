#this is for as we will create m project as a package and deploy as a package 
from setuptools import find_packages,setup
from typing import List

he='-e .'# when you pip req.txt this e. will map it with setup
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file:
        requirements=file.readlines()# by default adds/n
        requirements=[req.replace("\n","") for req in requirements]
        if he in requirements:
            requirements.remove(he)
        return requirements    
    
setup(
    name='MLPROJECT',
    version='0.0.1',
    author='Rupesh',
    author_email='rupeshkaprwan6@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    )