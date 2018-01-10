import re


def convert(text):
    if text.isdigit():
        return int(text)
    else:
        return text.lower()


def alphanum_key(element):
    return_data= []
    for c in re.split('([0-9]+)', element):
        converted_value = convert(c)
        return_data.append(converted_value)
    return return_data


def natural_sort(data):
    return sorted(data, key = alphanum_key)


