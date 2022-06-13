fileN = input('name of file you need to change: ')
enc = input('what encoding file using(e.g. utf-8): ')
char_b = input('what symbol change: ')
char_c = input('ON what symbol: ')


with open(fileN, "rt", encoding=enc) as file_handle:
    file_content: str = file_handle.read()
 
file_content = file_content.replace(char_b , char_c)
 
with open(fileN, "wt", encoding=enc) as file_handle:
    file_handle.write(file_content)
