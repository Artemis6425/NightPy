from setuptools import setup

setup(
    name='NightPy',
    version='2024.4.22',

    description='NightBot API wrapper.',

    # The project's main homepage.
    url='https://www.IamGregAmato.com',

    # Author details.
    author='Aurora Rose',
    author_email='aurorarose6425@gmail.com',

    # License
    license='Apache License v2.0',

    # Classifiers
    classifiers=[
        # Project Stage:
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3 :: Only',
    ],
    # Keywords
    keywords=['NightPy', 'NightBot', 'Artemis', 'API'],

    packages=['NightPy'],

    # Required dependencies. Will be installed by pip
    # when the project is installed.
    install_requires=['requests'],
)
