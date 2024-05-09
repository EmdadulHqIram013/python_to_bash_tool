from setuptools import setup, find_packages

setup(
    name="pytobash",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pytobash = python_to_bash.cli:main',
        ],
    },
    install_requires=[
    ],
    include_package_data=True,
    description="A tool to convert Python scripts to Bash scripts.",
    author="Emdadul Haque Iram",
    author_email="iramhq14@gmail.com",
    url="https://github.com/EmdadulHqIram013/python_to_bash_tool",  
)


