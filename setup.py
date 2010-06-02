try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='geo-utils',
    version='0.1',
    description='Miscellaneous geospatial utilities.',
    author='Ilya Sterin',
    author_email='',
    license='BSD',
    url='http://github.com/isterin/geo-utils',
    packages=find_packages(exclude=['ez_setup']),
    install_requires = [
        "nose>=0.11",
        "numpy>=1.4.1"
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6'
    ]
)