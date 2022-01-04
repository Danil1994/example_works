"""
this function create sudoku
 in the range from 1 to 42 squared very fast
 """

def make_sudoku(size):
    spisok_1=[]
    sudoku=[]
    for i in range (size**2):
        spisok_1.append(i+1)
    for i in range(size):
        for j in range(size):
            sudoku.append(spisok_1)
            spisok_1=spisok_1[size:]+spisok_1[:size]
        spisok_1=spisok_1[1:]+spisok_1[:1]
    
    return sudoku

print (make_sudoku(4))
