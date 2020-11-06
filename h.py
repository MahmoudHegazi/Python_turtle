import turtle
hend = turtle.Turtle()
hend.color('pink')



def drawh():
	for side in range(3):
		if side % 2 == 0:
			hend.left(90)
			hend.forward(100)
			hend.right(180)
			hend.forward(200)
			hend.left(180)
			hend.forward(100)
		else:
			hend.right(90)
			hend.forward(100)
	app = str(input('do you wanna draw h  Y/N'))
	if app == 'y' or app == 'Y':
		drawh()

drawh()


	
