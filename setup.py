from setuptools import setup, find_packages

setup(
    name="RPi_SocketComm",
    version="0.1.0",
    description="Socket communication package for RFID systems like IDENTIUM and SECUREYE",
    author="Bidyadhar Muduli",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
