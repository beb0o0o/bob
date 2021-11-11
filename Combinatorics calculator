import time
def EorO(num):
    if int(num)%2 != 0 :
        return "odd"
    elif int(num)%2 == 0:
        return "even"
def factorial(n):
    res = 1
    for i in range(int(n)+1):
        if int(i) != 0:
            res*=int(i)
    return res
frst=input("Do you want to make a new calculation (y/n)\n")
 
while frst == "y":
    q = input ("************************************************\nEnter calculation process you want to perform\n1-Factorial\n2-Double factorial\n3-Combination\n4-permutation\n************************************************\n")
    if int(q) == 1: 
        n = input("Enter the number\n")
        if n.isdigit():
            time.sleep(1)
            print(factorial(n))
            time.sleep(1)
        else:
            print("please enter an integer")

        frst=input("Do you want to make a new calculation (y/n)\n")
    elif int(q) == 2 : 
        n = input("Enter the number\n")
        def Dfactorial(n):
            res = 1
            typ = EorO(int(n))
            for i in range (int(n)+1):
                if i !=0 and EorO(i) == typ:
                    res*=i
            return res
        if n.isdigit():
            time.sleep(1)
            print(Dfactorial(n))
            time.sleep(1)
        else:
            print("please enter an integer")      


    elif int(q) == 3 :
        n = input("enter the value of n (Combination of n = nCr)")
        r = input("enter the value of r (Combination of n = nCr)")
        def combination():
            res = 0
            if (int(n)>int(r)):
                res = int(factorial(int(n)))/(factorial(r)*int(factorial(int(n)-int(r))))
            if (int(r)>int(n)):
                res = "r can't exceed n"
            return res
        if n.isdigit() and r.isdigit():
            time.sleep(1)
            print(combination())
            time.sleep(1)
   
        else:
            print("please enter an integer")      

    elif int(q) == 4:
        n = input("enter the value of n (permutation of n = nPr)")
        r = input("enter the value of r (permutation of n = nPr)")
        def permutation():
            res = 0
            if (int(n)>int(r)):
                res = int(factorial(int(n)))/int(factorial(int(n)-int(r)))
            if (int(r)>int(n)):
                res = "r can't exceed n"
            return res
        if n.isdigit() and r.isdigit():
            time.sleep(1)    
            print(permutation())
            time.sleep(1)
        else:
            print("please enter an integer")
