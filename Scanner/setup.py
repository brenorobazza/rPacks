import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Scanner",
    version = "0.0.1",
    author = "Breno Robazza",
    author_email = "breno.robazza@hotmail.com",
    description = ("Scan images"),
    license = "BSD",
    keywords = "Scan images",
    url = "",
    py_modules = ['Scanner.Scanner'],
    # packages=['pkg'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)