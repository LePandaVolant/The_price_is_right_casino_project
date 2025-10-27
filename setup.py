from setuptools import setup, find_packages

setup(
    name='gambling-simulation',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'numpy',
        'matplotlib',
    ],
    entry_points={
        'console_scripts': [
            'gamble=main:main',  # Assuming main.py has a main function to run the simulation
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A gambling simulation project that implements various strategies and statistical analyses.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/gambling-simulation',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)