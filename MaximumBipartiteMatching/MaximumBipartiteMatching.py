

class Solution:
	def maximumMatch(self, G):
		jobsApplicant = {}
		selected = []
		for i in range(len(G[0])):
			selected.append(-1)
			# jobsApplicant[i] = 0

		# Applicant = []
		# for i in range(len(G)):
		# 	Applicant.append(-1)
		# for i in G:
		# 	for j in range(len(i)):
		# 		if i[j] == 1:
		# 			jobsApplicant[j] += 1

		# jobPreference = {}
		# for i in range(len(G)):
		# 	jobPreference[i] = 0



		# print(f"jobs and no of applicants ...{jobsApplicant}")

		
		for  no_ofJob in range(len(G[0])):

			jobsApplicant = {}
			for i in range(len(G[0])):
				if selected[i] == -1:
					jobsApplicant[i] = 0

			# print(f"SELECTION list... ",selected)
			# print(f"job 22 in selection list {selected[22]}")
			

			for i in range(len(G)):
				if i not in selected:
					for j in range(len(G[i])):
						if G[i][j] == 1 and selected[j]==-1:
							jobsApplicant[j] += 1

			# print(f"job applicants list {jobsApplicant}")

			
			loweset_no_of_applicant = 99999999999999999
			The_job = 0
			for i in jobsApplicant:
				if loweset_no_of_applicant > jobsApplicant[i] and selected[i]==-1:
					loweset_no_of_applicant = jobsApplicant[i]
					The_job = i

			if loweset_no_of_applicant == 0:
				selected[The_job] = -2
				continue

		
			jobPreference = {}
			for i in range(len(G)):
				if i not in selected and G[i][The_job]==1:
					jobPreference[i] = 0


			for i in range(len(G)):
				if i not in selected and G[i][The_job] ==1:
					for j in range(len(G[i])):
						if G[i][j] == 1 and selected[j]==-1:
							jobPreference[i] += 1

			
			jobpre_keys = list(jobPreference)
			jobpre_val = list(jobPreference.values())

			int_cadidate = []
			for i in range(len(jobpre_keys)):
				for j in range(i):
					if jobpre_val[j]> jobpre_val[i]:
						jobpre_val[j], jobpre_val[i] = jobpre_val[i], jobpre_val[j]
						jobpre_keys[j], jobpre_keys[i] = jobpre_keys[i], jobpre_keys[j]

			# print(f"jobPreference dictionary : {jobPreference}")
			# print(f"sortedlists are: \n{jobpre_keys}\n{jobpre_val}")

			flag = 0
			for member in jobpre_keys:

				if G[member][The_job] == 1 and member not in selected:
					selected[The_job] = member
					flag = 1
					break

			if flag == 1:
				# print(f"candidate {member} is selected for job {The_job}")
				flag = 0
			else :
				# print(f"\n sorry !!! no candidate is selected for job {The_job}\n")
				selected[The_job] = -2

		# print(selected)
		count = 0
		for i in selected:
			if i!=-1 and i!=-2 :
				count += 1
		return count




with open("fileInput100x100.txt", 'r') as file:
	inputs = file.readlines()

# list_ = eval(input("enter list : "))
list_ = eval(inputs[0].strip())
obj = Solution()
res = obj.maximumMatch(list_)
print(res)

[[0, 1, 1],[1, 0, 1],[1, 0, 0]]