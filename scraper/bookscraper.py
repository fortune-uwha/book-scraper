from datetime import datetime
from random import randint
from time import sleep

import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup


class BooksScraper:
    """Automated data collection tool (web-scraper) that is specifically
    tailored to scrape data on Bookdepository based on specific category
    keyword.
    """

    def __init__(self, number_of_samples: int, category: str, export_to_csv: bool = False) -> None:
        """
        Initialization
        :param number_of_samples: The number of samples of data to be scraped.
        :category: book category to be scraped
        :param header: web browser information used to construct scraper headers.
        :param baseurl: Url used to collect book categories for scraping.
        :param bool export_to_csv: Should the scraped data be exported to csv?
        """
        self.number_of_samples = number_of_samples
        self.category = category
        self._baseurl = "https://www.bookdepository.com/search?searchTerm="
        self._header = {"User-Agent": "Mozilla/5.0"}
        self._export_to_csv = export_to_csv

    @property
    def number_of_pages(self) -> int:
        """
        Calculates number of pages that will be scraped
        based on number of samples user wants to get.
        By default, each page has 30 samples.
        
        :param : None
        :return: number of pages that will be scraped.
        """
        try:
            if self.number_of_samples < 30:
                raise ValueError(
                    "Number of samples must be equal to or larger than 30.")
            return int(round(self.number_of_samples / 30))
        except TypeError:
            raise TypeError(
                "Number of samples must be of integer type.")from None

    def get_page_response(self, base_url: str, category: str, number_of_pages: int, header: dict) -> BeautifulSoup:
        """
        Retrieves response from book depository server.
        :param url: desired url.
        :category: book category to be scraped. Constructed during Initialization.
        :param number_of_pages: The number of pages of data to be scraped.
        :param header: identification needed for scraping. Constructed during Initialization.
        :return: response. if connection blocked prints error message.
        """
        for page in range(1, number_of_pages+1):
            url = base_url + category + "&page=" + str(page)
            page = requests.get(url, headers=header)
            soup = BeautifulSoup(page.content, "html.parser")
        if not page.ok:
            print(f"There is a {page} error. Please check your URL.")
        else:
            return soup

    @staticmethod
    def get_book_authors(soup, number_of_pages) -> list:
        """
        Function which gathers book authors from the provided
        BeautifulSoup object.
        :param soup: BeautifulSoup object containing book info.
        :param number_of_pages: The number of pages of data to be scraped.
        :return: appends the book author to the selected list. If not provided None is returned.
        """
        authors = []
        try:
            for page in range(1, number_of_pages+1):
                authors.extend([author.text for author in soup.find_all(
                    "span", attrs={"itemprop": "name"})])
            return authors
        except ValueError:
            return np.nan

    @staticmethod
    def get_book_titles(soup, number_of_pages) -> list:
        """
        Function which gathers book titles from the provided
        BeautifulSoup object.
        :param soup: BeautifulSoup object containing book info.
        :param number_of_pages: The number of pages of data to be scraped.
        :return: appends the book title to the selected list. If not provided None is returned.
        """
        titles = []
        try:
            for page in range(1, number_of_pages+1):
                titles.extend(
                    [title.text for title in soup.find_all("h3", class_="title")])
            return titles
        except ValueError:
            return np.nan

    @staticmethod
    def get_book_prices(soup, number_of_pages) -> list:
        """
        Function which gathers book prices from the provided
        BeautifulSoup object.
        :param soup: BeautifulSoup object containing book info.
        :param number_of_pages: The number of pages of data to be scraped.
        :return: appends the book price to the selected list. If not provided None is returned.
        """
        prices = []
        try:
            for page in range(1, number_of_pages+1):
                prices.extend(
                    [price.text for price in soup.find_all("p", class_="price")])
            return prices
        except ValueError:
            return np.nan

    @staticmethod
    def get_book_editions(soup, number_of_pages) -> list:
        """
        Function which gathers book editions from the provided
        BeautifulSoup object.
        :param soup: BeautifulSoup object containing book info.
        :param number_of_pages: The number of pages of data to be scraped.
        :return: appends the book price to the selected list. If not provided None is returned.
        """
        editions = []
        try:
            for page in range(1, number_of_pages+1):
                editions.extend(
                    [edition.text for edition in soup.find_all("p", class_="format")])
            return editions
        except ValueError:
            return np.nan

    @staticmethod
    def get_book_dates(soup, number_of_pages) -> list:
        """
        Function which gathers book prices from the provided
        BeautifulSoup object.
        :param soup: BeautifulSoup object containing book info.
        :param number_of_pages: The number of pages of data to be scraped.
        :return: appends the book price to the selected list. If not provided None is returned.
        """
        publish_dates = []
        try:
            for page in range(1, number_of_pages+1):
                publish_dates.extend(
                    [date.text for date in soup.find_all("p", class_="published")])
            return publish_dates
        except ValueError:
            return np.nan

    @staticmethod
    def get_book_item_urls(soup, number_of_pages) -> list:
        """
        Function which gathers books item url from the provided
        BeautifulSoup object.
        :param soup: BeautifulSoup object containing book info.
        :param number_of_pages: The number of pages of data to be scraped.
        :return: appends the book's item url to the selected list. If not provided None is returned.
        """
        item_urls = []
        item_url_prefix = "https://www.bookdepository.com"
        try:
            for page in range(1, number_of_pages+1):
                item_urls.extend([item_url_prefix+url.a['href']
                                 for url in soup.find_all("div", attrs={"class": "book-item"})])
            return item_urls
        except ValueError:
            return np.nan

    @staticmethod
    def get_book_image_urls(soup, number_of_pages) -> list:
        """
        Function which gathers books image url from the provided
        BeautifulSoup object.
        :param soup: BeautifulSoup object containing book info.
        :param number_of_pages: The number of pages of data to be scraped.
        :return: appends the book's image url to the selected list. If not provided None is returned.
        """
        image_urls = []
        try:
            for page in range(1, number_of_pages+1):
                image_urls.extend([image['data-lazy']
                                  for image in soup.find_all("img", class_="lazy")])
            sleep(randint(1, 3))
            return image_urls
        except ValueError:
            return np.nan

    def collect_information(self) -> pd.DataFrame:
        """
        Function which combines all functions required for scraping.
        
        :param : None
        :return: pandas dataFrame.
        """
        print(
            f">>>>Now collecting information on {self.category} books for {self.number_of_pages} page(s)<<<<")
        print(">>>>Please be patient this might take a while:)<<<<")
        soup = self.get_page_response(
            self._baseurl, self.category, self.number_of_pages, self._header)

        title = self.get_book_titles(soup, self.number_of_pages)
        author = self.get_book_authors(soup, self.number_of_pages)
        price = self.get_book_prices(soup, self.number_of_pages)
        edition = self.get_book_editions(soup, self.number_of_pages)
        publish_date = self.get_book_dates(soup, self.number_of_pages)
        item_url = self.get_book_item_urls(soup, self.number_of_pages)
        image_url = self.get_book_image_urls(soup, self.number_of_pages)

        nested_book_details = [title, author, price,
                               edition, publish_date, item_url, image_url]
        columns = ["title", "author", "price", "edition",
                   "publish_date", "item_url", "image_url"]
        book_details = pd.DataFrame(nested_book_details, columns).T
        book_details['category'] = self.category
        if self.export_to_csv:
            self.export_to_csv(book_details)
        return book_details

    def export_to_csv(self, data: pd.DataFrame) -> None:
        """
        Exports a dataframe to a .csv file in working dir.
        :param data: pandas dataframe
        :return: None
        """
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
        return data.to_csv(f"{self.category}_{timestamp}.csv", index=False)


class CleanBookScraper(BooksScraper):
    """ A subclass of BooksScraper specifically tailored to clean data on bookdepository.com. 
    Takes all functionality of the BooksScraper class for re-use.
    """

    def __init__(self, number_of_samples: int, category: str, export_to_csv: bool = False) -> None:
        """
        Initialization
        :param number_of_samples: The number of samples of data to be scraped. 
        :category: book category to be scraped
        :param bool export_to_csv: Should the scraped data be exported to csv?
        """
        super().__init__(number_of_samples, category)

    @staticmethod
    def process_data(data: pd.DataFrame) -> pd.DataFrame:
        """
        Function which cleans book data from the provided Dataframe.
        :param data: Scraped data containing book info.
        
        :return: pandas dataframe
        """
        data = data.dropna()
        data['title'] = data['title'].str.strip()
        data['title'] = data['title'].str.replace("'", "")
        data['author'] = data['author'].str.replace("'", "")
        data['price'] = data['price'].str.replace("\n", "")
        data['price'] = data["price"].str.split("$", n=2, expand=True)[1]
        data['price'] = data['price'].str.replace("US", "")
        data['price'] = data['price'].str.replace("R", "")
        data['edition'] = data['edition'].str.strip()
        data['publish_date'] = data['publish_date'].str.strip()
        data['released_year'] = data['publish_date'].map(
            lambda x: x.split(' ')[-1])
        data['category'] = data['category'].str.title()
        return data

    def clean_dataframe(self) -> pd.DataFrame:
        """
        Function which combines all functions required for cleaning scraped data.
        
        :param : None
        :return: pandas dataFrame.
        """

        data = self.process_data(self.collect_information())
        if self.export_to_csv:
            self.export_to_csv(data)
        return data
