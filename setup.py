import setuptools

setuptools.setup(
    name="hof",
    author="prs-watch",
    version="1.0.1",
    description="not practical tool to make hof as you want.",
    url="https://github.com/prs-watch/hof",
    license="MIT",
    packages=setuptools.find_packages(),
    install_requires = [
        "pybaseball", "click", "rich", "pandas"
    ],
    entry_points={
        "console_scripts": [
            "hof = hof:hof"
        ]
    }
)