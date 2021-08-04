import csv

import config
import pandas as pd
from datetime import datetime
from psycopg2 import DataError, OperationalError, ProgrammingError, connect


class Database:
    def __init__(self) -> None:
        """
        Database class. This handles all connections to the PostgreSQL database on heroku.
        """
        self.__host = config.HOST
        self.__db = config.DB
        self.__user = config.USER
        self.__password = config.PASSWORD
        self.__port = config.PORT

    def connect(self) -> None:
        """
        Connects to the database. Reads the credentials from config.py.

        :return: Operational error if connection is unsuccessful.
        """
        try:
            connection = connect(
                host=self.__host,
                database=self.__db,
                user=self.__user,
                password=self.__password,
                port=self.__port,
            )
            return connection
        except OperationalError as error:
            raise error

    def execute_query(self, query: str) -> None:
        """
        Executes SQL query. For queries which do not return any results, for example:
        INSERT, UPDATE, CREATE, ALTER, DROP, etc.
        :param query: SQL query
        :return: None
        """
        try:
            connection = self.connect()
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            connection.close()
        except ProgrammingError as error:
            raise error

    def execute_query_and_fetch(self, query: str) -> list:
        """
        Executes SQL query and fetches a response. For queries which return results, for example: SELECT.
        :param query: SQL query
        :return: array
        """
        try:
            connection = self.connect()
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            connection.close()
            return result
        except ProgrammingError as error:
            raise error

    def create_tables(self) -> None:
        """
        Creates categories and book table and foreign keys.
        :return: None
        """
        try:
            print("Creating categories table")
            self.execute_query(
                """
                CREATE TABLE IF NOT EXISTS categories(id SERIAL PRIMARY KEY,
                category VARCHAR(25) UNIQUE);"""
            )

            print("Creating book table")
            self.execute_query(
                """
                CREATE TABLE IF NOT EXISTS books (id SERIAL PRIMARY KEY,
                title VARCHAR(255),
                author VARCHAR(64),
                price VARCHAR(25),
                item_url VARCHAR(255),
                image_url VARCHAR(255),
                category_id INTEGER);"""
            )

            print("Setting up foreign keys")
            self.execute_query(
                """
                ALTER TABLE books
                ADD FOREIGN KEY (category_id) 
                REFERENCES Categories(id);"""
            )
            print(">>>>Successful!<<<<")
        except ProgrammingError as error:
            raise error

    def delete_tables(self) -> None:
        """
        deletes book and categories tables from the database
        :return: Tables successfully deleted message
        """
        try:
            self.execute_query("DROP TABLE IF EXISTS books")
            self.execute_query("DROP TABLE IF EXISTS categories")
            print("Books and Categories tables no longer in database.")
        except ProgrammingError as error:
            raise ProgrammingError(
                "There was a problem dropping table in the specified database"
            )

    def insert_data_into_db(self, dataframe: pd.DataFrame, category: str) -> None:
        """
        Inserts dataframe into the database.
        :param dataframe: pandas Dataframe
        :param category: category of the data
        :return: None
        """
        try:
            print("Inserting data into the database")
            self.execute_query(
                f"""
                INSERT INTO categories(category) 
                VALUES('{str.capitalize(category)}') 
                ON CONFLICT DO NOTHING"""
            )
            category_id = self.execute_query_and_fetch(
                f"SELECT id FROM categories WHERE category = '{str.capitalize(category)}'"
            )
            data_array = dataframe.to_records(index=False)
            query = ""
            for row in data_array:
                title, author, price, item_url, image_url = row
                query += f"""
                    INSERT INTO books(category_id, title, author, price, item_url, image_url) 
                    VALUES ({category_id[0][0]}, '{title}', '{author}', '{price}', '{item_url}', '{image_url}');"""

            self.execute_query(query)
            print(">>>>>Successful!<<<<")
        except DataError as error:
            raise DataError("Please try again. Could not perform the requested query")

    def export_to_csv(self, title: str) -> csv:
        """
        Connects to the database, fetches the data and exports the data to csv file.
        :return: csv file
        """
        try:
            print("Exporting to csv")
            books = self.execute_query_and_fetch(
                """
                SELECT books.id, title, author, category, price, item_url, image_url 
                FROM books
                LEFT JOIN categories ON books.category_id = categories.id
                ORDER BY books.id"""
            )
            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
            columns = [
                "id",
                "title",
                "author",
                "category",
                "price",
                "item_url",
                "image_url",
            ]
            books_df = pd.DataFrame(books)
            books_df.to_csv(f"{title}_{timestamp}.csv", index=False, header=columns)
            print(f">>>>>Sucessfull. Data exported as {title}_{timestamp}.csv<<<<<")
            return
        except DataError as error:
            raise error
