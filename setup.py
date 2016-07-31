from setuptools import find_packages, setup

setup(
    name='django-click-counter',
    version='1.0.0',
    author='Sagar Chakravarthy',
    author_email='bp.sagar@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=1.9',
    ],
    zip_safe=False
)
