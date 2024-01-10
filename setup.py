from setuptools import setup, find_packages
import io
import os

VERSION = "3.36"


def get_long_description():
    with io.open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="duckdb-utils",
    description="CLI tool and Python library for manipulating DuckDB databases",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Booth",
    version=VERSION,
    license="Apache License, Version 2.0",
    packages=find_packages(exclude=["tests", "tests.*"]),
    package_data={"duckdb_utils": ["py.typed"]},
    install_requires=[
        "sqlite-fts4",
        "click",
        "click-default-group>=1.2.3",
        "tabulate",
        "python-dateutil",
        "pluggy",
    ],
    extras_require={
        "test": ["pytest", "black", "hypothesis", "cogapp"],
        "docs": [
            "furo",
            "sphinx-autobuild",
            "codespell",
            "sphinx-copybutton",
            "beanbag-docutils>=2.0",
            "pygments-csv-lexer",
        ],
        "mypy": [
            "mypy",
            "types-click",
            "types-tabulate",
            "types-python-dateutil",
            "types-pluggy",
            "data-science-types",
        ],
        "flake8": ["flake8"],
        "tui": ["trogon"],
    },
    entry_points="""
        [console_scripts]
        duckdb-utils=duckdb_utils.cli:cli
    """,
    url="https://github.com/databooth/duckdb-utils",
    project_urls={
        "Documentation": "https://duckdb-utils.databooth.com.au/en/stable/",
        "Changelog": "https://duckdb-utils.databooth.com.au/en/stable/changelog.html",
        "Source code": "https://github.com/databooth/duckdb-utils",
        "Issues": "https://github.com/databooth/duckdb-utils/issues",
        "CI": "https://github.com/databooth/duckdb-utils/actions",
    },
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Database",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    # Needed to bundle py.typed so mypy can see it:
    zip_safe=False,
)
