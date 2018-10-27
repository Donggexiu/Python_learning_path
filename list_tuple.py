edward = ['edward gumby',42]
john = ['John smith' ,50]
database = [edward,john]
print(database)
'''
python之中还有一种名为容器的的数据结构,容器基本上是包含其他对象的任意对象.序列(例如元祖和列表)和映射(例如字典)
是两类主要的容器,序列中的每个元素都有自己的编号,而映射中的每个元素则有一个名字(也称为键).
'''
#所有序列类型进行某些特定的操作,这些操作包括:索引(indexing),分片(sliceing),加(add),乘(mutiplying)以及检查某个元素是否
#属于序列成员.除此之外,python还有计算序列长度,找出最大元素和最小元素的内建函数.
'''索引'''
#最后一个元素的索引是-1 字符串就是一个由字符组成的序列,索引0指向第一个元素,
greeting = 'hello'
print(greeting[0])
print(greeting[-1])
'''list函数:因为字符串不能像列表一样被修改.'''
print(list('hello'))#list函数适用于所有类型的序列.而不只是字符串
#提示:可以用下面的表达式将一个由字符(如前面代码中的)组成的列表转成字符串:'.'join(somelist)
#在这里,somelist是需要转换的列表.
'''---list的method--'''
#改变列表:元素赋值
x = [1,1,1]
x[1] = 2
print(x)#attention:不能为一个位置不存在的元素进行赋值
#删除元素
y = [1,2,3,4]
del y[2]
print(y)
#del语句还能用于删除其他元素.它可以用于字典元素,甚至是其他变量的删除操作
#3.分片赋值
name = list('deng')
print(name)
name[2:] = list('ar')
print(name)
#使用分片赋值是,可以使用与原序列不等长的序列将分片替换:
list_1 = list('perl')
list_1[1:] = list('ython')
print(list_1)
#分片赋值还可以在不需要替换任何原有元素的情况下插入新的元素.
numbers = [1,5]
numbers [1:1] = [2,3,4]
print(numbers)
numbers[1:4] = []
print(numbers)
#列表方法(method)
#append方法和其他方法有些类似,只是在恰当位置修改原来的列表.它不仅简单的返回一个修改过的新列表,
#而是直接修改原来的列表.
list2 = [1,2,3]
list2.append(4)
print(list2)
#count(统计某个元素在列表中出现的次数)
list_3 = [1,2,2,3,4,4,5,5,]
print(list_3.count(2))
x = [[1,2],1,[2,1,[1,2,3]]]
print(x.count(1))
print(x.count([1,2]))
#extend(可以在列表的末尾一次性追加另一个序列中的多个值.换句话说,可以用新列表扩展原有的表)
a = [1,2,3]
b = [4,5,6]
a.extend(b)
print(a)#extend修改了被扩展的序列(在这个例子中,就是a).而原始的连接操作不然
#index从列表中找出某个值第一个匹配项的索引位置
list_4 = [1,2,'python',4,5,6]
print(list_4.index('python'))
#insert用于将对象插入到列表中insert( index, p_object)
list_5 = [1,2,3,45]
list_5.insert(3,'ceshi')
print(list_5)
#pop会移除列表中的一个元素,并且返回该元素的值:pop方法是唯一一个既能修改列表又返回元素值(除NONE)的列表方法
x = [1,2,3]
print(x.pop())
print(x)
#reverse将列表中的元素反向存放()
y = [1,2,3]
print(y.reverse())
#sort用于在原位置对列表进行排序.在'原位置排序'意味着改变原来的列表,从而让其中的元素能按一定的顺序排列
#sort方法修改了x却返回了空值,
x = [4,6,7,1,9]
x.sort()
print(x)
numbers_1 = [3,1,8,5]
numbers_1.sort(reverse=True)
print(numbers_1)

print('---tuple---')
'''tuple以一个序列作为参数并把它转换为元祖.如果参数就是元祖,那么该参数就会原样返回"'''
print(tuple([1,2,3]))
tuple_1 = 1,2,3
print(tuple_1)


