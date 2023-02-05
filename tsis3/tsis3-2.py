def func1(movies):
    print("1'st function, enter name of the movie")
    st=input()
    for i in movies:
        if st==i["name"]:
            if i["imdb"] >=5.5:
                print("returned True")
                return True
            else:
                print("returned False")
                return False
    print("There isn't such movie.")

def func2(movies):
    lis=[]
    for i in movies:
        if i["imdb"] >=5.5:
            lis.append(i["name"])
    print(lis)

def func3(movies):
    print("Write down category you that you need")
    st=input()
    lis=[]
    for i in movies:
        if st==i["category"]:
            lis.append(i["name"])
    if len(lis)==0:
        print("There aren't any movie in that category")
    else:
        print(lis)
def func4(movies):
    a=0
    b=0
    for i in movies:
        a+=i["imdb"]
        b+=1
    print(a/b)

def func5(movies):
    a=0
    b=0
    print("Write the category you need")
    st=input()
    lis=[]
    for i in movies:
        if st==i["category"]:
            a+=i["imdb"]
            b+=1
            lis.append(i["imdb"])
    if len(lis)==0:
        print("there isn't such category")
    else:
        print(a/b)
movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
print("Select what function you need, write a number from 1 to 5 inclusive")
c=int(input())
if c==1:
    func1(movies)
elif c==2:
    func2(movies)
elif c==3:
    func3(movies)
elif c==4:
    func4(movies)
elif c==5:
    func5(movies)
else:
    print("There isn't such function, would ou mind trying again?")
