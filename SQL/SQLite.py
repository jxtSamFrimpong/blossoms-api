import sqlite3 as sql

conn = sql.connect('customers.db')

#cursor
csr = conn.cursor()

# creating a table
# csr.execute(
#     """CREATE TABLE customers (
#     first_name text,
#     last_name text,
#     email text
#     )"""
# )
#there are five sqlite datatypes
#null, integer, real, text, blob

#inserting ONE RECORD into table
# csr.execute(
#     "INSERT INTO customers VALUES('ofri', 'fm', 'ofrifm@600days.com')"
# )

# #todo insert MANY RECORDS into table
# many_customers_list = [
#     ('first', 'of_many', 'firstof@many'),
#     ('second', 'of_many', 'secondof@many'),
#     ('last', 'of_three', 'lastof@three')
# ]
# #actual execution
# csr.executemany("INSERT INTO customers VALUES(?,?,?)", many_customers_list)

# #todo fetching ALl stuff in our database
# csr.execute("SELECT * FROM customers")
# all = csr.fetchall()
# #also there is fetchone() aand fetchmany(number) methods
# print(all)

# #todo fetch items with PRIMARY_KEY included
# csr.execute("SELECT rowid, * FROM customers")
# all = csr.fetchall()
# for one in all:
#     print([i for i in one])

# #todo searching through our records
# search_term = "'odogofm@600days.com'"
# csr.execute(f"SELECT * FROM customers WHERE email = {search_term}")
# all = csr.fetchall()
# for one in all:
#      print([i for i in one])


##todo UPDATE record
# csr.execute("""UPDATE customers SET first_name = 'kojo'
#             WHERE rowid = 1
#  """)
# csr.execute("SELECT rowid, * FROM customers")
# all = csr.fetchall()
# for one in all:
#      print([i for i in one])

##todo DELETE a record
# csr.execute("DELETE FROM customers WHERE rowid = 4")

##todo ORDERing
# csr.execute("SELECT rowid, * FROM customers ORDER BY last_name DESC")
# all = csr.fetchall()
# for one in all:
#      print([i for i in one])

##todo searching using AND/OR
# csr.execute("SELECT rowid, * FROM customers WHERE last_name = 'fm' OR email LIKE '%m%' AND first_name LIKE 'o%' OR 'ko%'")
# all = csr.fetchall()
# for one in all:
#      print([i for i in one])

##todo LIMITS
# csr.execute("SELECT rowid, * FROM customers ORDER BY last_name DESC LIMIT 3")
# all = csr.fetchall()
# for one in all:
#      print([i for i in one])

##todo DROP an entire table
csr.execute("DROP TABLE customers")


#commiting to our database
conn.commit()


# csr.execute("SELECT rowid, * FROM customers")
# all = csr.fetchall()
# for one in all:
#      print([i for i in one])

#closing our connection
conn.close()