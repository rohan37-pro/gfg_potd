

def rearrange(S, N):
	vowels = ['a','e','i','o','u']
	vowel_count = 0
	vowels_in_S = []
	consonant_in_S = []
	for i in S:
		if i in vowels:
			vowel_count += 1
			vowels_in_S.append(i)
		else:
			consonant_in_S.append(i)

	vowels_in_S.sort()
	consonant_in_S.sort()

	if vowel_count > (N - vowel_count + 1) or vowel_count < (N - vowel_count -1):
		return -1

	if vowel_count < N - vowel_count:
		r = 0
	else:
		char = min(vowels_in_S[0] , consonant_in_S[0])
		if char in vowels:
			r = 1
		else :
			r = 0
	
	new_string = ''
	i_v = 0
	i_c = 0
	for i in range(N):
		if r == 1:
			new_string += vowels_in_S[i_v]
			r = 0
			i_v += 1
		elif r == 0 :
			new_string += consonant_in_S[i_c]
			r = 1
			i_c += 1
		#print(new_string)
	return new_string




S = input("enter a string : ")
print()
print()
print(rearrange(S,len(S)))