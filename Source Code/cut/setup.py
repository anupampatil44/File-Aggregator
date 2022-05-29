import os
from setuptools import setup

setup(
    name = "cut_util",
    version = "1.0",
    author = "RajasxPuranikxAnupam",
    author_email = "anupampatil44@gmail.com",
    packages=['cut_util'],
    package_dir={'cut_util':'cut/'},
    license = "MIT",
    entry_points = {
        'console_scripts' : ['cut_util = cut_util.cut_util:main']
    },
    classifiers=[
    	"Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
        "Operating System :: POSIX :: Linux"
    ],
    python_requires=">=3.5"
)
