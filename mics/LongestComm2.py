def longestCommonSubsequence(string1, string2):
    string = ""
    count = 0
    
    for x in string1:
        for y in string2:
            if y == x:
                string += x
                count += 1
    print (string)
    return count

def main():
  count = longestCommonSubsequence("ABCDGH","AEDFHR")
  print(count)
  
if __name__== "__main__":
  main()

        
