

# this file is purposely for moving and distributing your source code in the form of a package

# and i can move it to pypi

from setuptools import find_packages, setup
from typing import List

HYPEN_DOT = "-e ."
def get_requirements(file_path:str)->List[str]:
    """
        reutrns list of packages and requirements
    s
    
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    
        if HYPEN_DOT in requirements:
            requirements.remove(HYPEN_DOT)

setup(
    name="Student Performance",
    version="0.0.1",
    author="Alhamdu",
    author_email="jallowalhamdou20@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt"),
)