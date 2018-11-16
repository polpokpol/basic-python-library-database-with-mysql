import mysql.connector


#THE PART .execute IS VERY SENSITIVE EDIT AT YOUR OWN RISK. However it is easy to add fields on the table
#	NOTE: I DID NOT ADD A DROP TABLE FEATURE.
#THIS WILL ONLY WORK IF YOU HAVE MYSQL OTHERWISE USE sqlite3 IN PYTHON


# conn = mysql.connector.connect(user="root",password='password',host='localhost',database='library',port='3306')
# cur = conn.cursor()
# cur.execute("CREATE TABLE IF NOT EXISTS store (item VARCHAR(25), quantity INT, price REAL);")
# conn.commit()

def create_table():
	conn = mysql.connector.connect(user="root",password='password',host='localhost',database='library',port='3306')
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS store (id INT PRIMARY KEY AUTO_INCREMENT, title VARCHAR(50), author VARCHAR(50), category VARCHAR(20), isbn INT);")
	conn.commit()
	conn.close()


def insert(title, author, category, isbn):
	conn = mysql.connector.connect(user="root",password='roskimoski',host='localhost',database='library',port='3306')
	cur = conn.cursor()
	cur.execute("INSERT INTO store (title, author, category, isbn) VALUES (%s, %s, %s, %s)", (title, author, category, isbn))
	conn.commit()
	conn.close()

def view():
	conn = mysql.connector.connect(user="root",password='roskimoski',host='localhost',database='library',port='3306')
	cur = conn.cursor()
	cur.execute("SELECT * FROM store;")
	rows = cur.fetchall()
	conn.close()
	print(rows)
	return rows

def search(title = "", author = "", category = "", isbn = ""):
	conn = mysql.connector.connect(user="root",password='roskimoski',host='localhost',database='library',port='3306')
	cur = conn.cursor()
	cur.execute("SELECT * FROM store WHERE title = %s OR author = %s OR category = %s OR isbn = %s", (title, author, category, isbn))
	rows = cur.fetchall()
	conn.close()
	# print(rows)
	return rows

def delete(id):
	conn = mysql.connector.connect(user="root",password='roskimoski',host='localhost',database='library',port='3306')
	cur = conn.cursor()
	cur.execute("DELETE FROM store WHERE id = %s", (id,))
	conn.commit()
	conn.close()

def update(id, title, author, category, isbn):
	conn = mysql.connector.connect(user="root",password='roskimoski',host='localhost',database='library',port='3306')
	cur = conn.cursor()
	cur.execute(("UPDATE store SET title = %s, author = %s, category = %s, isbn = %s WHERE id = %s"), (title, author, category, isbn, id))
	conn.commit()
	conn.close()

create_table()