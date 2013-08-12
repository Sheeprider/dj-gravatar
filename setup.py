from setuptools import setup, find_packages
import gravatar

setup(
    name='dj-gravatar',
    version=gravatar.__version__,
    packages=find_packages(),
    long_description=open('README').read(),
    install_requires=[
        'Django',
    ]
)
