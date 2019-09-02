
def unique_names():
    '''
    this function reads the names from file names.txt and prints the unique names in the file.
    :return: nothing
    '''
    f = open("names.txt","r")
    if f.mode == 'r':
        contents = f.readlines()
        list_set = set(contents)
        unique_list = (list(list_set))
        print unique_list

if __name__ == '__main__':
    unique_names()