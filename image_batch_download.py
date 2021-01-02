from read_the_maxfilename_for_sort import max_number
import requests

i = 1
temp_number = max_number()

def download(url):
    global i
    global temp_number
    print('Processing {0} url:{1}'.format(i,url))
    img = open('{}.jpg'.format(temp_number),'wb')
    respone = requests.get(url, stream=True).content
    img.write(respone)
    i += 1
    temp_number += 1
    img.close()