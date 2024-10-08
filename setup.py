from setuptools import setup, find_packages

setup(
    name='tornetx',
    version='2.1.2',
    packages=find_packages(),
    install_requires=[
        'colorama',
        'requests',
        'stem',
    ],
    entry_points={
        'console_scripts': [
            'tornetx=tornetx.tornetx:main',
        ],
    },
    author="ByteBreach",
    author_email="mrfidal@proton.me",
    maintainer="Macxzew",
    maintainer_email="macxzew@proton.me",
    description="TorNetX - Automate IP address changes using Tor (Adapted by Macxzew)",
    license="MIT",
    url="https://github.com/Macxzew/tornetx",
    project_urls={
        'Original Repo': 'https://github.com/ByteBreach/tornet',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
