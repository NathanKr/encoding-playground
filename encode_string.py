str = 'hello world' # the default method of string encoding in python is utf-8
str_utf8_encoded_to_bytes : bytes = str.encode('utf-8')

print(f'type(str_utf8_encoded_to_bytes) : {type(str_utf8_encoded_to_bytes)} , str_utf8_encoded_to_bytes : {str_utf8_encoded_to_bytes}')
for c in str_utf8_encoded_to_bytes:
    print(hex(c))

# the following is ok because mapping of 'helloe world' is the same for ascii and utf-8
str = 'hello world' # the default method of string encoding in python is utf-8
str_ascii_encoded_to_bytes : bytes = str.encode('ascii')
print(f'type(str_ascii_encoded_to_bytes) : {type(str_ascii_encoded_to_bytes)} , str_ascii_encoded_to_bytes : {str_ascii_encoded_to_bytes}')
for c in str_utf8_encoded_to_bytes:
    print(hex(c))


# the following will throw 
try:
    str = 'שלום עולם' # the default method of string encoding in python is utf-8
    str_utf8_encoded_to_bytes : bytes = str.encode('ascii')
except Exception as e:
    print (e)


