import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="osnma_core",
    version="0.0.4",
    author="Aleix Galan",
    author_email="algafi@protonmail.com",
    description="Implementation of OSNMA protocol functions and data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Algafix/osnma_core",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
    'bitstring',
    'ecdsa'
    ],
)