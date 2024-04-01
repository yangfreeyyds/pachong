import random


def decrypt(input_file):
    decrypted_text = ""  # 用于存储解密后的字符串
    with open(input_file, 'r') as cipher_file:
        mapping = {}
        arr = list(range(26))
        random.shuffle(arr)

        for i in range(26):
            mapping[chr(ord('a') + arr[i])] = chr(ord('a') + i)
            mapping[chr(ord('A') + arr[i])] = chr(ord('A') + i)

        for line in cipher_file:
            for ch in line:
                if ch in mapping:
                    decrypted_text += mapping[ch]  # 将解密后的字符添加到解密字符串中
                else:
                    decrypted_text += ch

    return decrypted_text

cout=0
input_file = "Cipher.txt"
while(1):
   decrypted_string = decrypt(input_file)
   n = decrypted_string[-28:-24]

   #print(decrypted_string[-28:-24])  # 打印解密后的字符串
   if n == "flag":
       print(decrypted_string)
       cout=cout+1;
       if cout == 200:
           break;