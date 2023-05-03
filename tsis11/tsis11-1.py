import configparser
import psycopg2

config = configparser.ConfigParser()
config.sections()

config.read(r'C:\Users\ilias\OneDrive\Рабочий стол\hello\tsis10\database.ini')
conf = config['1']

conn = psycopg2.connect(
    host = conf['host'],
    database = conf['database'],
    user = conf['user'],
    password = conf['password']
)

cur = conn.cursor()

def man_user_add_1():
    k = int(input("How many new users: "))
    add_names, add_numbers = [], []

    print('''Okay, write your:
 name    phone''')

    for i in range(0, k):
        l = input().split()
        add_names.append(l[0])
        add_numbers.append(l[1])


    cur.execute("SELECT add_many_users(%s, %s)", (add_names, add_numbers))
    conn.commit()
    result = cur.fetchone()[0]
    if result != None:
        print("Incorrect phone numbers: ", result)
        
        
def find_all_user_2():
    k = input("Who do you want to find?")
    cur.execute("SELECT * FROM return_all_same_user(%s)", (k, ))
    result = cur.fetchall()
    print(result)

def ad_up_3():
    
    print('''Write your user:
name   phone''' )
    arr_user = input().split()
    cur = conn.cursor()


    cur.execute("CALL add_or_update_user(%s, %s)", (arr_user[0], arr_user[1]))

def num_users_4():
    k = int(input("Start row:"))
    l = int(input("Number of row:"))
    
    cur.execute("SELECT * FROM get_users_between_rows(%s, %s)", (k, l))
    result = cur.fetchall()
    print(result)

def del_user_5():
    k = input("Who do you want to delete? ")

    cur.execute("CALL delete_user(%s)", (k, ))

print('''Hello, what you need today:
      1. add many users
      2. find all users
      3. add or update users
      4. see the number of users
      5. delete user ''')
num = int(input())
if num == 1:
    man_user_add_1()
elif num == 2:
    find_all_user_2()
elif num == 3:
    ad_up_3()
elif num == 4:
    num_users_4()
elif num == 5:
    del_user_5()
else:
    print('no such function, try again')
conn.commit() 
cur.close()
conn.close()