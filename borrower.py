import psycopg2

conn = psycopg2.connect(
    # dbname="stepicdatabase",
    # user="stepicuser",
    # password="stepicpassword"
    dbname="postgres",
    user="myuser",
    password="mypassword"
)
cursor = conn.cursor()


create_borrower_query = """ 
        CREATE TABLE IF NOT EXISTS borrower (
                borrower_id SERIAL PRIMARY KEY,
                name_borrower VARCHAR(100),
                email VARCHAR(50)
        );
"""

cursor.execute(create_borrower_query)
conn.commit()


insert_borrower_query = """
    INSERT INTO borrower (borrower_id, name_borrower, email) VALUES (%s, %s, %s);
"""

borrowers = [
    (1, 'Baranov Pavel', 'baranov@test'),
    (2, 'Abramova Elena', 'abramova@test'),
    (3, 'Semenov Ivan', 'semenov@test')
]


cursor.executemany(insert_borrower_query, (borrowers))
conn.commit()

# Close the connection
cursor.close()
conn.close()