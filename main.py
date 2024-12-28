import pymongo

client=pymongo.MongoClient("mongodb+srv://qwexykk:123123a@cluster0.j2zxh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

database=client["test"]

collection=database["cats"]

catlist=[
    {"name": "barsik", "age": 3, "features": ['ходить в капці', 'дає себе гладити', 'рудий', 'смердючий']},
    {'name': 'Liza', 'age': 4, 'features': ['ходить в лоток', 'дає себе гладити', 'білий']},
    {'name': 'Boris', 'age': 12, 'features': ['ходить в лоток', 'не дає себе гладити', 'сірий']},
    {'name': 'Murzik', 'age': 1, 'features': ['ходить в лоток', 'дає себе гладити', 'чорний']},
    {'name': 'Dariy', 'age': 10, 'features': ['ходить в лоток', 'не дає себе гладити', 'сірий']},
    {'name': 'Lama', 'age': 2, 'features': ['ходить в лоток', 'не дає себе гладити', 'сірий']}
]

def create():
    collection.insert_many(catlist)

    for cat in collection.find():
        print(cat)



def all():
    if collection.find_one() is None:
        print("В колекції записи відсутні")
    else:
        for cat in collection.find():
            print(cat)

def findone():
    name=str(input("Введіть ім'я кота: "))
    
    if collection.find_one({"name": name}) is None:
        print("Кота з таким ім'ям не було знайдено")
    else: 
        print(collection.find_one({"name": name}))


def updateage():
    name=str(input("Введіть ім'я кота: "))
    age=int(input("Введіть вік кота: "))

    if collection.find_one({"name": name}) is None:
        print("Кота з таким ім'ям не було знайдено")
    else: 
        collection.update_one({"name": name}, {"$set" : {"age": age}})
        print(collection.find_one({"name": name}))

def addfeature():
    name=str(input("Введіть ім'я кота: "))
    feature=str(input("Введіть нову властивість кота: "))
    
    if collection.find_one({"name": name}) is None:
        print("Кота з таким ім'ям не було знайдено")
    else:
        collection.update_one({"name": name}, {"$addToSet": {"features":feature}})
        print(collection.find_one({"name":name}))

def delrecord():
    name=str(input("Введіть ім'я кота: "))

    if collection.find_one({"name": name}) is None:
        print("Кота з таким ім'ям не було знайдено")
    else:
        collection.delete_one({"name": name})
        for el in collection.find():
            print(el)

def delall():
    collection.delete_many({})
    print("Всі записи в колекції були видалені")


updateage()