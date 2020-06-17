import pandas as pd
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform
from sklearn import preprocessing

books = pd.read_pickle('/Users/annabradleywebb/PycharmProjects/Project5/Modeling/00_topic_modeling/all_data.pkl')

smaller_books = books.drop(['link','word_tokenized_description','lemmatized_description', 'edition_information', 'description', 'publisher',
                   '1_generic', '2_spanish' ,'12_disregard', '23_award_winning_authors', '13_disregard', '30_disregard'], axis=1)

de_duped_books = smaller_books.drop_duplicates('title')

de_duped_books.isbn13 = de_duped_books.isbn13.astype(int)

scaler = preprocessing.StandardScaler()

book_topics = smaller_books[['isbn13','3_love_stories', '4_big_life_changes', '5_strong_characters',
       '6_world_war_II', '7_family_sagas_intergenerational', '8_time_travel',
       '9_erotic_vampires', '10_women', '11_murder_crime_mystery',
       '14_places_journeys', '15_holidays_christmas_warmth', '16_world_global',
       '17_generic', '18_family_parents', '19_men_power',
       '20_business_choices', '21_parents_young_children', '22_historical_USA',
        '24_science_fiction', '25_places_journeys',
       '26_firsts', '27_friendship', '28_coming_home',
       '29_secret_discoveries']]
pairwise = pd.DataFrame(
    squareform(pdist(de_duped_books[['3_love_stories', '4_big_life_changes', '5_strong_characters',
       '6_world_war_II', '7_family_sagas_intergenerational', '8_time_travel',
       '9_erotic_vampires', '10_women', '11_murder_crime_mystery',
       '14_places_journeys', '15_holidays_christmas_warmth', '16_world_global',
       '17_generic', '18_family_parents', '19_men_power',
       '20_business_choices', '21_parents_young_children', '22_historical_USA',
        '24_science_fiction', '25_places_journeys',
       '26_firsts', '27_friendship', '28_coming_home',
       '29_secret_discoveries']])),
    columns = de_duped_books['isbn13'],
    index = de_duped_books['isbn13']
)
column_list = ['3_love_stories', '4_big_life_changes',
               '5_strong_characters', '6_world_war_II',
               '7_family_sagas_intergenerational', '8_time_travel',
               '9_erotic_vampires', '10_women',
               '11_murder_crime_mystery','14_places_journeys',
               '15_holidays_christmas_warmth', '16_world_global',
               '18_family_parents', '19_men_power',
               '20_business_choices', '21_parents_young_children',
               '22_historical_USA',
               '24_science_fiction', '25_places_journeys',
               '26_firsts', '27_friendship',
               '28_coming_home','29_secret_discoveries']

topic_list = ['Love stories', 'Big life changes',
              'Strong characters', 'World War II',
              'Family sagas/intergenerational','Travel',
              'Erotic/paranormal/vampires', 'Women',
              'Murder/crime mysteries', 'Places and journeys',
             'Holidays and/or Christmas', 'The world',
              'Family and parents', 'Men',
              'Business and choices', 'Parents and young children',
             'Historical fiction - USA',
              'Science fiction', 'Travel and journeys',
             'Firsts', 'Friendship',
              'Coming home', 'Secrets and discoveries']

scaled_data = de_duped_books[['isbn13','avg_rating', 'ratings_count',
       'text_reviews_count', 'num_pages', 'bestseller',
       '5-star', '4-star', '3-star', '2-star', '1-star', 'total',
       '3_love_stories', '4_big_life_changes', '5_strong_characters',
       '6_world_war_II', '7_family_sagas_intergenerational', '8_time_travel',
       '9_erotic_vampires', '10_women', '11_murder_crime_mystery',
       '14_places_journeys', '15_holidays_christmas_warmth', '16_world_global',
       '17_generic', '18_family_parents', '19_men_power',
       '20_business_choices', '21_parents_young_children', '22_historical_USA',
        '24_science_fiction', '25_places_journeys',
       '26_firsts', '27_friendship', '28_coming_home',
       '29_secret_discoveries']]

scaled_data.set_index('isbn13')

scaled_df = scaler.fit_transform(scaled_data)

scaled_df = pd.DataFrame(scaled_df, columns=scaled_data.columns, index=scaled_data.isbn13)

scaled_df = scaled_df.drop(['isbn13'], axis=1)
scaled_df = scaled_df.fillna(0)

pairwise_2 = pd.DataFrame(
    squareform(pdist(scaled_df)),
    columns = de_duped_books['isbn13'],
    index = de_duped_books['isbn13']
)


def most_similar(isbn):
    topic_dict = {}
    new_topic_dict = {}
    user_book = de_duped_books[de_duped_books['isbn13']==isbn]
    for i in range(len(column_list)):
        topic_dict[topic_list[i]] = list(user_book[column_list[i]])
    original_topics = ', '.join(list({k: v for k, v in sorted(topic_dict.items(), key=lambda item: item[1], reverse=True)})[0:3])
    original_book = pairwise[pairwise.index==isbn]
    original_book = original_book.drop(isbn, axis=1)
    min_index_1 = original_book.idxmin(axis=1)
    closest_isbn = list(min_index_1)[0]
    new_book = de_duped_books[de_duped_books['isbn13']==closest_isbn]
    for i in range(len(column_list)):
        new_topic_dict[topic_list[i]] = list(new_book[column_list[i]])
    new_book = ''.join(list(de_duped_books[de_duped_books['isbn13']==closest_isbn]['title'])[0].title())
    new_author = ''.join((list(de_duped_books[de_duped_books['isbn13']==closest_isbn]['authors'])[0]))
    new_topics = ', '.join(list({k: v for k, v in sorted(new_topic_dict.items(), key=lambda item: item[1], reverse=True)})[0:3])
    return "Main topics in the book you like: {} You may also like {} by {}. Its main topics are {}.".format(original_topics, new_book, new_author, new_topics)

def most_similar_meta(isbn):
    user_book = list(de_duped_books[de_duped_books['isbn13']==isbn]['title'])[0].title()
    user_author = list(de_duped_books[de_duped_books['isbn13']==isbn]['authors'])[0]
    original_book = pairwise_2[pairwise_2.index==isbn]
    original_book = original_book.drop(isbn, axis=1)
    min_index_1 = original_book.idxmin(axis=1)
    closest_isbn = list(min_index_1)[0]
    new_book = list(de_duped_books[de_duped_books['isbn13']==closest_isbn]['title'])[0].title()
    new_author = list(de_duped_books[de_duped_books['isbn13']==closest_isbn]['authors'])[0]
    return "You entered: {} by {}. You might also like {} by {}.".format(user_book, user_author, new_book, new_author)