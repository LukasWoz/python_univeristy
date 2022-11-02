import os


def jpg_to_png(path):

    for src in os.listdir(path):
        full_src = os.path.join(path, src)
        if os.path.isfile(full_src):
            dst = src.replace('.jpg', '.png')
            if src != dst:
                full_dst = os.path.join(path, dst)
                os.rename(full_src, full_dst)


if __name__ == '__main__':
    jpg_to_png(r'C:\Folder\jpg')
