# Build the workflow project

from setuptools import setup, Extension, find_packages
import re
import os


# Getting description:
with open("README.md", "r") as fh:
    long_description = fh.read()

# Getting requirements:
with open("requirements.txt") as requirements_file:
    requirements = requirements_file.readlines()

# Getting version:
with open("./src/__init__.py") as init_file:
    version = re.search("__version__ = \"(.*?)\"", init_file.read()).group(1)

setup(
    name='pysysinfo',
    version=version,
    scripts=[],
    author="Ganesh B",
    author_email="desktopcgi@gmail.com",
    maintainer="Ganesh B",
    maintainer_email="desktopcgi@gmail.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ganeshkbhat/py-device-info",
    download_url="https://pypi.org/project/pysysinfo/",
    packages=find_packages(),
    # package_dir={
    #     # "": "pysysinfo",
    # },
    # package_data={
    #     # "some_dep": ["*.pxd", "*.pyi", "py.typed"],
    # },
    ext_modules=[],
    install_requires=[],
    extras_require={},
    zip_safe=True,
    entry_points={
        'console_scripts': []
    },
    license='Proprietary',
    platforms=["any"],
    keywords=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        # "License :: OSI Approved :: MIT License",
        "License :: Free To Use But Restricted",
        "License :: Free For Educational Use",
        "License :: Freely Distributable",
        "Operating System :: OS Independent"
        # 'Operating System :: POSIX :: Linux',
        # 'Operating System :: Microsoft :: Windows',
        # 'Operating System :: MacOS'
    ],
)


"""
ext_modules=[
        Extension("dependency_injector.containers",
                ["src/dependency_injector/containers.c"],
                define_macros=list(defined_macros.items()),
                extra_compile_args=["-O2"]),
        Extension("dependency_injector.providers",
                ["src/dependency_injector/providers.c"],
                define_macros=list(defined_macros.items()),
                extra_compile_args=["-O2"]),
    ],
"""

# RUN setup.py with below command
# python3 setup.py sdist bdist_wheel

# The Pypirc file stores the PyPi repository information
# https://docs.python.org/2.5/dist/pypirc.html
# for Windows :  C:\Users\UserName\.pypirc
# for *nix :   ~/.pypirc

# To upload your dist/*.whl file on PyPi https://pypi.org/, use Twine
# python3 -m twine upload dist/*
