def quad(b,a,c):
	print(c*b+2*c)
	for i in range(a):
		print('%s%s%s'%(c,' '*b,c))
	print(c*b+2*c)

bas=int(input())
alt=int(input())
carc=str(input())

quad(bas,alt,carc)
