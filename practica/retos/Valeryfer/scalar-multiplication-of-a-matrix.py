# Link del reto: https://www.deep-ml.com/problems/5

def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	return [[element * scalar for element in row] for row in matrix]
