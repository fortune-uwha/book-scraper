import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='books_scraper',
    version='0.0.1',
    license='MIT',
    description='This is an automated data collection package (web-scraper) that is specifically tailored to scrape data on the Book depository website',
    author='Fortune Uwha',
    author_email='fortune.uwha@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/fortune-uwha/scrape_books',
    packages=setuptools.find_packages(),
    install_requires=[
        'atomicwrites==1.4.0',
        'attrs==20.3.0',
        'beautifulsoup4==4.9.3',
        'certifi==2020.12.5',
        'chardet==4.0.0',
        'colorama==0.4.4',
        'idna==2.10',
        'iniconfig==1.1.1',
        'lxml==4.6.2',
        'numpy==1.19.5',
        'packaging==20.8',
        'pandas<=1.2.0',
        'pluggy==0.13.1',
        'py==1.10.0',
        'pyparsing==2.4.7',
        'pytest==6.2.1',
        'python-dateutil==2.8.1',
        'pytz==2020.5',
        'requests==2.25.1',
        'six==1.15.0',
        'soupsieve==2.1',
        'toml==0.10.2',
        'urllib3==1.26.2'
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    python_requires=">=3.6",
)
