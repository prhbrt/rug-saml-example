from setuptools import setup

setup(
    name='rugsamlexample',
    version=__import__('rugsamlexample').__version__,

    description='Example login using SAML 2 for the University of Groningen Single sign-on service',
    long_description='Example login using SAML 2 for the University of Groningen Single sign-on service',

    url='https://github.com/prinsherbert/rug-saml-example',

    author='Herbert Kruitbosch',
    author_email='H.T.Kruitbosch@rug.nl',
    license='Only for use within the University of Groningen and only with permission from the authors.',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Scientists',
        'License :: Only with authors permission',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='rug, university of groningen, rijkuniversiteit groningen, saml2, saml, authenticatie, single sign on',

    install_requires=[
        'django>=1.11.1,<1.12',
        'django-tables2>=1.6.1,<1.7',
        'django-bootstrap3>=8.2.3,<8.3',
        'django-saml2-auth>=2.1.1,<3'
    ],
    zip_safe=False,
)
