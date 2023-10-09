
N = int(input("enter : "))

array = [1]
total_chicks = 1
for i in range(2,N+1):
	if i > 6:
		dead = array.pop(0)
		total_chicks -= dead
		print(f"i = {i} pop {dead}")
	array.append(total_chicks * 2)
	total_chicks = total_chicks * 2 + total_chicks
	



print(array)
print(total_chicks)
