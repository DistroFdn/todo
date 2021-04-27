row = 0
tasks = {}

print("Welcome to TODO app\n")

while True:
    work = str(input("[A]dd , [C]heck , [L]ist , [E]xit >>> "))

    if work.lower() == "a" :
        print("\nNow add your job as this template:")
        print("Name Text")
        
        add = str(input("\nOk, Go on >>> ")).split(" ")
        
        row = row + 1

        try:
            tasks.update({ row : [add[0] , add[1] , "ny"]})
        except IndexError:
            print('enter in proper format')
            continue

        print("Done !")

    elif work.lower() == "c" :
        check = int(input("\nWrite row of your job >>> "))

        tasks.pop(check)

        print(tasks)

    elif work.lower() == "l" :
        print(tasks)

    elif work.lower() == "e" :
        print("Ok, Bye !")
        quit()

    else :
        continue
