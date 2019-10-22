import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
        name="pybricks-stubs",
        version="0.0.2",
        author="Lawrence (Drew) Whisenant",
        author_email="dwhisenant@FIRSTinAlabama.org",
        description="An stubs package to write EV3 Python code.",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/drewwhis/pybricks-stubs",
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
)
