"""
Docker Remove Obsolete Image
"""
from setuptools import find_packages, setup

dependencies = ['click', 'docker-py']

setup(
    name='docker-rmi',
    version='1.0.1',
    url='https://github.com/vankhoa011/docker-remove-images',
    license='BSD',
    author='Nguyen Vu Van Khoa',
    author_email='vankhoa011@gmail.com',
    description='README.md',
    long_description=__doc__,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    platforms='linux',
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'docker-rmi = docker_rmi.cli:main',
        ],
    },
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        # 'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
