import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="jsxgraph",
    version="0.0.1",
    description="Jupyter Notebook/Lab magic wrapper for the JavaScript math-sketching utility JSXGraph",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/chunxy/jsxgraph-magic",
    author="chunxy",
    license="MIT",
    classifiers=[
        "Framework :: IPython",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
    ],    
    packages=["jsxgraph-magic"],
    include_package_data=True,
)