import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
# For the version use the following ideology
# version = X.Y.Z where
#   X is MAJOR
#   Y is MINOR
#   Z is PATCH
setup(
    name="hallred-chart",
    version="0.0.2",
    description="Data analytics and charting for Verizon System Performance Engineers",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/hallred/chart",
    author="Hal Allred",
    author_email="halley.allred@verizonwireless.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude="tests"),
    install_requires=["numpy", "matplotlib"]
)
