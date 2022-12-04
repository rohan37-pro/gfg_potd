
def isItPossible(S, T, M, N):
	if M != N:
		return 0
	S_A = S.count('A')
	S_B = S.count('B')
	S_has = S.count('#')
	T_A = T.count('A')
	T_B = T.count('B')
	T_has = T.count('#')
	if S_A == T_A and S_B == T_B and S_has == T_has:
		S_dic = {'A': [], 'B': [], '#': []}
		T_dic = {'A': [], 'B': [], '#': []}
		for i in range(M):
			S_dic[S[i]].append(i)
			T_dic[T[i]].append(i)
		print(S_dic, T_dic)

		for i in range(len(S_dic['A'])):
			if S_dic['A'][i] >= T_dic['A'][i]:
				for k in [j for j in range(T_dic['A'][i], S_dic['A'][i])]:
					if k in S_dic['B']:
						return 0
					else :
						pass
			else:
				return 0

		for i in range(len(S_dic['B'])):
			if S_dic['B'][i] <= T_dic['B'][i]:
				for k in [j for j in range(S_dic['B'][i]+1, T_dic['B'][i]+1)]:
					if k in S_dic['A']:
						return 0
					else:
						pass
			else:
				return 0

		return 1
		
	else: 
		return 0





if __name__ == "__main__":
	s = input("enter a string : ")
	t = input("enter a string : ")

	print(isItPossible(s,t,len(s),len(t)))