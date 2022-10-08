import sqlite3

def connect():
       conn = sqlite3.connect("student.db")
       cur = conn.cursor()

       cur.execute("CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY, registernumber integer ,department text ,name text, fname text, mname text, \
                     address text, mobno integer,email text, dob integer, gender text)")

       conn.commit()
       conn.close()

def insert(registernumber=' ', department=' ', name =' ', fname =' ', mname = ' ', address = ' ', mobno = ' ', email = ' ', dob = ' ', gender = ' '):
       conn = sqlite3.connect("student.db")
       cur = conn.cursor()

       cur.execute("INSERT INTO student VALUES (NULL,?,?,?,?,?,?,?,?,?,?)", (registernumber, department, name, fname,\
                                                                             mname, address, mobno, email, dob, gender))

       conn.commit()
       conn.close()
                                                                        

def view():
       conn = sqlite3.connect("student.db")
       cur = conn.cursor()

       cur.execute("SELECT * FROM student")
       rows = cur.fetchall()
       return rows

       conn.close()

def delete(id):
       conn = sqlite3.connect("student.db")
       cur = conn.cursor()

       cur.execute("DELETE FROM student WHERE id = ?", (id,))

       conn.commit()
       conn.close()

def update(id,registernumber=" ",department=" ", name = " ", fname = " ", mname = " ", address = " ", mobno = " ", email = " ", dob = " ", gender = " "):
       conn = sqlite3.connect("student.db")
       cur = conn.cursor()

       cur.execute("UPDATE student SET registernumber=? OR department=? OR name = ? OR fname = ? OR mname = ? OR address = ? OR mobno = ? OR email = ? OR dob = ? OR gender = ?", \
                   (registernumber,department,name, fname, mname, address , mobno, email, dob, gender))

       conn.commit()
       conn.close()

def search(registernumber=" ",department=" ",name = " ", fname = " ", mname = " ", address = " ", mobno = " ", email = " ", dob = " ", gender = " "):
       conn = sqlite3.connect("student.db")
       cur = conn.cursor()

       cur.execute("SELECT * FROM student WHERE registernumber= ? OR department= ? OR name = ? OR fname = ? OR mname = ? OR address = ? OR mobno = ? OR email = ? OR dob = ? \
                     OR gender = ?", (registernumber, department, name, fname, mname, address , mobno, email, dob, gender))
       rows = cur.fetchall()
       return rows
       
       conn.close()


                                                               
connect()
       
