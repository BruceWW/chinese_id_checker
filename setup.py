# encoding: utf-8
from setuptools import setup, find_packages

SHORT = 'chinese id checker'

__version__ = "0.9.2"
__author__ = 'Lin Luo / Bruce Liu'
__email__ = '15869300264@163.com'

readme_path = 'README.md'

setup(
    name='chinese_id_checker',
    version=__version__,
    packages=find_packages(),
    install_requires=[],
    url='https://github.com/BruceWW/chinese_id_checker',
    author=__author__,
    author_email=__email__,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    include_package_data=True,
    package_data={'': ['*.py', '*.pyc']},
    zip_safe=False,
    platforms='any',

    description=SHORT,
    long_description=open(readme_path, encoding='utf-8').read(),
    long_description_content_type='text/markdown',
)
