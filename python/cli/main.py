from tinydb import TinyDB, Query

db = TinyDB('todo.json')
q = Query()
row = 0

print("Welcome to TODO app\n")

while True:
    work = str(input("[A]dd , [C]heck , [L]ist , [E]xit >>> "))

    if work.lower() == "a" :
        print("\nNow add your job as this template:")
        print("Name Text")
        
        add = str(input("\nOk, Go on >>> ")).split(" ")
        
        row = row + 1

        db.insert({"row": row, "title": add[0], "description": add [1], "status": "undone"})

        print("Done !")

    elif work.lower() == "c" :
        check = int(input("\nWrite row of your job >>> "))


        print(db.search(q.row == check))
        db.remove(q.row == check)


    elif work.lower() == "l" :
        for item in db.all():
            print(item)

    elif work.lower() == "e" :
        print("Ok, Bye !")
        quit()

    else :
        continue