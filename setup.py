from setuptools import setup, find_packages
setup(
    name = "EZgal",
    version = "2.1",
    packages = find_packages(),
    install_requires = ['numpy>=1.6', 'scipy>=0.12'],
    # metadata for upload to PyPI
    author = "Thuso Simon",
    author_email = "dr.danger.simon@gmail.com",
    description = "SSP handeler for on the fly csp generation for multiple models",
    license = "GPLv2",
    keywords = "SED, SSP, CSP, BC03",
    url = "https://github.com/drdangersimon/EZgal",
    classifiers=[
        'License :: OSI Approved :: GPLv2 License',
        'Programming Language :: Python :: 2 :: Only',
        'Topic :: Scientific/Engineering :: Astronomy spectral fitting']
)
