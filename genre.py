import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="myuser",
    password="mypassword"
)
cursor = conn.cursor()


create_genre_query = """
        CREATE TABLE IF NOT EXISTS genre (
                genre_id SERIAL PRIMARY KEY,
                name_genre VARCHAR(100),
        );
"""
cursor.execute(create_genre_query)
conn.commit()


insert_genres_query = """
    INSERT INTO genre (genre_id, name_genre) VALUES (%s, %s);
"""

insert_genres_query = """
    INSERT INTO genre (genre_id, name_genre) VALUES (%s, %s);
"""

genres = [
    (1, 'Romantic Fiction'),
    (2, 'Health & Lifestyle'),
    (3, 'Adventure'),
]
cursor.executemany(insert_genres_query, (genres))
conn.commit()

# Close the connection
cursor.close()
conn.close()