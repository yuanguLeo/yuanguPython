#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
字符串：字符串是以单引号或双引号栝起来的任意文本

字符串运算：

1、字符串连接
格式： 字符串1 + 字符串2

2、输出重复字符串
格式： 字符串1 * n

3、访问字符串中的某一个字符
通过索引下标查找字符，索引从0开始
格式：字符串名[小标]

4、截取字符串
格式：字符串名[下标start : 下标end]
下标start 可省略，代表：从头截取到给定下标之前
下标end 可省略，代表：从给定下标出开始截取到结尾

#eval(str)
#功能：将字符串str当成有效的表达式来求值并返回计算结果
例如：ptint(eval(“+123”))

#len(str)
#功能：返回字符串的长度,字符个数
print(len("weiss is a good man!"))

#r 表示不转义
print(r"weiss \n good man")


#lower(str) 转换字符串中大写字母为小写字母
str20 = “SUNCK is a Good Man”
str21 = str20.lower()
print(str21)

#upper()转换字符串中小写字母为大写字母
print("SUNCK is a Good Man".upper())

#swapcase()转换字符串中小写字母为大写字母，大写字母为小写字母
str22  =  "SUNCK is a Good Man"


#capitalize() 首字母大写，其他小写
str23 = "SUNCK is a Good Man"
print(str23.capitaloze())

#title() 每次单词的首字母大写
str24 = "str.title"


#center(width,fillchar) 返回一个指定宽度的居中字符串，fillchar为填充的字符串，默认空格填充
srt25 = "kaige is a nice man"
print(str25.cneter(40,"*"))

#ijust(width[,fillchar])返回一个指定宽度的左对齐字符串，fillchar为填充的字符串，默认空格填充
str26 = "kaige is a nice man"
print(str26.ijust(40,"%"))

#rjust(width[,fillchar])返回一个指定宽度的右对齐字符串，fillchar为填充的字符串，默认空格填充
str27 = "kaige is a nice man"
print(str27.just(40,"%"))

#zfill(width)返回一个长度为width的字符串，原字符串右对齐，前面补0
str28 = "kaige is a nice man"
print(str28.zfill(40))

#count(str[,start][,end]) 返回字符串中str出现的次数
str29 = “kaige is a very very nice man”
print(str19.count("very",15,len(str29)))

#find(str[,start][,ebd])
#从左到右检测str字符串是否包含在字符串中，可以指定范围，默认从头到尾，得到的是第一次出现的开始下标，没有返回-1
#rfing  从右到左检测
str30 = “kaige is a very very nice man”
print(str30.finger（“very”）)

#index(str,start = 0, end = len(str)) 跟fing()一样，只不过如果str不存在的时候会报一个异常
#rindex()
str31 = "kaige is a very very nice man"
print(str31.index("very"))

#lstrip() 截掉字符串左侧指定的字符，默认为空格
str33 = "     kaige is a good nice man"
print(str33.lstrip("*"))

#rstrip() 截掉字符串右侧指定的字符，默认为空格
str34 = "     kaige is a good nice man"
print(str34.rstrip(),"*")

#strip()
#str35 = "********kaige is a good nice man***********"
print(str35.strip("*"))

'''

#splir(str = "")
#以str为分隔符截取字符串,指定num，则仅截取num个字符串
str38 = "leo**is*******a****good***man"
print(str38.split("*",3))


#splitlinse([keepends]):安装('\t','\r\n','\n')分隔
#keepemde == True   会保留换行符
str40 = '''
leo is a good man!
leo is a nice man!
leo is handsome man!
'''
print(str40)

#join() 以指定的字符串分隔符，将seq中的所有哦元素组合成一个字符串
list41 = ['leo','is','a','good','man']
str42 ="&^%$#".join(list41)
print(str42)

#max()   min()
str43 = "leo is a good man!z"
print(max(str43))
print("*"+min(str43)+"*")


#replace(olddtr,newstr,count) 用newstr替换olddtr，默认是全部替换。如果指定了count,那么只替换前count个
str44 = "leo is a good good good man"
str45 = str44.replace("good","nice",1)
print(str45)

#创建一个字符串映射表
t46 = str.maketrans("good" , "nice")
str47 = "sunck is a good good good man"
str48 = str47.translate(t46)
print(str48)

#startswith(“str,start=0.end=len(str)”) 判断是否是以给定的字符串开头的，没有给定范围，默认整个字符串
str49 = "leo is a good man"
print(str49.startswith("le"))

#endswith(“str,start=0.end=len(str)”) 判断是否是以给定的字符串结尾的，没有给定范围，默认整个字符串
str50 = "leo is a good man"
print(str50.endswith("le"))

#encode(encoding="utf-8",errors="strict")  编码
str51 = "leo is a good man迪"
data52 = (str51.encode("utf-8","ignore"))
print(data52)
print(type(data52))

#解码 注意：要与编码时的编码格式一致
str53 = data52.decode("gbk","ignore")
print(str53)

#isalpha() 如果字符串中至少有一个字符且所有字符都是字母返回True，否则返回False
str54 = "leoisagoodman"
print(str54.isalpha())

#isalnum()如果字符串中至少有一个字符串且所有的字符都是字母或数字返回True,否则返回False
str55 = "la#2s3"
print(str55.isalnum())

#isupper()
#如果字符串中至少有一个英文字符且所有字符都是大写的英文字母返回True,否则返回False
print("ABC".isupper())
print("ABC1".isupper())
print("ABC#".isupper())


#islower()
#如果字符串中至少有一个英文字符且所有字符都是小写的英文字母返回True,否则返回False
print("abc".islower())

#istitle()
#如果字符串是标题化的返回True,否则返回False
print("Leo Is".istitle())
print("Leo is".istitle())
print("leo is".istitle())


#isdigit() 如果字符串中只包含数字字符返回True,否则返回False
print("123".isdigit())


#isnumeric() 同上
print("123".isnumeric())
print("123a".isnumeric())

#isdecimal()字符串中只包含十进制字符
print("123".isdecimal())

#isspace() 如果字符串中只包含空格则返回True,否则返回False
#"\t","\n" 按空格算
print(" ".isspace())
print("\n".isspace())
