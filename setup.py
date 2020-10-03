from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')
setup(
    name = "Tuby",
    version = "3.5.8",
    author = "Guru Prasadh J.",
    author_email = "guruprasadh_j@outlook.com",
    description = "Super Fast YouTube Downloader ",
    license = "MIT",
    url = "https://github.com/guruprasadhj/Tuby",
    packages=find_packages(),
    entry_points = {
        'console_scripts' : [
            'tuby-gui  = tuby.tuby:tuby',
            'tuby-cli  = tuby.main:main'
            ]},
    #data_files = [('share/applications/', ['vxlabs-myscript.desktop'])],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        ],
    project_urls={ 
        'Bug Reports': 'https://github.com/guruprasadhj/Tuby/issues',
        'Source': 'https://github.com/guruprasadhj/Tuby/',
    },
 
)
