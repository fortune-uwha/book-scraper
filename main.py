from scraper.bookscraper import CleanBookScraper
from database.database import Database


def main():
    db = Database()
    db.delete_tables()
    db.create_tables()
    categories = ["economics", "science", "health"]
    examples_to_scrape = 3000
    for category in categories:
        scraper = CleanBookScraper(examples_to_scrape, category)
        df = scraper.clean_dataframe()
        db.insert_data_into_db(df, category)
    db.export_to_csv("export")
