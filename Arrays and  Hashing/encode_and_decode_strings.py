def encodeString(arr):
    res = ""
    for each_str in arr:
        res += (str(len(each_str)) + "#" + each_str)
    return res

def decodeString(s):
    res = []
    i = 0
    while(i < len(s)):
        j = i
        while(s[j] != "#"):
            j += 1
        length = int(s[i:j])
        res.append(s[j+1:j+1+length])
        i = j + 1 + length
    return res


arr = ["neet","code","love","you"]
encoded = encodeString(arr)
print(encoded)
print(decodeString(encoded))