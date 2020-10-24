import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pylibcdb",
    version="0.0.1",
    author="Antonio Pastorelli",
    author_email="neetx@protonmail.com",
    description="libc_database python wrapper for exploit automation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Neetx/pylibcdb",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License:: GPL-3.0 License",
        "Operating System :: OS Linux",
    ],
    python_requires='>=3.7',
)