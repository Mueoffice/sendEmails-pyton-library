from setuptools import setup, find_packages

classifiers = [
    'Devlopment Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Opearating System :: Microsoft :: Windows :: Windows 10',
    'Lisence :: OSI Approved :: MIT Lisence',
    'Programming Language :: Python :: 3'
]

setup(
    name='sendEmails',
    version='0.0.1',
    description='sendEmail module helps you to send your mail with short lines of code as compared to smtplib.',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Mue',
    author_email='rishitsinha29@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='sendEmails',
    packages=find_packages(),
    install_requires=['']
)
