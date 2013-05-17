from distutils.core import setup
from ariane_old import __version__

setup(
    name='Ariane',
    version=__version__,
    author='Guillaume Vincent',
    author_email='vincent.guillaume.inp@gmail.com',
    packages=['ariane', 'ariane.tests'],
    url='https://github.com/guillaumevincent/Ariane',
    license='wtfpl - Do what the fuck you want to public license',
    description='Ariane is a python package for describing, producing and visualizing RESTful APIs',
    long_description=open('README').read(),
    install_requires=[
        "jinja2 >= 0.7.6",
    ],
)
