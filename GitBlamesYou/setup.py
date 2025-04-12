from setuptools import setup, find_packages

setup(
    name='gitblamesyou',
    version='0.1',
    packages=find_packages(include=['gitblamesyou']),
    install_requires=[
        'chardet==5.2.0',
        'pillow==11.1.0',
        'reportlab==4.3.1'
    ],
    entry_points={
        'console_scripts': [
            'blaming=gitblamesyou.gitBlame:main'
        ]
    },
    author='Emilia Diaz',
    description='Paquete para cálculo de líneas por autor.',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License'
    ],
    python_requires='>=3.6',
)
