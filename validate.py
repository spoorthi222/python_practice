def validate(valid_array,data_for_validation):
    if data_for_validation not in valid_array:
        return False
    elif "email" not in valid_array:
        return False
    elif "password" not in valid_array:
       return False

    return True

if __name__ == '__main__':

    valid_array= ["name","email","password"]
    data_for_validation = (
        {"name":"spoo",
         "email":"spoo@gmail.com",
         "password":"xyz"
         }
    )
    print (validate(valid_array,data_for_validation))


