import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Math",
    version = "0.0.1",
    author = "Breno Robazza",
    author_email = "breno.robazza@hotmail.com",
    description = ("My math package"),
    license = "BSD",
    keywords = "Math",
    url = "",
    packages=['LinearRegression'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)