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
        'beautifulsoup4==4.9.3',
        'black==19.10b0',
        'certifi==2021.5.30',
        'chardet==4.0.0',
        'idna==2.10',
        'numpy==1.21.1',
        'pandas==1.3.1',
        'psycopg2==2.9.1',
        'python-dateutil==2.8.1',
        'pytz==2021.1',
        'requests==2.25.1',
        'soupsieve==2.2.1',
        'urllib3==1.26.6'
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    python_requires=">=3.6",
)
