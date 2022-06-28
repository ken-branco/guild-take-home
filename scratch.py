import re
import json
import sqlite3
import pandas as pd

conn = sqlite3.connect('./data/movies.db')
movie_data = pd.read_csv('./data/the-movies-dataset/movies_metadata.csv')
# ratings_data = pd.read_csv('./data/the-movies-dataset/ratings.csv')


# extract only needed columns
movie_meta_genre = movie_data.filter(items=['id', 'genres'], axis=1)
genre_movies_set = set()
# for row in movie_meta_genre.items():
for i in range(3400):
    # if row[1] == '[]' or row[0] in [1147,
    #                                 2312,
    #                                 2540,
    #                                 3456,
    #                                 3835]:
    #     continue
    row = movie_meta_genre.loc(axis=0)[i]
    movie_id = row.id
    row_movie_genres = row.genres
    if row_movie_genres == '[]' or i in [1147, 2222, 2312, 2540, 3456, 3835]:
        continue
    row_movie_genres = \
        row_movie_genres.replace("[", "").replace("]", "").replace("'", '"').replace("},", '}|')
    row_move_genres = row_movie_genres.split('|')
    for movie_genres in row_move_genres:
        movie_genres = re.sub('([A-Za-z])(")([A-Za-z])', '\\1\\\\\\2\\3', movie_genres)
        movie_genres = re.sub('([A-Za-z])(") ([A-Za-z])', '\\1\\\\\\2\\3', movie_genres)
        movie_genres = re.sub('"([A-Za-z]+)(")(")(,)', '\\1\\2\\4', movie_genres)
        movie_genres = re.sub(' ([A-Za-z])(")(.)', '\\1\\\\\\2\\3', movie_genres)
        movie_genres = re.sub('(")([0-9]+)(")', '\\\\\\1\\2\\3', movie_genres)
        # production_companies = re.sub('(\\\\)(")', '\\2', production_companies)
        movie_genre = json.loads(movie_genres)
        genre_movies_set.add((movie_id, movie_genre['id']))

print('foo')
# drop unneeded columns form dataframe
# insert_ratings = ratings_small_data.drop(labels=['userId', 'timestamp'], axis=1)

# write dataframe to table
# insert_ratings.to_sql('ratings', conn, if_exists='replace', index=False)

# verify write with small read
# pd.read_sql('select * from movie_meta limit 5', conn)

conn.commit()
conn.close()

print('foo')
