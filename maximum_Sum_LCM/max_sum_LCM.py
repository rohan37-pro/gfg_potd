

n = int(input("enter : "))


array=[]
loop = int(n**0.5)
for i in range(1,loop+1):
	print(f"running for {i}")
	if n%i==0 :
		array.append(i)
		array.append(n//i)

array = set(array)
sum = 0
for i in array:
	sum += i

print(array)
print(sum)