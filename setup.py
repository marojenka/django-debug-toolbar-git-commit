from setuptools import setup, find_packages

setup(
    name='django-debug-toolbar-git-commit',
    version='0.0.1',
    description='A git log panel for the Django Debug Toolbar',
    long_description=open('README.md').read(),
    # Get more strings from http://www.python.org/pypi?:action=list_classifiers
    author='Mark Selshot',
    author_email='mirkerz@gmail.com',
    url='https://github.com/marojenka/django-debug-toolbar-git-commit',
    download_url='https://github.com/github.com/marojenka/django-debug-toolbar-git-commit/downloads',
    license='BSD',
    packages=find_packages(exclude=('tests', 'example')),
    tests_require=[
        'django>=1.5',
    ],
    test_suite='runtests.runtests',
    include_package_data=True,
    zip_safe=False,
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
