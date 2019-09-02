
def palindrome_string():
    string1 = raw_input("enter a string")
    string2 = string1[::-1]
    print string2
    if string1 == string2:
         print "string is palindrome "
    else:
        print "string is not a palindrome"

if __name__ == '__main__':
    palindrome_string()