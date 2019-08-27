def validate(valid_array,data_for_validation):
    if "name" not in valid_array:
        return False
    elif "email" not in valid_array:
        return False
    elif "password" not in valid_array:
        return False

    return True

valid_array= ({"name":"spoorthi",
               "email":"spoo@gmail.com",
               "password":"xyz"}
)
data_for_validation = (
    {"name":"spoo",
     "email":"spoo@gmail.com",
     "password":"xyz"
     }
)
print (validate(valid_array,data_for_validation))


