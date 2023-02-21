

class Solution:
	def goodStones(self, n, arr):
		not_visited = [i for i in range(n)]
		Bad_stone = []
		pointer = 0
		good_stone = 0
		temp_stone = []
		good_stone_lis = []
		total_visited = 0
		while total_visited != n:
			if pointer >= n or pointer < 0 or pointer in good_stone_lis:
				good_stone += len(temp_stone)
				good_stone_lis += temp_stone
				total_visited+= len(temp_stone)
				temp_stone = []
				print(f"good stones :{good_stone_lis} --> {good_stone} , {total_visited}")
				if total_visited != n:
					pointer = not_visited[0]
				continue

			elif pointer in Bad_stone or pointer in temp_stone:
				Bad_stone += temp_stone
				total_visited+= len(temp_stone)
				temp_stone = []
				print(f"Bad_stone {Bad_stone} , {total_visited}")
				if total_visited !=n :
					pointer = not_visited[0]
				continue


			step = arr[pointer]
			not_visited.remove(pointer)
			temp_stone.append(pointer)
			print(arr, pointer)
			if step == 0:
				Bad_stone += temp_stone
				total_visited+= len(temp_stone)
				temp_stone = []
				print(f"Bad_stone {Bad_stone} , {total_visited}")
				if total_visited !=n :
					pointer = not_visited[0]
				continue
			pointer += step

		return good_stone



if __name__ == "__main__":
	n = int(input("enter a size : "))
	arr = list(map(int, input("enter array : ").split()))

	obj = Solution()
	print(obj.goodStones(n, arr))