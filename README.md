## Book Recommender Systems

This project uses Natural Language Processing (topic modeling) and meta-data to recommend a fiction book that a user may like based on a book the user previously liked. 

Components of this repo:

### 0. Data gathering

I used three data sources for this project:

1. The New York Times Books API to gather fiction bestsellers from the past 9 years (**00_nyt_api_data**)
2. A Kaggle list of books from BookDepository.com to gather ISBNs of non-bestsellers (**01_kaggle_data_goodreads_api**)
3. The Goodreads.com API to gather text data and meta-data (review distribution, number of ratings) on the books (**02_goodreads_api_data**)

I then built a PostGreSQL database on an AWS machine to store and clean the data. The SQL schemas are in **03_sql_schemas**. 



### 1. Exploratory Data Analysis

In the **01_EDA** repo: data cleaning and preparation for topic modeling.



### 2. Modeling

1. Topic modeling on the GoodReads descriptions and identification of key topics (**00_topic_modeling**)
2. Recommender systems (**01_recommender**):
   1. "Content-only" recommender: uses only the doc-topic matrix to identify similar books based on topics only
   2. "Holistic" recommender: uses the doc-topic matrix and meta-data to identify books with similar popularity and topic makeup

### 3. Flask App

In the **03_Flask_App** repo: scripts needed to run a simple Flask app on a local machine that provides a book recommendation given user input



### 4. Results and Visualization

Placeholder for Youtube link

#  

