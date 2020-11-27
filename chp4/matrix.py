from typing import List, Tuple, Callable
import math

# 타입 명사를 위한 별칭
Vector = List[float]
Matrix = List[List[float]]

A = [[1, 2, 3], # A는 2개의 행과 3개의 열로 구성되어 있다.
     [4, 5, 6]]

B = [[1, 2],    # B는 3개의 행과 2개의 열로 구성되어 있다.
     [3, 4],
     [5, 6]]

'''
수학에서는 첫 번째 행을 행1, 첫 번째 열을 열1로 표기한다.
하지만 파이썬의 리스트는 0부터 시작하기 때문에 여기서도 행0, 열1로 표기했다.
'''

def shape(A: Matrix) -> Tuple[int, int]:
    """(열의 개수, 행의 개수)를 변환"""
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0 # 첫 번째 행의 원소의 개수
    return num_rows, num_cols

assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3) # 2행, 3열

'''
행렬이 n개의 행과 k개의 열로 구성되어 있다면 이 행렬을 'n x k 행렬' 이라고 부르자.
n x k 행렬에서 각 행의 길이는 k이고 각 열의 길이는 n 이다.
'''

def get_row(A: Matrix, i: int) -> Vector:
     """A의 i번째 행을 반환"""
     return A[i]           # A[i]는 i번째 행을 나타낸다.

def get_column(A: Matrix, j: int) -> Vector:
     """A의 j번째 열을 반환"""
     return [A_i[j]           # A_i 행의 j번째 원소
             for A_i in A]    # 각 A_i 행에 대해

def make_matrix(num_rows: int, 
                num_cols: int,
                entry_fn: Callable[[int, int], float]) -> Matrix:
     
     """
     (i,j)번째 원소가 entry_fn(i,j)인
     num_rows x num_cols 리스트를 반환
     """
     return [[entry_fn(i, j)           # i가 주어졌을 때, 리스트를 생성한다.
             for j in range(num_cols)]   # [entry_fn(i,0), ...]
             for i in range(num_rows)]  # 각 i에 대해 하나의 리스트를 생성한다.
     
def identity_matrix(n: int) -> Matrix:
     """ nxn 단위 행렬을 반환"""
     return make_matrix(n, n, lambda i, j: 1 if i == j else 0)

# print(make_matrix(5, 5, lambda i, j: 1 if i == j else 0))
assert identity_matrix(5) == [[1, 0, 0, 0, 0],
                              [0, 1, 0, 0, 0],
                              [0, 0, 1, 0, 0],
                              [0, 0, 0, 1, 0],
                              [0, 0, 0, 0, 1]]


