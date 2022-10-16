"""

SQL database manager v. 2.0 - WORKS in SoloLearn!

Coded by mariosec1337 (c) 2022

The code creates an SQL database in memory, not using the file system (too big for SoloLearn). It then manages the database with pure SQL sample commands.

Thanks to Kirk Schafer, who inspired me to use sqlite3 ':memory:' for the code to work in SoloLearn! Now it can pass as 'educational purpose' ;)

As always, feel free to use it for your convenience :)

"""

import sqlite3

connect = sqlite3.connect(':memory:') #in-memory db

cursor = connect.cursor()

# establish a link to the db

people_data = {

 1:('Kuba S', 37),

 2:('Lara C', 24),

 3:('Tomy D', 23),

 4:('Nora B', 34),

 5:('Zack S', 44),

 6:('Rana S', 38),

 7:('Rose M', 32),

 8:('Ania L', 28)

}

# just a sample to refer to the original code v.1.0

# let's define some methods:

def create():

    # creates the table to manage

    sqlstr = 'CREATE TABLE PEOPLE(ID int AUTO_INCREMENT, Name varchar(255), Age int)'

    cursor.execute(sqlstr)

    connect.commit()

def insert(id, name, age):

    # method to add a new record

    sqlstr = 'INSERT INTO PEOPLE(ID, Name, Age) VALUES ("' + str(id) + '", "' + str(name) + '", ' + str(age) + ')'

    cursor.execute(sqlstr)

    connect.commit()

def filter(f):

    # method to filter records based on 'f' statement, see comments below

    sqlstr = 'SELECT * FROM PEOPLE WHERE ' + f + ' ORDER BY Name'

    print ('Database filtered by:', sqlstr, '\n')

    print ('ID', 'Name            ', '    Age')

    print ("-----------------------------")

    for row in cursor.execute(sqlstr):

        print(('{0:{width}}'.format(row[0], width=2)),

              ('{0:{width}}'.format(row[1], width=20)),

              ('{0:{width}}'.format(row[2], width=2)))

    print('-----------------------------\n')

def display_all():

    # method to list all records

    sqlstr = 'SELECT * FROM PEOPLE'

    print ('Showing the whole database')

    print ('ID', 'Name            ', '    Age')

    print ("-----------------------------")

    for row in cursor.execute(sqlstr):

        print(('{0:{width}}'.format(row[0], width=2)),

              ('{0:{width}}'.format(row[1], width=20)),

              ('{0:{width}}'.format(row[2], width=2)))

    print('-----------------------------\n')

# let's go!

create()

for k, v in people_data.items():

    insert(k, v[0], v[1])

filter('Age>25')            # lists all older than 25

print('* ' * 19, '\n')

filter('Name LIKE "%k%"')   # lists all with a 'k' in Name

print('* ' * 19, '\n')

display_all()

"""

display_all() should show the below:

ID Name                 Age

-----------------------------

 1 Kuba S               37

 2 Lara C               24

 3 Tomy D               23

 4 Nora B               34

 5 Zack S               44

 6 Rana S               38

 7 Rose M               32

 8 Ania L               28

-----------------------------

"""

# n = input("Enter name: ")

# a = input("Enter age: ")

# insert(9, n, a)

# print("New record added.")

# ^^^ unhash the above to be able to add a new record (Name, Age)

cursor.close()

# close the db
