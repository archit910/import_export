import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="import_export",
    version="0.0.2",
    author="Archit Chauhan",
    author_email="architchauhan910@gmail.com",
    description="Import export bulk",
    long_description=long_description,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7", "Python :: 3.6", "Python :: 3.9",
        "Operating System :: OS Independent",
    ],
)
