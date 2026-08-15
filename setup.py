from setuptools import setup, find_packages

# get_requirements = lambda file_path: open(file_path).read().splitlines()

def get_requirements(file_path):                  #file_path == requirements.txt
    with open(file_path) as f:
        requirements = f.read().splitlines()

    if '-e .' in requirements:
        requirements.remove('-e .')

    return requirements

setup(
  name = "New Project",
  version = "0.0.1",
  author = "Prem Kumar Singh",
  author_email = "priyanshusingh1307@gmail.com",
  packages = find_packages(),                                # src example
  install_requires = get_requirements('requirements.txt')
)