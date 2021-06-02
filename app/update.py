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

# Function updating rarity of row by name
def updateRowRarity(tablename, weaponname, weaponrarity):
    try:
        connection = psycopg2.connect(user=db_user,
                                    password=db_pass,
                                    host=db_host,
                                    port=db_port,
                                    database=db_name)
        cursor = connection.cursor()

        # Show row before update
        print("Table Before updating record ")
        sql_select_query = "SELECT * FROM " + tablename + " WHERE " + name + " = %s"
        cursor.execute(sql_select_query, (weaponname,))
        record = cursor.fetchone()
        print(record)

        query_update = "UPDATE " + table_name + " SET " + rarity + " = %s WHERE " + name + " = %s;"

        # Update record
        result = cursor.execute(query_update, (weaponrarity, weaponname))
        print(result)

        connection.commit()
        print("Successfully updated: ", cursor.rowcount, "records")

        # Show row after update
        print("Table After updating record ")
        cursor.execute(sql_select_query, (weaponname,))
        record = cursor.fetchone()
        print(record)

    except (Exception, psycopg2.Error) as error:
        print("Error while updating data from PostgreSQL", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

# Table for insert
table_name = 'sword'
# New rows data
records_to_update = 'Super Weapon'
rarity_to_update = 4

# Calling function for insert
updateRowRarity(table_name, records_to_update, rarity_to_update)