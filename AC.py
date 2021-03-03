print(' <======---====*-*====---======>')
print('      Area Calculator v1.1')

def Cube() :
	print()
	print(' <======---====*-*====---======>')
	print()
	s=float(input(' Enter Side of Cube in Centimeters : '))
	vcm=round(s**2,2)
	vm=round(vcm/1000,3)
	print()
	print(' <======---====*-*====---======>')
	print(' Volume of Cube is',vcm,'cm³ or',vm,'m³')
	print(' <======---====*-*====---======>')
	print()

def Cuboid():
	print()
	print(' <======---====*-*====---======>')
	print()
	l=float(input(' Enter Length of Cuboid in Centimeters : '))
	b=float(input(' Enter Width of Cuboid in Centimeters : '))
	h=float(input(' Enter Height of Cuboid in Centimeters : '))
	vcm=round(l*b*h,2)
	vm=round(vcm/10000,3)
	print()
	print(' <======---====*-*====---======>')
	print(' Surface Area of Cuboid is',vcm,'cm³ or',vm,'m³')
	print(' <======---====*-*====---======>')
	print()

def Sphere() :
	print()
	print(' <======---====*-*====---======>')
	print()
	r=float(input(' Enter Radius of Sphere in Centimeters : '))
	vcm=round((4/3)*(22/7)*(r**3),2)
	vm=round(vcm/1000,3)
	print()
	print(' <======---====*-*====---======>')
	print(' Area of Sphere is',vcm,'cm³ or',vm,'m³')
	print(' <======---====*-*====---======>')
	print()

def Cone():
	print()
	print(' <======---====*-*====---======>')
	print()
	h=float(input(' Enter Hight of Cone in Centimeters : '))
	r=float(input(' Enter Radius of Base of Cone  in Centimeters : '))
	vcm=round((1/3)*(22/7)*(r**2)*h,2)
	vm=round(vcm/10000,3)
	print()
	print(' <======---====*-*====---======>')
	print(' Area of Cone is',vcm,'cm³ or',vm,'m³')
	print(' <======---====*-*====---======>')
	print()

def Area():
	print(' <======---====*-*====---======>')
	print()
	print(' What would you like to do ?')
	print()
	print(' 1  ---->  Find Area of Cube')
	print(' 2  ---->  Find Area of Cuboid')
	print(' 3  ---->  Find Area of Sphere')
	print(' 4  ---->  Find Area of Cone')
	print()
	print(' <======---====*-*====---======>')
	print()
	t=float(input(' Enter Task Code : '))
	if t==1 or t==2 or t==3 or t==4 :
		if t==1 :
			Cube()
		if t==2 :
			Cuboid()
		if t==3 :
			Sphere()
		if t==4 :
			Cone()
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
		print(' 3  ---->  Main Menu')
		print()
		xit=float(input('>'))
		if xit==1 or xit==2 or xit==3 :
			if xit==1 :
				exit
			if xit==2 :
				Area()
			if xit==3 :
				import main.py
		else :
			print()
			print(' What Du U MeeN ?')
			print()
			exxit()
	exxit()
Area()
