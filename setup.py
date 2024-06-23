from setuptools import setup, find_namespace_packages


with open('README.md', 'r') as fh:
    readme = "\n" + fh.read()

setup(
    name='pyqt-advanced-slider',
    version='1.1.1',
    author='Niklas Henning',
    author_email='business@niklashenning.com',
    license='MIT',
    packages=find_namespace_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        'QtPy>=2.4.1'
    ],
    python_requires='>=3.7',
    description='A clean and customizable int and float slider widget for PyQt and PySide',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/niklashenning/pyqt-advanced-slider',
    keywords=['python', 'pyqt', 'qt', 'slider', 'int slider', 'float slider'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License'
    ]
)
