import configparser
import psycopg2
import csv

config = configparser.ConfigParser()
config.sections()

config.read('database.ini')
conf = config['1']

conn = psycopg2.connect(
    host = conf['host'],
    database = conf['database'],
    user = conf['user'],
    password = conf['password']
)

cur = conn.cursor()
cur.execute("SELECT EXISTS(SELECT * FROM information_schema.tables WHERE table_name='phonebook')")
table_exists = cur.fetchone()[0]
if not table_exists:
    phonebook_creation = '''CREATE TABLE phonebook(
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        phone VARCHAR(5) NUT NULL
        );'''
    cur.execute(phonebook_creation)
    conn.commit()

def implement_1():
    print('''1 for input from terminal.
2. for input from csv file''')
    num=int(input())
    if num==1:
        print('please input name and phone number')
        n_value = input('Enter a name: ')
        p_value = input("Enter a number with 5 characters: ")
        while len(p_value) != 5:
            p_value = input("Value must be 5 characters. Please try again: ")
        cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (n_value, p_value))
        conn.commit()
    elif num == 2:
        with open('phone.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                name = row[0]
                phone = row[1]
            cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
            conn.commit()
def update():
    print('what exactly do you want to change? 1.Name, 2. phone')
    num = int(input())
    if num == 1:
        n = int(input('please write the id of a person you want to update: '))
        n_name = input('please write the new name for this person: ')
        cur.execute("UPDATE phonebook SET name = %s WHERE id = %s", (n_name, n))
    elif num == 2:
        n = int(input('please write the id of a person you want to update: '))
        n_phone = input('please write the new number for this person: ')
        cur.execute("UPDATE phonebook SET phone = %s WHERE id = %s", (n_phone, n))
    else:
        print('try again some other time')
    conn.commit()

def search():
    print('how exactly do you want to search? 1. first letter of name. 2. first digit of number')
    n = int(input())
    if n == 1:
        n_name = input('input letter : ')      
        while len(n_name) != 1:
            n_name =  input('i said one letter: ')
        else:
            cur.execute("SELECT * FROM phonebook WHERE name LIKE '{}'".format(n_name+'%'))
            rows = cur.fetchall()
            for row in rows:
                print(row[1], row[2])
    if n == 2:
        n_phone = input('input number : ')      
        while len(n_phone) != 1:
            n_phone =  input('i said one number: ')
        else:
            cur.execute("SELECT * FROM phonebook WHERE phone LIKE '{}%'".format(n_phone))
            rows = cur.fetchall()
            for row in rows:
                print(row[1], row[2])
                
def delete_entry():
    row_id = input("Enter the id of the person to delete from phonebook: ")

    cur.execute("DELETE FROM phonebook WHERE id = %s", (row_id,))

    conn.commit()

    print("person deleted successfully.")
    
    
print('''Hello, it is phonebook, choose one of the following functions:
      1.input info into phonebook
      2.update info in phonebook
      3.search info from phonebook
      4.delete person from phonebook
      5.see the phonebook''')
num = int(input())
if num == 1:
    implement_1()
elif num == 2:
    update()
elif num == 3:
    search()
elif num == 4:
    delete_entry()
elif num == 5:
    cur.execute("SELECT * FROM phonebook")

    rows = cur.fetchall()
    for row in rows:
        print(row)

else:
    print('try again other time')
