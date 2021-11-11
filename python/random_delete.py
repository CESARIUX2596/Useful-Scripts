'''
Function that randomly deletes files in a directory until a certain lenght
'''
import random
import os

def delete_files(files_to_preserve,folder_path, odds):
    files = os.listdir(folder_path)
    if (len(files) < files_to_preserve):
        print('Your folder contains less files that the amount yo whant to preserve.')
        pass
    else:
        while len(files) > files_to_preserve:
            for f in files:
                random.shuffle(files)
                should_i_kill_it = random.randint(1, 100)
                if should_i_kill_it < odds:
                    files.remove(f)
                    os.remove(folder_path + f)
            print('Done')

def main():
    files_to_preserve = 600
    full_path = 'D:/Datasets/rc_car_dataset/image_annotations/'
    odds = 15
    delete_files(files_to_preserve, folder_path, odds)

if __name__ == "__main__":
    main()







