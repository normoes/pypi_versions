from setuptools import setup, find_packages

from pypi_versions._version import __version__


setup(
    name="pypi_versions",
    version=__version__,
    description=("Compare local depdenencies against Pypi."),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Norman Moeschter-Schenck",
    author_email="norman.moeschter@gmail.com",
    url="https://github.com/normoes/pypi_versions",
    download_url=f"https://github.com/normoes/pypi_versions/archive/{__version__}.tar.gz",
    install_requires=["requests>=2.23.0"],
    # py_modules=["pypi_versions"],
    packages=find_packages(exclude=["tests*"]),
    scripts=["pypi_versions/bin/pypi_versions"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
    ],
)
