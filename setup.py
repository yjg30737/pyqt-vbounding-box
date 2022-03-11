from setuptools import setup, find_packages

setup(
    name='pyqt-vertical-selection-square-graphics-view',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt QGraphicsView with selection box. User can move horizontal border of the box vertically.',
    url='https://github.com/yjg30737/pyqt-vertical-selection-square-graphics-view.git',
    install_requires=[
        'PyQt5>=5.8'
    ]
)