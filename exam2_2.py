#输入两个集合setA和setB，分别输出他们的交集、并集和差集

setA=eval(input("请输入一个集合："))
setB=eval(input("再输入一个集合："))
print("交集:",setA & setB)
print("并集：",setA | setB)
print("setA-setB:",setA - setB)

