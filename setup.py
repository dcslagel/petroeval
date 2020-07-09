import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="petroeval", # Replace with your own username
    version="1.0.2",
    author="Ibrahim Olawale",
    author_email="ibrahim.olawale13@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/olawaleibrahim/formeval",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)