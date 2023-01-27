import csv
import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="athiva@",
    database='Demo'
)
cursor = conn.cursor()
# Open the CSV file
with open("C:/Users/vaish/OneDrive/Desktop/incert.csv", mode='r', encoding="utf8", errors='replace') as file:
    # Create a CSV reader object
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(row)
    # Insert the data into the database
        cursor.execute(
            "INSERT INTO america (first_name, last_name, company_name,address ,city,county,state,zip,phone1,phone2,email,web) VALUES (%s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",row)
    # for i in range(0, 1):
    #     cursor.execute('DELETE FROM america where id = 0 order by id ')

# Commit the
# changes and close the connection
conn.commit()
cursor.close()
conn.close()





