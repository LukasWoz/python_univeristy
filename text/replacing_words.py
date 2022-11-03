import os
import re


def change_words(path, word_dict):
    outfile = open(r'C:\Folder\modified2.txt', "w+")
    try:
        with open(path) as txt_in:
            for line in txt_in:
                # splited = line.split()
                splited = re.split(r'[,. \t]', line)
                splited_update = []
                for word in splited:
                    splited_update.append(word_dict.get(word, word))
                outfile.write(" ".join(splited_update))
                print(splited)
                print(splited_update)
    except:
        print('Unable to open file:', path)
        exit()


if __name__ == '__main__':
    word_dict = {'i': 'oraz', 'oraz': 'i', 'nigdy': 'prawie nigdy', 'dlaczego': 'czemu'}
    change_words(r'C:\Folder\tekst.txt', word_dict)
