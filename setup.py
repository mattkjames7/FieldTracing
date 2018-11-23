import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="FieldTracing",
    version="0.0.2",
    author="Matthew Knight James",
    author_email="mattkjames7@gmail.com",
    description="A package containing simple algorithms for field tracing.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mattkjames7/FieldTracing",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
		'numpy',
	],
)
