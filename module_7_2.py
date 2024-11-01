def custom_write(file_name, strings):
    strings_positions = {}

    with open(file_name, 'w', encoding='utf-8') as file:
        for line_num, line_text in enumerate(strings, start=1):
            byte_position = file.tell()
            file.write(line_text + '/n')
            strings_positions[(line_num, byte_position)] = line_text
    return strings_positions

info = [
    'Text for tell.'
    '\nИспользуйте кодировку utf-8'
    '\nBecouse thre are 2 languages!'
    '\nСпасибо'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)