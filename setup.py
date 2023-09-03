from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str) -> List[str]:
    """
    Will return the list of required libraries
    """

    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")

    return requirements

setup(
    name="MLProject",
    version="0.0.1",
    author="Javier",
    author_email="javier.nezcia@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)