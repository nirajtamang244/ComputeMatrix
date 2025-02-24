import numpy as np

def input_matrix(prompt="input the matrix where each rows are seperated by semicolon \";\""):
    while True:
        userInput= input(prompt)
        newRow= [list(map(float,row.split())) for row in userInput.split(";")]
        rowLength={len(row) for row in newRow }
        if len(rowLength)!= 1:
            print("Error. Put a valid matrix")
            continue
        return np.array(newRow)
    

def addMatrix(A,B):
    return A+B

def subMatrix(A,B):
    return A-B

def mulMatrix(A,B):
    return np.dot(A,B)

def transMatrix(A):
    return A.T

def invertMatrix(A):
    try:
        return np.linalg.inv(A)
    except np.linalg.LinAlgError:
        print("Matrix is singular and cannot be inverted")
        return None

def takeSubMatrix(matrix,startRow,endRow,startColumn,endColumn):
    return matrix[startRow:endRow, startColumn:endColumn]

def determinantOfSub(matrix,startRow,endRow,startColumn,endColumn):
    subMatrix=takeSubMatrix(matrix,startRow,endRow,startColumn,endColumn)
    return np.linalg.det(subMatrix)

def getRightMatrix():
    while True:
        A= input_matrix("what is A?")
        B= input_matrix("what is B?")
        
        if A.shape!=B.shape:
            print("Error, the matrices should have same dimensions!!!")
        return A,B


def main():
    while True: 
        print("Would you like to use pre-defined matrices or input on your own?")
        mode= input("enter '1' for predefined matrices, '2' for custom input:")
    
        if mode=="2":
            A,B= getRightMatrix()
        
        else:
            A=np.array([[1,2,6],[1,2,3],[3,4,8]])
            B=np.array([[5,6,3],[2,6,6],[7,8,4]])
        
        while True:
            print(f"Matrix A:\n {A}")
            print(f"Matrix B:\n {B}")
            print(" Choose the operations from below: \n   1: Add matrices\n2:subtract matrices \n3: multiply matrices \n 4:transpose matrices \n5:invert matrices \n 6:determinant of subMatrix")
            choice=input("Enter the operation number:")
            if choice== "1":
                C=addMatrix(A,B)
                print(C)
            elif choice=="2":
                C=subMatrix(A,B)
                print(C)
            elif choice =="3":
                C=mulMatrix(A,B)
                print(mulMatrix(A,B))
            elif choice== "4":
                C=transMatrix(A)
                print(C)
            elif choice =="5":
                C=invertMatrix(A)
                if C is not None:
                    print(C)
                else:
                    break
            elif choice=="6":
                if A.shape[0]<3 or A.shape[1]<3:
                    print("It should be atleast 3x3 square matrix. Try again")
                    break
                else:
                    print(f"The submatrix of the matrix A is \n{takeSubMatrix(A,1,A.shape[0],1,A.shape[1])}")
                    determinant= determinantOfSub(A,1,A.shape[0],1,A.shape[1])
                    print(f"The determinant of the matrix A is {determinant}")
            else:
                print("invalid choice")
                break
            chooseplay= input("do you want to add in the current matrix? if yes click 'y'")
            if chooseplay.lower()== "y":
                A=C
                print(f"this is your A now:\n{A}")
                B=input_matrix("enter new matrix to compute with the result")
            else:
                break

        again= input("Do you want to quit? click 'q' ")
        if again.lower()=="q":
            print('Thankyou and Bye')
            break

        
if __name__== "__main__":
    main()