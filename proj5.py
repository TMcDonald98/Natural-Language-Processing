'''
Class: CPSC 475-01
Team Member 1: Thomas McDonald
Team Member 2: Diego Valdez
Pgm Name: proj5.py 
Pgm Desc: minimum edit distance and alignment
Usage: 1) python pro5.py source target
'''
import sys

def main():
    target = sys.argv[2]
    source = sys.argv[1]
    distanceMatrix = getMatrix(target, source)
    distanceMatrix = fillMatrix(distanceMatrix, target, source)

    
    print("Target: "+target)
    print("Source: " + source)
    print"\nMin. Edit Distance: ", findCost(distanceMatrix), "\n"
    align(distanceMatrix, target, source)

def getMatrix(word1, word2): 
    matrix = [[0 for x in range(len(word2)+1)]for y in range(len(word1)+1)] 
    #Stores words in array
    for count1 in range(0, len(word1)+1):
        matrix[count1][0] = count1
    for count2 in range(0, len(word2)+1):
        matrix[0][count2] = count2
    return matrix

def fillMatrix(matrix, word1, word2):
    for i in range(1, len(matrix)):
        for k in range(1, len(matrix[0])):
            if(word1[i-1] == word2[k-1]):
                cost = 0
            else:
                cost = 2
            matrix[i][k] = min([matrix[i-1][k] + 1,#insertion
                                matrix[i-1][k-1] + cost,#substitusion
                                matrix[i][k-1] + 1])#delete
    return matrix

def findCost(matrix):
    return matrix[len(matrix)-1][len(matrix[0])-1]

def align(matrix, word1, word2):
    path1=""
    path2=""
    operations=""
    i=len(word1)
    j=len(word2)
    while(i != 0 or j != 0):
        if(i == 0):
            j-=1
            path1+="-"
            path2+=word2[j]
            operations+="d"
        elif(j==0):
            j-=1
            path2+="-"
            path1+=word1[i]
            operations+="i"
        elif(word1[i-1]== word2[j-1]):#same letter
            i-=1
            j-=1
            path1+=word1[i]
            path2+=word2[j]
            operations+=" "
        elif(matrix[i-1][j-1]< matrix[i][j]):#substitue
            i-=1
            j-=1
            path1+=word1[i]
            path2+=word2[j]
            operations+="s"
        elif(matrix[i][j-1]< matrix[i][j]):#delete
            j-=1
            path1+="-"
            path2+=word2[j]
            operations+="d"
        elif(matrix[i-1][j]< matrix[i][j]):
            i-=1
            path2+="-"
            path1+=word1[i]
            operations+="i"
        else:
            print(i)
            print(j)
            print(word1[i-1])
            print(word2[j-1])
            break
    print("Alignment:")
    print(path2[::-1])
    print(path1[::-1])
    print(operations[::-1])

def displayMatrix(matrix):    
    for k in range(0, len(matrix[0])):
        for i in range(0, len(matrix)):
            print(matrix[i][len(matrix[0])-1-k]),
        print("")
        
main()