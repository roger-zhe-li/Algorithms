# Link to the original problem w/o premium subscription: 
# https://www.lintcode.com/problem/sparse-matrix-multiplication/description 


class Solution:
    """
    @param a: a sparse matrix
    @param b: a sparse matrix
    @return: the result of A * B
    """
    def multiply(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        # write your code here
        res_shape0 = len(a)
        res_shape1 = len(b[0])
        res_shape_int = len(a[0])
        res = [[0] * res_shape1 for _ in range(res_shape0)]
        # print(len(res), len(res[0]))
        for i in range(res_shape0):
            for j in range(res_shape_int):
                if a[i][j] != 0:
                    for k in range(res_shape1):
                        if b[j][k] != 0:
                            print(i, j, k, a[i][j], b[j][k])
                            res[i][k] += a[i][j] * b[j][k]
                            print(res)
        return res
