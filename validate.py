def validate(valid_array,data_for_validation):
    '''
    thus function checks all the keys in data_for_validation are present in valid_array
    :param valid_array: array of keys
    :param data_for_validation: json object
    :return: true or flase
    '''
    arrkey = []
    arrkey = data_for_validation.keys()
    count =0
    for j in range(len(data_for_validation)):
        for i in range(len(valid_array)):
            if arrkey[j] == valid_array[i]:
                count += 1
                print arrkey[j]
    if count==len(valid_array):
        return True
    else:
        return False

if __name__ == '__main__':

    valid_array= ["name","email","password"]
    data_for_validation = (
        {"name":"spoo",
         "email":"spoo@gmail.com",
         "password":"xyz"
         })
    print (validate(valid_array,data_for_validation))


