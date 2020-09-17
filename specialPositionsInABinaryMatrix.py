# Given a rows x cols matrix mat, where mat[i][j] is either 0 or 1,
# return the number of special positions in mat.
#
# A position (i,j) is called special if mat[i][j] == 1 and
# all other elements in row i and column j are 0 (rows and columns are 0-indexed).

class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """


        i_row = {}
        j_column = {}
        special_indexes = []

        # Checks for unique 1's in each row. adds positions to special_indexes if a 1.
        # If more than one 1, removes positions from special indexes and starts again with next row.
        for i, row in enumerate(mat):
            for j, column in enumerate(row):
                if column == 1:
                    special_indexes.append([i, j])

        removal_indexes = []
        for x, position in enumerate(special_indexes):
            try:
                removal_indexes.append(i_row[str(position[0])])
                removal_indexes.append(x)
            except KeyError:
                i_row[str(position[0])] = x

        for y, position in enumerate(special_indexes):
            try:
                removal_indexes.append(j_column[str(position[1])])
                removal_indexes.append(y)
            except KeyError:
                j_column[str(position[1])] = y

        set_removal_indexes = set(removal_indexes)
        sorted_indexes = sorted(set_removal_indexes, reverse=True)
        for index in sorted_indexes:
            special_indexes.pop(index)

        return len(special_indexes)


s = Solution()
s.numSpecial([[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,1],[0,0,0,0,1,0,0,0],[1,0,0,0,1,0,0,0],[0,0,1,1,0,0,0,0]])

class BetterSolution:
    def betternNumSpecial(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        #taking transpose of matrix
        lst = [[mat[j][i] for j in range(n)] for i in range(m)]
        res = 0
        for i in range(n):
            for j in range(m):
                #Checking if current element is 1 and sum of elements of current row and column is also 1
                if mat[i][j] == 1 and sum(mat[i]) == 1 and sum(lst[j]) == 1:
                    res += 1
        return res

