from distutils.core import setup

setup(
    name='Ariane',
    version='0.0.2',
    author='Guillaume Vincent',
    author_email='vincent.guillaume.inp@gmail.com',
    packages=['ariane', 'ariane.test'],
    url='https://github.com/guillaumevincent/Ariane',
    license='WTFPL - DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE',
    description='Ariane is a python package for describing, producing and visualizing RESTful APIs',
    long_description=open('README').read(),
)
