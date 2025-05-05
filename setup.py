from setuptools import setup, find_packages

setup(
    name="stpackagetool",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'stpackagetool=stpackagetool.main:main',
        ],
    },
    description="Test package tool",
    author="Your Name",
    author_email="sacha.thuault@gmail.com",
    url="https://github.com/SachaThuault/stpackagetool",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)