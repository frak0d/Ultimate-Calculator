print()
print(' <======---====*-*====---======>')
print('  Ultimate Calculator v0.9 Beta')

def main():
    print(' <======---====*-*====---======>')
    print()
    print(' What would you like to launch ?')
    print()
    print('    1  ---->   AP Calculator')
    print('    2  ---->   GP Calculator')
    print('    3  ---->  Area Calculator')
    print('    4  ----> Volume Calculator')
    print()
    print(' <======---====*-*====---======>')
    print()
    task=float(input(' Enter Task Code : '))
    if task==1 or task==2 or task==3 or task==4 :
        if task==1 :
            import AP.py
        if task==2 :
            import GP.py
        if task==3 :
            import AC.py
        if task==4 :
            import VC.py
    else :
        print()
        print(' <======---====*-*====---======>')
        print('       Input is not Valid !')
        print('  Please Run the Script Again !')
        print(' <======---====*-*====---======>')
        print()
    def exxit() :
        print(' Do You want to Exit or Try Again ?')
        print(' 1  ---->  Exit')
        print(' 2  ---->  Try Again')
        print()
        xit=float(input(">>"))
        if xit==1 or xit==2 :
            if xit==1 :
                exit
            if xit==2 :
                Volume()
        else :
            print()
            print(' What Du U MeeN ?')
            exxit()
main()
