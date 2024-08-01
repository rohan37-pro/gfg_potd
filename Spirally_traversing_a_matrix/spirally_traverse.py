class Solution:
    def spirallyTraverse(self, matrix):
        row = [i for i in range(len(matrix[0]))]
        col = [i for i in range(len(matrix))]
        row_vector = 1
        col_vector = 1
        spiral_array = []
        while len(row)!=0 and len(col)!=0:
            if row_vector==1 and col_vector==1:
                for i in row:
                    spiral_array.append(matrix[col[0]][i])
                row_vector=0
                col.pop(0)
            elif row_vector==0 and col_vector==1:
                for i in col:
                    spiral_array.append(matrix[i][row[-1]])
                col_vector=0
                row.pop(-1)
            elif row_vector==0 and col_vector==0:
                for i in row[-1::-1]:
                    spiral_array.append(matrix[col[-1]][i])
                row_vector=1
                col.pop(-1)
            elif row_vector==1 and col_vector==0:
                for i in col[-1::-1]:
                    spiral_array.append(matrix[i][row[0]])
                col_vector=1
                row.pop(0)
        return spiral_array


matrix = [[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
[13, 14, 15, 16]]

obj = Solution()
print(obj.spirallyTraverse(matrix))