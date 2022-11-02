import os


def file_count(path):
    counter = 0
    for i in os.listdir(path):
        counter+=1
    return counter


if __name__ == '__main__':
    print(file_count(r'C:\Folder'))
