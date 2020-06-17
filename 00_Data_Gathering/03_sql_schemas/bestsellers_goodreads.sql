select sum("rank") as "sum_of_bestseller_rank", 
min("rank") as "best_nyt_rank", 
max(weeks_on_list) as "total_weeks_on_nyt_list", 
u_nyt_bestsellers.title, u_nyt_bestsellers.author, 
min(nytgoodreads.description) as "goodreads_description", nytgoodreads.avg_rating as "goodreads_avg_rating",
min(nytgoodreads.publication_date) as "earliest_publication", 
min(nytgoodreads.rating_dist) as "goodreads_rating_dist",
max(nytgoodreads.text_reviews_count) as "goodreads_reviews_count",
min(u_nyt_bestsellers.primary_isbn10) as "isbn_10", min(u_nyt_bestsellers.primary_isbn13) as "isbn_13",
case when sunday_review_link is not null then 1 else 0 end as "nyt_sunday_review",
case when book_review_link is not null then 1 else 0 end as "nyt_book_review",
case when first_chapter_link is not null then 1 else 0 end as "nyt_first_chapter_featured",
min("date") as "first_week_on_nyt_list",
max("date") as "last_week_on_nyt_list"
from u_nyt_bestsellers 
inner join nytgoodreads on text(nytgoodreads.isbn13) = u_nyt_bestsellers.primary_isbn13 
group by u_nyt_bestsellers.title, nytgoodreads.avg_rating,
u_nyt_bestsellers.author,
"nyt_sunday_review", "nyt_book_review", "nyt_first_chapter_featured"
order by total_weeks_on_nyt_list desc