def print_func(text):
    count = 0

    while count < 6:
        print(text)
        count += 1
    return count

text = 'Hello! My name is Aleks'

if print_func(text) == 6:
    print('This is fun!')
