import argparse

CODE = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F", "--.": "G",
    "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N",
    "---": "O", ".--．": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
    "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z",

    "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4",
    ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9",

    ".-.-.-": ".", "---...": ":", "--..--": ",", "-.-.-.": ";", "..--..": "?",
    "-...-": "=", ".----.": "'", "-..-.": "/", "-.-.--": "!", "-....-": "-",
    "..--.-": "_", ".-..-.": '"', "-.--.": "(", "-.--.-": ")", "...-..-": "$",
    ".-...": "&", ".--.-.": "@", ".-.-.": "+",
}  # 摩斯密码字典


# 编码模块
def morse_encode(n):
    # n = input("[+]要编码的明文为: ").upper()
    inverted_code = {value: key for key, value in CODE.items()}
    codelist = []
    keylist = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.:,;?='/!-_\"()$&@+"
    # keylist = []
    # for i in inverted_code.keys():
    #    keylist.append(i)
    for i in n:
        codelist.append(str(inverted_code.get(i)) + " ")
    for i in codelist:
        if i == 'None ':
            print("Error！仅支持如下字符：\n" + ''.join(keylist))
            exit()
        else:
            continue
    print("[=]编码结果为:\n" + ''.join(codelist))


# 解码模块
def morse_decode(n):
    # n = input("[+]要解码的密文为: ")
    codelist = []
    spl = input(r"[+]分隔符" + '("/"或空格)' + "为:")
    if len(spl) == 1:
        if ord(spl) == 32 or ord(spl) == 47:
            if spl not in n:
                print("[x]请检查分隔符是否正确!")
                print("[!]如果只翻译一个字符请在最后加空格，并将分隔符设为空格！")
                exit()
            else:
                s = str(n).split(spl)
            for i in s:
                codelist.append(str(CODE.get(i)))
            if codelist[0] == str(None):
                print("[x]请检查分隔符或密文是否正确")
                exit()
            else:
                if ord(n[-1]) == 32:
                    codelist.pop()
                print("[=]解码结果为:" + ''.join(codelist))
        else:
            print("[x]请输入"' / '"或 空格！")
            exit()
    elif len(spl) == 0:
        print("[x]请输入分隔符！")
        print("[!]如果只翻译一个字符请在最后加空格，并将分隔符设为空格！")
        exit()
    elif len(spl) > 1:
        print("[x]请输入一位分隔符！")
        exit()

n = "-..../.----/-..../-..../-..../...--/--.../....-/-..../-..../--.../-.../...--/.----/--.../...--/..---/--.../--.../....-/...../..-./--.../...--/...--/-----/...../..-./...--/...--/...--/....-/...--/...../--.../----./--.../-.."
print(morse_encode(n))

m = '.. .-.. --- ...- . -.-- --- ..-'
print(morse_decode(n))


