import psycopg2

# DB Connection data
db_user = 'username'
db_pass = 'secret'
db_host = 'localhost'
db_port = '5432'
db_name = 'genshin'

table_name = 'sword'

try:
    connection = psycopg2.connect(user=db_user,
                                  password=db_pass,
                                  host=db_host,
                                  port=db_port,
                                  database=db_name)
    cursor = connection.cursor()
    postgreSQL_select_Query = "select * from " + table_name

    print("Table: ", table_name)

    cursor.execute(postgreSQL_select_Query)
    print("Selecting rows from mobile table using cursor.fetchall")
    mobile_records = cursor.fetchall()

    print("Print each row and it's columns values")
    for row in mobile_records:
        print("name = ", row[0])
        print("rarity = ", row[1])
        print("atk  = ", row[2])
        print("substat  = ", row[3], "\n")

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
