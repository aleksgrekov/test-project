def print_func(text):
    count = 0

    while count <= 6:
        print(text)
        count += 1

text = 'Hello! My name is Aleks'

for _ in range(5):
    print_func(text)
