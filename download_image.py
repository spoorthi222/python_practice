import requests
def download_images(list):
    '''
    this function downloads the image and stores in the directory
    :param list:  it is a list of urls
    :return: nothing
    '''
    str =["python1","python2","python3"]
    for i in range(len(list)):
        r= requests.get(list[i])
        with open (str[i]+".jpg","wb") as f:
            f.write(r.content)

if __name__ == '__main__':
    links = [ "https://bucketdemotrill.s3-ap-southeast-1.amazonaws.com/1.jpeg_1547107887.jpeg",
              "https://bucketdemotrill.s3-ap-southeast-1.amazonaws.com/1.jpeg_1548664079.jpeg",
              "https://bucketdemotrill.s3-ap-southeast-1.amazonaws.com/1.jpeg_1549956673.jpeg"
    ]
    download_images(links)

