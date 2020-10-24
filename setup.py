"""
Copyright 2020 Neetx

This file is part of pylibcdb.

pylibcdb is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

pylibcdb is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with pylibcdb.  If not, see <http://www.gnu.org/licenses/>.
"""

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