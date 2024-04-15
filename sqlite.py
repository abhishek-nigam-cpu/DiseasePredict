import sqlite3

conn = sqlite3.connect('disPred.db')
print("Opened database successfully")
cur=conn.cursor()
# conn.execute('''CREATE TABLE users
#          (ID TEXT PRIMARY KEY     NOT NULL,
#          NAME           TEXT    NOT NULL,
#          PASSWORD       CHAR(20)     NOT NULL);''')
#cur.execute('INSERT INTO users (ID,NAME,PASSWORD) VALUES (?,?,?)',("abhishekch1999@gmail.com","Abhishek Chaurasia","123456789") )
#cur.execute('INSERT INTO users (ID,NAME,PASSWORD) VALUES (?,?,?)',("abc@gmail.com","Abhishek Nigam","12345") )
#conn.commit()
email="abhishekch1999@gmail.com"
# cur.execute("select * from users)
cur.execute("select * from users")
#cur.execute("delete from users")
#conn.commit()
res=cur.fetchall()
print(res)
conn.close()