print(len('ABC')) # 3
print(len('森A')) # 2
x = b'\xc9\xad' 
print(x) 
print(x.decode("GBK")) # 森
print(len(x)) # 2
# 1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节。
print(len('森'.encode('utf-8'))) # 3
print(len('森A'.encode('utf-8'))) # 4