import quopri
m = "=E9=82=A3=E4=BD=A0=E4=B9=9F=E5=BE=88=E6=A3=92=E5=93=A6"
a = quopri.decodestring(m)
print(a.decode())