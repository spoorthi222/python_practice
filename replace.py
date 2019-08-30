def Replace_str(main_str,sub_sting,pat):
    '''
    this function replaces the sub_string from pat in the main_str
    :param main_str:the sting in which we need to replace
    :param sub_sting:the string that need to be replace in main_str
    :param pat:the string that should be substitued in place sub_str in main_str
    :return:replaced value ll be returned
    '''
    print (main_str.replace(sub_sting, pat))


if __name__ == '__main__':

    string1 =raw_input("enter a string")
    pat = raw_input("enter string to be replace ")
    sub = raw_input("enter string to be placed")
    Replace_str(string1,pat,sub)

