import setuptools
from setuptools import find_packages
import re

with open("./linkedin_python/__init__.py", "r") as f:
    content = f.read()
    # from https://www.py4u.net/discuss/139845
    version = re.search(r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]', content).group(1)

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="linkedin_python",
    version=version,
    author="zuppif",
    author_email="francesco.zuppichini@gmail.com",
    description="Create LinkedIn content using Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    install_requires=["requests"],
    packages=find_packages(exclude="test"),
    extras_require={
        "dev": ["flake8", "black==22.3.0", "isort", "twine", "pytest", "wheel"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
