def is_valid_IP(string):
    isValid = 'true'
    octectNumber = ""
    array = []
    octectIndex = 0;
    
    # iterate through string 
    for c in string:
        octectNumber += str(c)

        if (string[c] == "."):
            array[octectIndex] = octectNumber
            octectIndex += 1
            octectNumber = ""


    for i in array:
        print(array[i])
            
            
    # create a string for each octect 
    # octectNumber += c
        

    # make sure octect number is less than 255 and greater than 0
    # make sure there are no leading 0s 

def main():
    is_valid_IP('12.12.12.12')
    

if __name__ == "__main__":
    # execute only if run as a script
    main()
