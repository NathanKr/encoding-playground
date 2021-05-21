str = 'בקר טוב'
print(f'str : {str}')

encoding_method = 'utf-8'
# encoding
encoded_str = str.encode(encoding_method)
print(f"encoded_str : {encoded_str}")
print(f"len(encoded_str) : {len(encoded_str)}")

# decoding
decoded_str = encoded_str.decode(encoding_method)
print(f'decoded_str : {decoded_str}')
print(f'len(decoded_str) : {len(decoded_str)}')

