import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='paretochart',
    version='1.0',
    author='Abraham Lee',
    author_email='tisimst@gmail.com',
    description="Pareto chart for python (similar to Matlab's, but much more flexible)",
    url='https://github.com/tisimst/paretochart',
    license='BSD License',
    long_description=read('README.rst'),
    install_requires=['matplotlib'],
    packages=[
        'paretochart'],
    keywords=[
        'matplotlib',
        'pareto',
        'chart',
        'plot',
        'quality',
        'economics',
        'manufacturing'
        ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Customer Service',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Manufacturing',
        'Intended Audience :: Other Audience',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Telecommunications Industry',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: OS Independent',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Topic :: Multimedia',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Multimedia :: Graphics :: Presentation',
        'Topic :: Office/Business',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Visualization',
        ]
    )
