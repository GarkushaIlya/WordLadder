from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='word_ladder',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    python_requires=">=3.9",
    entry_points={
        'console_scripts':
            ['word_ladder = wordladder.main:main']
    }
)
