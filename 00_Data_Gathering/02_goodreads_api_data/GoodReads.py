from goodreads import client
import pandas as pd
import pickle
import time
from goodreads.request import GoodreadsRequest
from goodreads.request import GoodreadsRequestException
gc = client.GoodreadsClient('fwPQlCIO7e2UGe7ETreIA', 'eAedByj5h9CvGwNft0pTpjGtrCrS6Ong9BSHxLWew')

def goodreads_df(isbn_list):
    base_df = pd.DataFrame()
    for i in range(len(isbn_list)):
        print(i)
        try:
            book = gc.book(isbn = isbn_list[i])
            book_dict = {'gid': book.gid, 'title': book.title, 'authors': book.authors, 'description': book.description, 'avg_rating': book.average_rating,
            'rating_dist': book.rating_dist, 'ratings_count': book.ratings_count, 'text_reviews_count': book.text_reviews_count,
             'num_pages': book.num_pages,
             'publication_date': book.publication_date, 'publisher': book.publisher, 'language_code': book.language_code, 'edition_information': book.edition_information,
             'isbn': book.isbn, 'isbn13': book.isbn13, 'link': book.link}
            df = pd.DataFrame.from_dict(book_dict, orient='index')
            base_df = pd.concat([base_df, df], axis=1, join='outer', ignore_index=False)
            time.sleep(1)
        except (GoodreadsRequestException, TypeError):
            pass
    return base_df.transpose()

def goodreads_df_list(list_of_indices):
    base_df = pd.DataFrame()
    counter = 0
    for i in list_of_indices:
        counter += 1
        print(counter)
        try:
            book = gc.book(isbn = kaggle_isbns[i])
            book_dict = {'gid': book.gid, 'title': book.title, 'authors': book.authors, 'description': book.description, 'avg_rating': book.average_rating,
            'rating_dist': book.rating_dist, 'ratings_count': book.ratings_count, 'text_reviews_count': book.text_reviews_count,
             'num_pages': book.num_pages,
             'publication_date': book.publication_date, 'publisher': book.publisher, 'language_code': book.language_code, 'edition_information': book.edition_information,
             'isbn': book.isbn, 'isbn13': book.isbn13, 'link': book.link}
            df = pd.DataFrame.from_dict(book_dict, orient='index')
            base_df = pd.concat([base_df, df], axis=1, join='outer', ignore_index=False)
#             time.sleep(1)
        except (GoodreadsRequestException, TypeError):
            pass
    return base_df.transpose()

