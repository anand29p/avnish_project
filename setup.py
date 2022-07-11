from setuptools import setup,find_packages
from typing import List

#Declaring variables for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.2"
AUTHOR="Anand"
DESRCIPTION="This is a first complete Machine Learning Project"
PACKAGES = ["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list() -> List[str]:
    """
    Description: This function is going to return list of requirement
    mention in requirements.txt file
    return This function is going to return a list which contain name
    of libraries mentioned in requirements.txt file
    """
    
setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESRCIPTION,
packages=PACKAGES, 
install_requires=get_requirements_list()
)
    