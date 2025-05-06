#not, in

key = "abcdefg"

check = "abc" in key

check2 = "ZXC" in key

check3 = "ZXC" not in key

print(f"Key: {key}\n")

print(f"Abc in key: {check}\n")

print(f"ZXC in key: {check2}")

print(f"ZXC not in key: {check3}")