# Book Depository Scraper
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
![](https://github.com/fortune-uwha/scrape_books/blob/main/assets/book_depository%20logo.png)
## Table of Contents
* [General Information](#general-information)
* [Installation](#installation)
* [Usage](#usage)
* [Features](#features)
* [Project Status](#project-status)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
* [License](#license)

## General Information
This is an automated data collection package (web-scraper) that is specifically tailored to scrape data on the Book depository website based on specific category keyword of choice. Check [features](#features) of this scraper for details.

## Installation
Use the package installer [pip](https://pip.pypa.io/en/stable/) to install book scraper.
* Install directly from github repository
```python
!pip install git+https://github.com/fortune-uwha/scrape_books
```
## Usage
The BooksScraper takes two arguments: number of examples to scrape and keyword to search. This returns a Pandas DataFrame with the records, with an option to export to a csv file.
* To export raw data without cleaning:
```python
from scraper.bookscraper import BooksScraper
scraper = BooksScraper(3000, "economics", True)
scraper.collect_information()
```
* To export clean data:
```python
from scraper.bookscraper import CleanBookScraper
scraper = CleanBookScraper(3000, "economics", True)
scraper.clean_dataframe()
```
For more information just type help(BooksScraper) or help(CleanBookScraper).

## Features
Based on specified category, BooksScraper collects information on:
* Book title
* Book author
* Book price
* Book item url
* Book image url

## Project Status
Project is: in progress

## Acknowledgements
This project was based on [Turing College](https://www.turingcollege.com) learning on SQL and Data Scraping.

## Contact
Created by [@fortune_uwha](https://fortune-uwha.github.io/Fortune_Portfolio/) - feel free to contact me!

## License
This project is open source and available under the terms of the [MIT](https://opensource.org/licenses/MIT) license.
