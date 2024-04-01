def uuencode():
    str = input("请输入需要编码的字符:")
    data = ""
    for c in str:
        a = format(ord(c), 'b')
        for i in range(8 - len(a)):
            a = "0" + a
        data = data + a

    if (len(data) % 24 != 0):
        lenght = len(data)
        for i in range(24 - lenght % 24):
            data = data + "0"

    print(chr(32 + int(len(data) / 8)), end="")

    for i in range(0, len(data), 24):
        data_1 = data[i:i + 24]
        for j in range(0, len(data_1), 6):
            if int(data_1[j:j + 6], 2) == 0:
                print(chr(int(0x60)))
            else:
                print(chr(int(data_1[j:j + 6], 2) + 32), end="")


def uudecode():
  str = input("请输入需要解码的字符:")
  data = ""

  for c in str[1:]:

      a = format(ord(c) - 32, 'b')
      for i in range(6 - len(a)):

          a = "0" + a


      data = data + a

  for i in range(0, len(data), 24):
    data_1 = data[i:i + 24]
    for j in range(0, len(data_1), 8):

     print(chr(int(data_1[j:j + 8], 2)), end="")

if __name__ == "__main__":
    uudecode()
    print()
    uuencode()