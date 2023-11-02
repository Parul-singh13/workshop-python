dictictionary={0:10,1:20}
dictictionary[2]=30
print(dictictionary)
#question2
dic1={0:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)
#question3
color_dict={'red':'#FF0000', 'green':'#008000','black':'#000000','white':'#FFFFFF'}
sort=sorted(color_dict)
print(sort)

#q1
d={'x':10,'y':20,'z':30}
for key,value in d.items():
    print(f"{key}:{value}")
#q2
n=int(input("enter n "))
d2={x:x*x for x in range(1,n+1)}
print(d2)
#q3
d3={x:x**2 for x in range(1,16)}
print(d3)
#q4
c=0
my_dict={'data1':100,'data2':-54,'data3':247}
for value in d.values():
    c+=value
print(c)
print(sum(my_dict.values()))
color_dict1={}
x=color_dict.keys()
l_ist=[]
for i in x:
    l_ist.append(i)
l_ist1=sorted(l_ist)
for j in l_ist1:
    color_dict1[j]=color_dict[j]
print(color_dict) 
print(color_dict1)



