#그냥 연습했습니다. 중요한 내용은 노트북 파일에 있어요~!
import numpy as np

array1 = np.array([[1, 2],
                   [3, 4]]) #A행렬
array2 = np.array([[5, 6],
                   [7, 8]]) #B행렬

print("A:")
print(array1)
print("\nB:")
print(array2)
print("\nAB :")
print(array1 @ array2)