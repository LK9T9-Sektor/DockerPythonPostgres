import psycopg2

# DB Connection data
db_user = 'username'
db_pass = 'secret'
db_host = 'localhost'
db_port = '5432'
db_name = 'genshin'

# Column names
name = 'name'
rarity = 'rarity'
atk = 'atk'
substat = 'substat'

# Function insert rows data into table
def insertIntoTable(tablename, records):
    try:
        connection = psycopg2.connect(user=db_user,
                                    password=db_pass,
                                    host=db_host,
                                    port=db_port,
                                    database=db_name)
        cursor = connection.cursor()
        query_insert = "INSERT INTO " + table_name + "(" + name + "," + rarity + "," + atk + "," + substat + ") VALUES (%s, %s, %s, %s)"
        #query_insert = "INSERT INTO sword (name, rarity, atk, substat) VALUES (%s, %s, %s, %s)"

        # executemany() to insert multiple rows
        result = cursor.executemany(query_insert, records)
        print(result)
        connection.commit()
        print("Successfully inserted: ", cursor.rowcount, "records")

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

# Table for insert
table_name = 'sword'
# New rows data
records_to_insert = [('Test weapon', 1, 10, 'Atk%'), ('Super Weapon', 5, 100, 'Oneshoot chance%')]

# Calling function for insert
insertIntoTable(table_name, records_to_insert)