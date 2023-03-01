#this code swaps letters of a string from uppercase to lowercase and vice versa
#defining a function that will swap lowercase to uppercase and vice versa
def swap_case(s):
    length = len(s) #determining length of the string for getting the range of the for loop
    sWAP = "" #creating an empty string variable to store swapped string
    for i in range(length):
        #checking if the letter of the string is lowercase or not
        if s[i].islower():
            sWAP += s[i].upper() #converting the lowercase letter
        else: #if the letter is not lowercase then it is uppercase
            sWAP += s[i].lower() #converting uppercase to lowercase
    return sWAP #returning the swapped string

if __name__ == '__main__':
    input = input() #feeding the input
    result = swap_case(input) #calling the function
    print(result) #printing the final output