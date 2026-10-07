import numpy as np

def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	arr_a = np.array(a)
	arr_b = np.array(b)
	if arr_a.shape[1] != arr_b.shape[0]:
		return -1
		
	return (arr_a @ arr_b).tolist()