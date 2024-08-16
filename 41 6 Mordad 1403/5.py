import pyzipper
import os

secret_password = b'1234'
ended_files = []
# cur_dir=os.getcwd()
# cur_dir.join('radmehr')
# radmehr_dir = os.path.join(cur_dir, 'radmehr')

# for cur_dir_name_str, folders_list, files_list in os.walk(radmehr_dir):
for cur_dir_name_str, folders_list, files_list in os.walk('radmehr'):
    # print(files_list)
    # print(folders_list)
    # print(cur_dir_name_str)
    # print('-'*80)
    for file in files_list:
        file_name = os.path.join(cur_dir_name_str, file)
        # print(file_name)
        ended_files.append(file_name)
        with open(file_name, 'rb') as f:
            data = f.read()
            with pyzipper.AESZipFile(f'{file_name}.zip', 'w', compression=pyzipper.ZIP_LZMA, encryption=pyzipper.WZ_AES) as zf:
                zf.setpassword(secret_password)
                zf.writestr(file, data)

for file in ended_files:
    os.remove(file)
