from setuptools import setup, find_packages

VERSION = '0.0.3'
DESCRIPTION = 'Simple Logger Project'
LONG_DESCRIPTION = 'Simple Logger Project'

setup(
    name='logger',
    version=VERSION,
    author='Josef Kundinger-Markhauser',
    author_email='JoeyMarkhauser@gmail.com',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['logging', 'logger', 'log', 'logs'],
    classifiers=[
        'Development Status :: Alpha',
        'Intended Audience :: ALL',
        'Programing Language :: Python :: 2',
        'Programing Language :: Python :: 3',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: windows',
        'Operation System :: Linux :: Linux'
    ]
)
