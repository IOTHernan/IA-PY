from setuptools import setup, find_packages

setup(
    name='scripts',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    description='Paquete para ejecutar scripts de PowerShell y Bash',
    author='Hernán Enrique Canestraro',
    author_email='hernancanestraro@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
