import json

def write_json_to_file(data):
    '''
    this function writes the json object to the file (sample.json)
    :param data: data is dict object which contains json data
    :return: nothing
    '''
    with open("sample.json","w")as outfile:
        json.dump(data,outfile)


if __name__ == '__main__':

    data = {}
    data["user"]= []
    data["user"]. append(
      {"name" : "Spoorthi",
             "age"  : 21,
             "email_id" : "spoorthi.n222@gmail.com",
             "password" : "Spoorthin222"})
    data["user"]. append({
           "name" : "Kavyashree",
            "age"  : 22,
            "email_id" : "kkm18311@gmail.com",
            "password" : "kjadjkhdefajvo"
            })
    print data
    write_json_to_file(data)


