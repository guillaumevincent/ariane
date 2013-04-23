from distutils.core import setup

setup(
    name='Ariane',
    version='0.0.1',
    author='Guillaume Vincent',
    author_email='vincent.guillaume.inp@gmail.com',
    packages=['ariane', 'ariane.test'],
    url='https://github.com/guillaumevincent/Ariane',
    license='LICENSE',
    description='Ariane is a python package for describing, producing and visualizing RESTful APIs',
    long_description=open('README').read(),
    install_requires=[
        "Jinja2 >= 0.7.6",
    ],
)
