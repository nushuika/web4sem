def matrix_multiply(n, matrix_a, matrix_b):
    result_matrix = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result_matrix[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return result_matrix

if __name__ == "__main__":
    n = int(input())

    matrix_a = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix_a.append(row)

    matrix_b = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix_b.append(row)

    result = matrix_multiply(n, matrix_a, matrix_b)

    for row in result:
        print(' '.join(map(str, row)))
