import sqlite3
c = sqlite3.connect('test.db')
cursor = c.cursor()

user_name = input("Enter your name: ")
user_age = input("Enter your age: ")
user_age = int(user_age)

# cursor.execute('CREATE TABLE test(name next, age integer)')

cursor.execute(f"INSERT INTO test VALUES('{user_name}', {user_age})")
cursor.execute("SELECT * FROM test")
out = cursor.fetchall()

print(out)

c.commit()

'''
SQL injection example

Enter your name: elice', 20)--
Enter your age: 122
[('sql injection example 01', 10), ('sql injection example 02', 20), ('hello', 129), ('elice', 20)]
'''