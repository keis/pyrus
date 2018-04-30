from setuptools import setup

setup(
    name='pyrus',
    py_modules=['pyrus'],
    version='1.1.1',
    install_requires=[
        'structlog',
        'ansicolors'
    ],
    license='MIT',
    description='A logrus inspired renderer for structlog',
    keywords='logging structlog colour color'
)
