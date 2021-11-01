with open('file_name.txt', 'r') as file:
    for i, line in enumerate(file):
        if i == 0:
            column_keys = line.strip().split(',')
            dict_final = {key: {} for key in column_keys}
            continue
        values_columns = line.strip().split(',')

        for key, value, item in zip(dict_final.keys(), dict_final.values(), values_columns[1:]):
            value[values_columns[0]] = item

print(dict_final)
