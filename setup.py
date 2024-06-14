"""
Created on June 14, 2024
@ Author: Vinay Pattanashetti"""

import setuptools
 
with open("README.md", "r", encoding="utf-8") as f:
     long_description = f.read()

__version__ = "0.0.0"

REPO_NAME="NLP-Text-Summarization"
AUTHOR_USERNAME="vinaypattanashetti"
SRC_REPO = "textsummarization"
AUTHOR_EMAIL = "vinay.pattanashetti922821@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author="AUTHOR_USERNAME",
    author_email=AUTHOR_EMAIL,
    description="A small python pacakage for NLP-Text-Summarization app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}",
    project_urls={
         "Bug Tracker": f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)