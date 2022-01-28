from importlib.metadata import entry_points
from setuptools import setup

setup(
    name="hof",
    version="0.0.0",
    py_modules=["cmd"],
    install_requires = [
        "pybaseball", "click"
    ],
    entry_points={
        "console_scripts": [
            "hof = hof:hof"
        ]
    }
)