import sqlite3
conn = sqlite3.connect("MyDB.db")
print (type(conn))
cur = conn.cursor()
cur.execute("insert into Days (DoY, DoW, Holiday, Weather) values (1, 'Thurs', 1, 'Snow')")
conn.commit()
