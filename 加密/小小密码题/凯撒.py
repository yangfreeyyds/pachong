def decrypt(ciphertext, shift):
    """移位解密函数"""
    plaintext = ''
    for char in ciphertext:
        if char.isalpha(): # 如果是字母，进行移位解密
            if char.isupper():
                plaintext += chr((ord(char) - shift - 65) % 26 + 65) # 大写字母移位解密
            else:
                plaintext += chr((ord(char) - shift - 97) % 26 + 97) # 小写字母移位解密
        else: # 如果不是字母，直接输出
            plaintext += char
    return plaintext

# 加密密文和移位数
ciphertext = 'XMZFSLDZ'
shift = 3
ciphertext = ciphertext.lower()
# 小写易于观察
# 枚举所有可能的移位数，输出所有解密结果
for i in range(26):
    plaintext = decrypt(ciphertext, i)
    print("%d %s"% (i, plaintext))