
def LCS(string1, string2):

    sequenceLength = 0
    finalSequence = "" 
    
    for i in string1:
        for j in string2:
            if compare(i, j):
                sequenceLength += 1
                LCS()
            elif(not compare(i,j)):
                LCS()

    print("Sequence Length: " + sequenceLength)
    return sequenceLength
                
def compare(char1, char2):
    if char1 == char2:
        # print("true")
        return True
    else:
        # print("false")
        return False
    
def main():
    string1 = "GXTXAYB"
    string2 = "AGGTAB"
    print(string1)
    print(string2)

    value = compare("A", "B")
    print(value)
    value = compare("A", "A")
    print (value)
  
if __name__== "__main__":
  main()
