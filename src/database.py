import sqlite3



##res = cur.execute("SELECT * FROM employees")
##print(res.fetchall())

def connect():
    con = sqlite3.connect(r"C:\Users\Amir\Desktop\AskMyDB\company.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    return con, cur
