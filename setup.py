 from setuptools import setup, find_packages

setup(
    name="texl",
    version="0.1",
    description="Console application for latex",
    author="Yunhyeon Jeong",
    author_email="spaceship2021@gmail.com",
    license=license,
    packages=find_packages(exclude=("docs", "test", "sample")),
    install_requires=[
        "pyperclip",
        "pyinstaller"
    ]
)