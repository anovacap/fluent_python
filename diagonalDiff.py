def diagonalDifference(arr):
    sum_x = 0
    sum_z = 0
    inc = 0
    dec = len(arr[0]) - 1
    for x in range(len(arr) - 1):
        for z in range(len(arr[x]) - 1):
                sum_x += arr[x][inc]
                print(sum_x)
                sum_z += arr[x][dec]
                print(sum_z)
                break
        inc += 1
        dec -= 1
    return sum_x - sum_z

if __name__ == '__main__':
    arr = [[11,2,4],[4,5,6],[10,8,-12]]
    d = diagonalDifference(arr)
    print(d)
