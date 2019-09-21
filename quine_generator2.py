#!/usr/bin/env python3

file_name = input("File (full name) to be turned into a quine: ")
with open(file_name, 'r') as input_file:
    data = input_file.read()
with open(file_name, 'a') as output_file:
    if data[-1] != '\n':
        output_file.write('\n')
        data += '\n'

    data_list = list(data)
    for i in range(len(data_list)):
        if data_list[i] == '\n':
            data_list[i] = '\\n'
        if data_list[i] == '\\':
            data_list[i] = '\\\\'
        if data_list[i] == '\'':
            data_list[i] = '\\\''
        if data_list[i] == '{':
            data_list[i] = '{{'
        if data_list[i] == '}':
            data_list[i] = '}}'
    data = ''.join(data_list)
    escape_curly = "{0}"

    file_name = file_name[:-3]
    output_file.write("from random import randint\n")
    output_file.write('''with open("{0}" + str(randint(0, 10)) + ".py", "w") as output_file:\n'''.format(file_name))
    output_file.write('''    s = r\'\'\'output_file.write('{0}from random import randint\\nwith open("{1}" + str(randint(0, 10)) + ".py", "w") as output_file:\\n    s = r\\'\\'\\'{2}\\'\\'\\'\\n    {2}'.format(s))\'\'\'\n'''.format(data, file_name, escape_curly))
    output_file.write('''    output_file.write('{0}from random import randint\\nwith open("{1}" + str(randint(0, 10)) + ".py", "w") as output_file:\\n    s = r\\'\\'\\'{2}\\'\\'\\'\\n    {2}'.format(s))'''.format(data, file_name, escape_curly))