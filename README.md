# bypassAV
## 简介
破产版免杀，大致思路是将shellcode异或，之后在主程序中解码。
关键是清除一些符号信息，采用boy-hack大佬的go-strip

## 使用方法
```bash
python3 xor.py
```
# Reference 
https://github.com/boy-hack/go-strip