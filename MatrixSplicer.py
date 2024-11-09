# inintialize with already decided numbers
matrixA = [
    [1, 2, 3, 4, 5, 6, 7, 8],
    [9, 10, 11, 12, 13, 14, 15, 16],
    [17, 18, 19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30, 31, 32],
    [33, 34, 35, 36, 37, 38, 39, 40],
    [41, 42, 43, 44, 45, 46, 47, 48],
    [49, 50, 51, 52, 53, 54, 55, 56],
    [57, 58, 59, 60, 61, 62, 63, 64]
]

matrixB = [
    [64, 63, 62, 61, 60, 59, 58, 57],
    [56, 55, 54, 53, 52, 51, 50, 49],
    [48, 47, 46, 45, 44, 43, 42, 41],
    [40, 39, 38, 37, 36, 35, 34, 33],
    [32, 31, 30, 29, 28, 27, 26, 25],
    [24, 23, 22, 21, 20, 19, 18, 17],
    [16, 15, 14, 13, 12, 11, 10, 9],
    [8, 7, 6, 5, 4, 3, 2, 1]
]

# initialize with default value 2s
#rows, cols = 8, 8 # for a 8x8 matrix
#matrixB = [[2 for _ in range(cols)] for _ in range(rows)]

# initialize a blank answer that will be returned
rows, cols = 8, 8 # for a 8x8 matrix
matrixC = [[0 for _ in range(cols)] for _ in range(rows)]

cores = 4
matrixLength = len(matrixA)
splicedRowLength = int(matrixLength / cores)



def main():
    
    #prints matrixA
    for num in matrixA:
            print(num)
    #prints matrixB
    for num in matrixB:
            print(num)
    
    SpliceMatrix(matrixA)

    # prints answer stored in matrixC
    for num in matrixC:
            print(num)


# add handling for odd number of (NxN) / not evenly divisible by 8
# Use modulo

def SpliceMatrix(matrix):
    # these variables are initialized locally so the function has access to them
    # they could also be made global to access globally initialized variables
    currentRow = 0
    spliceToRow = currentRow + splicedRowLength

    # for loop cycles i = 0-3, if cores = 4
    for i in range(cores):
        print(f"Core: {i} processing rows {currentRow} up to but not including {spliceToRow}")
        splicedMatrix = matrix[currentRow:spliceToRow]
        for rows in splicedMatrix:
             print(rows)

        Core(splicedMatrix, matrixB, currentRow, splicedRowLength - 1)

        currentRow += splicedRowLength
        spliceToRow = currentRow + splicedRowLength
        

def Core(splicedMatrix, matrixB, firstRow, lastRow):
    #print(firstRow, lastRow)
    #for num in splicedMatrix:
    #    print(num)
    #for num in matrixB:
    #    print(num)

    for rows in range(splicedRowLength): # 2 rows/loops
        for cols in range(matrixLength): # 8 cols/loops
            #print(splicedMatrix[rows][cols])
            product = 0
            addedProduct = 0
            for idx in range(matrixLength):
                product = (splicedMatrix[rows][idx] * matrixB[idx][cols])
                addedProduct += product
                print(f"{splicedMatrix[rows][idx]} * {matrixB[idx][cols]} = {product}")

            matrixC[rows + firstRow][cols] = addedProduct



main()