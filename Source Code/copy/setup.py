import os
from setuptools import setup

setup(
    name = "copy_util",
    version = "1.0",
    author = "RajasxPuranikxAnupam",
    author_email = "anupampatil44@gmail.com",
    packages=['copy_util'],
    package_dir={'copy_util':'copy/'},
    license = "MIT",
    entry_points = {
        'console_scripts' : ['copy_util = copy_util.copy_util:main']
    },
    classifiers=[
    	"Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
        "Operating System :: POSIX :: Linux"
    ],
    python_requires=">=3.5"
)
