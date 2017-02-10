from setuptools import setup

setup(
    name='pyrus',
    py_modules=['pyrus'],
    version='1.0.0',
    install_requires=[
        'structlog',
        'ansicolors'
    ],
    license='MIT',
    description='A logrus inspired renderer for structlog',
    keywords='logging structlog colour color'
)
