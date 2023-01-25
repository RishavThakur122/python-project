import sqlite3
mybooks=sqlite3.connect('books.db')
curbooks=mybooks.cursor()
curbooks.execute('''CREATE TABLE BOOKS(
NUMBER INTEGER,
NAME STRING,
PRICE INTEGER 










);'''
)
mybooks.close()
