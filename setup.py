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
        'appdirs==1.4.4',
        'argh==0.26.2',
        'arrow==0.13.1',
        'atomicwrites==1.4.0',
        'beautifulsoup4==4.9.3',
        'black==19.10b0',
        'brotlipy==0.7.0',
        'certifi==2021.5.30',
        'entrypoints==0.3',
        'future==0.18.2',
        'inflection==0.5.1',
        'MarkupSafe==1.1.1',
        'mccabe==0.6.1',
        'mistune==0.8.4',
        'mypy-extensions==0.4.3',
        'numpy==1.21.1',
        'pandas==1.3.1',
        'parso==0.7.0',
        'pathspec==0.7.0',
        'PyYAML==5.4.1',
        'pyzmq==20.0.0',
        'QtPy==1.9.0',
        'sip==4.19.13',
        'soupsieve==2.2.1'
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    python_requires=">=3.6",
)
