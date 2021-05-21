str_ascii_encoded : str = b"\x68\x65\x6c\x6c\x6f\x20\x77\x6f\x72\x6c\x64" # hello world
for c in str_ascii_encoded:
    print(hex(c))


str_ascii_encoded = str_ascii_encoded.decode("ascii")
print(str_ascii_encoded)
