import os


def catalog_tree(path, tab_count=0, been_here=False):
    for i in os.listdir(path):
        if os.path.isdir(path+"\\"+i):
            print("\t" * tab_count, i, end="\n")
            tab_count += 1
            catalog_tree(path+"\\"+i, tab_count, been_here)
            tab_count -= 1
        else:
            print("\t" * tab_count, i, end="\n")


if __name__ == '__main__':
    catalog_tree(r'C:\Folder')
