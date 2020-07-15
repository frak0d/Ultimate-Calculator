def main():
    def sum():
        a=int(input(' Enter First term of AP: '))
        d=int(input(' Enter Common Difference: '))
        n=int(input(' Enter Total Number of Terms: '))
        print(' Sum of',n,'Terms of AP is',(n/2)*((2*a)+(n-1)*d))

    def term():
        a=float(input(' Enter First term of AP: '))
        d=float(input(' Enter Common Difference: '))
        n=int(input(' Enter the Term needed to be found(n): '))
        print('',n,'th Term is',a+(n-1)*d)

    def gen():
        a=int(input(' Enter First term of AP: '))
        d=int(input(' Enter Common Difference: '))
        t=int(input(' Enter Total Number of Terms: '))
        print()
        for n in range(1,t+1):
            print('',n,'th Term is',a+(n-1)*d)
    print()
    print(' 1 -----> Sum Of AP')
    print(' 2 -----> Nth Term Of AP')
    print(' 3 -----> Generate AP')
    x=int(input(' Enter Task Code :'))
    if x==1 or x==2 or x==3:
        if x==1:
            sum()
        if x==2:
            term()
        if x==3:
            gen()
    else :
        print(' Invalid Task Code !')
main()
print()
print(' Do You Want to Exit ?')
print(' 1 -----> Yes !')
print(' 2 -----> No, Try Again !') 
y=int(input(' Enter Task Code :'))
if y==1 or y==2 :
    if y==1:
        exit
    if y==2:
        main()
else :
    print(' Wat Du U Mean ?')
    print(' Exiting Automatically !')
