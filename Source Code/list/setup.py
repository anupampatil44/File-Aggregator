import os
from setuptools import setup

setup(
    name = "list",
    version = "1.0",
    author = "RajasxPuranikxAnupam",
    author_email = "anupampatil44@gmail.com",
    packages=['list'],
    package_dir={'list':'list/'},
    license = "MIT",
    entry_points = {
        'console_scripts' : ['list = list.list:main']
    },
    classifiers=[
    	"Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
        "Operating System :: POSIX :: Linux"
    ],
    python_requires=">=3.5"
)
