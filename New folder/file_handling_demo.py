#file handling
#read the example.txt

try:
    with open('example4.txt', 'r') as file1:
        #read the file
        content =file1.read()
        print(content)
except FileNotFoundError:
    print('File Not Found')
except IOError as e:
    print(f'IO error {e}')

finally:
    print('File Handling is completed')