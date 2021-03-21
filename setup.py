import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="devXliff",
    version="1",
    author="Vinayak Sharma",
    author_email="bplate3@gmail.com",
    description="A simple lightweight package to facilitate the programmatic creation of XLIFF files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vinayaksharmagh/devXliff",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=['devXliff'],
    python_requires=">=3.6"
    
)