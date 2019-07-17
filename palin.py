z=input("")
z=z.casefold()
rev=reversed(z)
if list(z) == list(rev):
	print("yes")
else:
	print("no")
