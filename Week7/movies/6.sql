SELECT SUM(rating) / COUNT(*) FROM movies JOIN ratings ON movies.id = ratings.movie_id WHERE year = 2012;
