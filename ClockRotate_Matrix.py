def rotate90Clockwise(A):
    N = len(A[0])
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = A[i][j]
            A[i][j] = A[N - 1 - j][i]
            A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
            A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
            A[j][N - 1 - i] = temp
    return A
    
n = int(input())
original_mat = []
for i in range(n):
    l = list(map(int,input().strip().split()))
    original_mat.append(l)
    copy_mat = list(map(list, original_mat))
angle_count = 0
while 1:
    query = input().split()
    if query[0] == 'A':
        count = int(query[1])
        count = count // 90
        count = count % 4
        angle_count += count
        for _ in range(count):
            original_mat = rotate90Clockwise(original_mat)
    elif query[0] == 'Q':
        r , c = int(query[1]) , int(query[2])
        print(original_mat[r-1][c-1])
    elif query[0] == 'U':
        r , c ,val = int(query[1]) , int(query[2]) , int(query[3])
        duplicate_matrix = list(map(list,copy_mat))
        duplicate_matrix[r-1][c-1] = val
        for _ in range(angle_count % 4):
            original_mat = rotate90Clockwise(duplicate_matrix)
    elif query[0] == '-1':
        exit()
