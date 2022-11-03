import os
import re


def delete_words(path, word_list):
    outfile = open(r'C:\Folder\modified.txt', "w+")
    try:
        with open(path) as txt_in: #, open(r'C:\Folder\modified.txt', "w+") as txt_out:
            for line in txt_in:
                #splited = line.split()
                splited = re.split(r'[,. \t]',line)
                splited_update = [i for i in splited if i not in word_list]
                outfile.write(" ".join(splited_update))
                print(splited)
                print(splited_update)
    except:
        print('Unable to open file:', path)
        exit()


if __name__ == '__main__':
    word_list = ["sie", "i", "oraz", "nigdy", "dlaczego", ]
    delete_words(r'C:\Folder\tekst.txt', word_list)
