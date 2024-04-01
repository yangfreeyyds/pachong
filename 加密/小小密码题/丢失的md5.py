import hashlib
for i in range(32,127):
    for j in range(32,127):
        for k in range(32,127):
            m=hashlib.md5()
            data = 'TASC' + chr(i) + 'O3RJMV' + chr(j) + 'WDJKX' + chr(k) + 'ZM'
            des = hashlib.md5(data.encode('utf-8')).hexdigest()
            if 'e9032' in des and 'da' in des and '911513' in des:
                print(des)