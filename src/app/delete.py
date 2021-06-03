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

# Function deleting rows data from table
def deleteRowByName(tablename, name):
    try:
        connection = psycopg2.connect(user=db_user,
                                    password=db_pass,
                                    host=db_host,
                                    port=db_port,
                                    database=db_name)
        cursor = connection.cursor()
        query_delete = "DELETE FROM " + table_name + " WHERE name = %s;"

        # executemany() to insert multiple rows
        result = cursor.execute(query_delete, (name,))
        print(result)
        connection.commit()
        print("Successfully deleted: ", cursor.rowcount, "records")

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
#records_to_delete = 'Test weapon'
print('Enter the name for delete:')
records_to_delete = input()

# Calling function for insert
deleteRowByName(table_name, records_to_delete)
