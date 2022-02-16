# view = ['布达拉宫', '稻城亚丁', '故宫', '张家界','九寨沟','丽江古城','雅鲁藏布江大峡谷','乐山大佛','万里长城']
# print(view)
# print(sorted(view)) #sorted()按照字母顺序临时性排序
# print(view)
# print(sorted(view,reverse=True)) #sorted()加入reverse=true，按照字母相反顺序临时性排序
# print(view)

# view.reverse() #reverse（）按照字母相反顺序永久性排序
# print(view)

# view.reverse() 
# print(view)

# view.sort() #sort()按照字母顺序永久性排序
# print(view)

# view.sort(reverse=True) #按照字母相反顺序永久性排序
# print(view)

# a=['1']
# b=a
# a.append('2')
# b.append('3')
# print(a)
# print(b)

# import turtle as t
# t.penup()
# t.setx(-280)
# t.sety(100)
# t.pd()
# t.fd(20)
# t.bk(10)
# t.rt(90)
# t.fd(80)
# t.left(90)
# t.fd(10)
# t.rt(180)
# t.fd(20)


# t.penup()
# t.setx(-180)
# t.sety(100)
# t.pd()
# t.left(90)
# t.fd(70)
# t.circle(10,180)

# t.penup()
# t.setx(-160)
# t.sety(60)
# t.pd()
# t.circle(-30)

# t.penup()
# t.setx(-90)
# t.sety(90)
# t.pd()
# t.rt(150)
# t.fd(70)
# t.lt(120)
# t.fd(70)

# t.penup()
# t.setx(-10)
# t.sety(60)
# t.pd()
# t.rt(60)
# t.fd(60)
# t.left(90)
# t.circle(30,180)
# t.circle(30,145)

# t.penup()
# t.setx(130)
# t.sety(100)
# t.pd()
# t.rt(145)
# t.fd(60)
# t.left(90)
# t.fd(40)
# t.left(90)
# t.fd(60)
# t.left(180)
# t.fd(140)
# t.rt(90)
# t.fd(40)

# t.penup()
# t.setx(210)
# t.sety(35)
# t.pd()
# t.circle(-30)

# t.penup()
# t.setx(250)
# t.sety(100)
# t.pd()
# t.lt(90)
# t.fd(60)
# t.left(90)
# t.fd(40)
# t.left(90)
# t.fd(60)
# t.left(180)
# t.fd(80)

# t.exitonclick()
from ssl import AlertDescription


alien={}
alien['age']=10
print(alien)
alien['age']=20
print(alien)
del alien['age']
print(alien)

user_0 = { 
 'username': 'efermi', 
 'first': 'enrico', 
 'last': 'fermi', 
 } 

# item方法将每个键值对以元组形式分别存放在列表中
# key方法将每个键分别存放在列表中
for k,v in user_0.items():
     print('\n'+k+': '+v)
     print(v+': '+v)
for k in user_0.keys():
    print(k)
# 默认浏览所有的键
for k in user_0:
    print(k)
# 按顺序遍历所有的键
favorite_languages = { 
 'jen': 'python', 
 'sarah': 'c', 
 'edward': 'ruby', 
 'phil': 'python', 
 } 
for name in sorted(favorite_languages.keys()):
    print('最喜欢'+name)
print(user_0.keys())
print(user_0.items())