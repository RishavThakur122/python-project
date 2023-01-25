import sqlite3
mybooks=sqlite3.connect('books.db')
curbooks=mybooks.cursor()

total=0
while True:
    mybookname=input("give the name of the book ")
    sql="SELECT * from BOOKS WHERE NAME='"+mybookname+"'"
    curbooks=mybooks.cursor()
    curbooks.execute(sql)
    rec=curbooks.fetchone()
    if rec!=None:
        print (rec)
        pr=rec[2]
        qty=int(input("give number of books : "))
        cost=pr*qty
        total=total+cost
    else:
        print("title not found")
    choice=input("add more books[Y/N]:")
    if choice=='N':break
print("Total cost of purchased Books",total)
mybooks.close()
        

