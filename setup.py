from setuptools import setup, find_packages

DESCRIPTION = 'Implementation of Topsis'

try:
    with open('README.md', 'r', encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

VERSION = '1.0.3'

setup(
    name="Topsis-YashPuri-102103812",
    version=VERSION,
    author="Yash Puri",
    author_email="ypuri1_be21@thapar.edu",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['pandas', 'numpy'],
    project_urls={
        'Project Link': 'https://github.com/YashPurii/Topsis_pkg'
    },
    keywords=['Topsis', 'Topsis-YashPuri-102103812', 'Yash', 'Topsis-YashPuri', '102103812'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ]
)
