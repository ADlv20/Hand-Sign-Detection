import os

os.chdir('Tensorflow/workspace/images/train/Spiderman')
print(os.getcwd())

for count, f in enumerate(os.listdir()):
    f_name, f_ext = os.path.splitext(f)
    f_name = "spiderman" + str(count+1)

    new_name = f'{f_name}{f_ext}'
    os.rename(f, new_name)