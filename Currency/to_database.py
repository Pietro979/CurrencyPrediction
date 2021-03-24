from sqlalchemy import create_engine
import string
import psycopg2

db_string = "postgres://postgres:postgres1@localhost:5432/dvdrental"
db = create_engine(db_string)
result_set = db.execute("SELECT city FROM city")

for r in result_set:
    print(r)

# Ile kategorii filmów mamy w wypożyczalni

number_of_categories = db.execute("SELECT MAX(city_id) FROM city")

for cat in number_of_categories:
    print(cat)

# Kategorie w kolejnosci alfabetycznej

categories_alphabet = db.execute("SELECT name from category ORDER BY name DESC")
for cat in categories_alphabet:
    print(cat)

# Najstarszy film
oldest_movie = db.execute("SELECT title, release_year FROM film order by release_year DESC LIMIT 1")
for cat in oldest_movie:
    print(cat)