from typing import List
from setuptools import find_packages,setup
HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:
	"""
	This function Will return the list of requirements
	"""
	requirements = []
	with open(file_path) as file_obj:
		requirements = file_obj.readlines()
		requirements = [req.replace("\n","") for req in requirements]
		
		if HYPEN_E_DOT in requirements:
			requirements.remove(HYPEN_E_DOT)
	return requirements
		
setup(
name='ml-project',
version='0.0.1',
author='Hari',
author_email='hpofficial420@gmail.com',
packages=find_packages(),
install_requires=['pandas','numpy','seaborn']
)
