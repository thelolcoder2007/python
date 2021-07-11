from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = ( here / 'readme.md').read_text(encoding = 'utf-8')

setup(
    name='fleurhome',
    version='1.0.1',
    description='Just a normal project...',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/thelolcoder2007/python',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3.9',
    ],
    packages=find_packages(where="fleurhome"),
    python_requires='>=3, <4'
)
