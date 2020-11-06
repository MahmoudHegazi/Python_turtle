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
