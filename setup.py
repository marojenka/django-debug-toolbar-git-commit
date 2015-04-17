from setuptools import setup, find_packages

setup(
    name='django-debug-toolbar-git-status',
    version='0.0.1',
    description='A git log panel for the Django Debug Toolbar',
    long_description=open('README.md').read(),
    # Get more strings from http://www.python.org/pypi?:action=list_classifiers
    author='Mark Selshot',
    author_email='mirkerz@gmail.com',
    url='https://github.com/sjhewitt/django-debug-toolbar-git-status',
    download_url='https://github.com/github.com/sjhewitt/django-debug-toolbar-git-status/downloads',
    license='BSD',
    packages=find_packages(exclude=('tests', 'example')),
    tests_require=[
        'django>=1.5,<1.7',
    ],
    test_suite='runtests.runtests',
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
