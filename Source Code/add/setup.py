import os
from setuptools import setup

setup(
    name = "add",
    version = "1.0",
    author = "RajasxPuranikxAnupam",
    author_email = "anupampatil44@gmail.com",
    packages=['add'],
    package_dir={'add':'add/'},
    license = "MIT",
    entry_points = {
        'console_scripts' : ['add = add.add:main']
    },
    classifiers=[
    	"Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
        "Operating System :: POSIX :: Linux"
    ],
    python_requires=">=3.5"
)
