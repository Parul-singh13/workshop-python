
#my_set.add(4)
#print(my_set)
#my_set.remove(4)
#print(my_set)
#my_set.discard(3)
#print(my_set)
#Find the union of two elements
#myset1={5,6,7}
#union=myset1.union(my_set)

#Find the intersection of two elements
my_set1 = {"a","b","c"}
my_set2 = {"c","d","e"}
intersection = my_set1.intersection(my_set2)
print(intersection)
my_set={1,2,3}  
my_set3={3,4,5}
inter = my_set.intersection(my_set3)
print(inter)
#Find the difference
differ=my_set1.difference(my_set2)
print(differ)
s1={1,2,3}
s2={2,3,4}
s3={3,4,5}
s4=s2.difference(s1)
print(s4)
s4=s2.symmetric_difference(s1)
print(s4)