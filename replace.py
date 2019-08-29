def Replace_str(main_str,sub_sting,pat):
    '''
    this function replaces the sub_string from pat in the main_str
    :param main_str:
    :param sub_sting:
    :param pat:
    :return:
    '''
    print (main_str.replace(sub_sting, pat))


if __name__ == '__main__':

    string1 =raw_input("enter a string")
    pat = raw_input("enter string to be replace ")
    sub = raw_input("enter string to be placed")
    Replace_str(string1,pat,sub)

