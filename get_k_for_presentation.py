from sys import argv

f = open(argv[1])

while True:

    magic_string=next(f)

    if magic_string=="firep\n":
        next(f)
        next(f)
    elif magic_string=="scc2020\n":
        next(f)
    else:
        print("Wrong data format")
        print("Magic string",magic_string)
        exit(1)

    size_string=next(f).split()
    no_simplices =int(size_string[0])
    no_stuff=int(size_string[1])
    
    pairs=[]

    for _ in range(no_simplices):
        numbers = next(f).split()
        new_x=numbers[0]
        new_y=numbers[1]
        pairs.append(str(new_x)+" "+str(new_y))

    pairs.sort()

    numbers = pairs[0].split()
    last_x=numbers[0]
    last_y=numbers[1]

    max_k=1
    curr_k=1

    grade_of_max_k=""

    for i in range(1,no_simplices):
        numbers = pairs[i].split()
        new_x=numbers[0]
        new_y=numbers[1]
        if(new_x<last_x):
            print(i,new_x,last_x)
            assert(new_x>last_x or (new_x==last_x and new_y>=last_y))
        if last_x==new_x and last_y==new_y:
            curr_k+=1
            if curr_k>max_k:
                max_k=curr_k
                grade_of_max_k=pairs[i]
        else:
            last_x=new_x
            last_y=new_y
            curr_k=1
    for _ in range(no_stuff):
        _ = next(f)
        
    print("Maximal k is",max_k)
    print("At grade",grade_of_max_k)

    break
f.close()



