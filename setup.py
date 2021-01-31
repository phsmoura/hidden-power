from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requires = f.read().splitlines()

setup(
    name="hiddenpower",
    version="0.1",
    packages=find_packages(),
    install_requires=requires,
    entry_points={
        'console_scripts': [
            'hiddenpower=hiddenpower.main:cli'
        ]
    }
)
