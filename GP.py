def main():
    def sum():
        a=int(input(' Enter First term of GP(a): '))
        r=int(input(' Enter Common Ratio(r): '))
        n=int(input(' Enter Total Number of Terms(n): '))
        print(' Sum of',n,'Terms of GP is',)

    def term():
        a=float(input(' Enter First term of GP(a): '))
        r=float(input(' Enter Common Ratio(r): '))
        n=int(input(' Enter the Term needed to be found(n): '))
        print('',n,'th Term is',a*r**(n-1))

    def gen():
        a=int(input(' Enter First term of GP: '))
        r=int(input(' Enter Common Ratio(r): '))
        t=int(input(' Enter Total Number of Terms(n): '))
        print()
        for n in range(1,t+1):
            print('',n,'th Term is',a*((r**n)-1)//(r-1))
    print()
    print(' 1 -----> Sum Of GP')
    print(' 2 -----> Nth Term Of GP')
    print(' 3 -----> Generate GP')
    print()
    x=int(input(' Enter Task Code :'))
    if x==1 or x==2 or x==3:
        if x==1:
            sum()
        if x==2:
            term()
        if x==3:
            gen()
    else :
        print()
        print(' Invalid Task Code !')
main()
print()
print(' Do You Want to Exit ?')
print(' 1 -----> Yes !')
print(' 2 -----> No, Try Again !')
print()
y=int(input(' Enter Task Code :'))
if y==1 or y==2 :
    if y==1:
        exit
    if y==2:
        main()
else :
    print(' Wat Du U Mean ?')
    print(' Exiting Automatically !')
    exit
