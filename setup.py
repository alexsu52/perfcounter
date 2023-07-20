from setuptools import setup

setup(
    name="perfcounter",
    version="0.0.1",
    author="Alexander Suslov",
    author_email="alexsuslovnn@gmail.com",
    description="Light performance counter to profile your python code",
    url="https://github.com/alexsu52/perfcounter",
    license="Apache-2.0",
    packages=["perfcounter"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    install_requires=["texttable"],
    keywords=[
        "python",
        "performance",
        "performance-counter",
        "performance-utils",
        "performance-metrics",
        "performance-mesuring",
        "performance-testing",
    ],
)
