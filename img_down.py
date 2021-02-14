from read_the_maxfilename_for_sort import max_number
import requests
import os.path

def download(url, name):
    # get url and name to download.
    print('Processing {0} url:{1}'.format(name,url))
    img = open('{}'.format(name),'wb')
    respone = requests.get(url, stream=True).content
    img.write(respone)
    img.close()

def downloads(urls):
    # create list from range and len of the list
    file_num = [*range(len(urls))]
    file_name = [*reversed(file_num)]

    for i in file_num:
        url = urls[i]
        file = 'Download/{}.jpg'.format(file_name[i])
        if os.path.isfile(file):
            continue
        else:
            print('Processing {0} url:{1}'.format(file_name[i],url))
            img = open('Download/{}.jpg'.format(file_name[i]),'wb')
            respone = requests.get(url, stream=True).content
            img.write(respone)
            img.close()