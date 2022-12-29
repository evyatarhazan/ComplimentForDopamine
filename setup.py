from setuptools import setup, find_packages

setup(
    name="ComplimentForDopamine",
    packages=find_packages(include=['ComplimentForDopamine']),
    version="1.0.0",
    py_modules=["compliment_generator"],
    author="Evyatar Hazan",
    author_email="7127547@email.com",
    description="A Python package that generates compliments for a given name",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
