import io
import os

from setuptools import find_packages, setup


def read(*paths, **kwargs):
    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="laboras",
    version="0.1.0",
    description="Laboras is a social posting app",
    url="laboras.io",
    python_requires=">=3.8",
    long_description="Laboras is a social posting app",
    long_description_content_type="text/markdown",
    author="Johnson Neto",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=read_requirements("requirements.txt"),
    entry_points={"console_scripts": ["laboras = laboras.cli:main"]},
)
