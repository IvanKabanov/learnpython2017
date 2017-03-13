item = {
    'type': 'phone',
    'vendor': 'apple',
    'price': 157,
    'color':'black'
    }

def print_item():
    for key, value in item.items():
    #value = str(value)
        print('{}: {}'.format(key, value))

print("Before delete:")
print_item()

try:
    del item['discount']
except KeyError:
    pass
    del item['price']

print("After delete")

print_item()
