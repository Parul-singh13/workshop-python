my_dict={}
student={
    "name":'alice',"age":25,"grade":"A"
}
s=student.get("age")
print(s)
student["age"]=26
print(student)
for key,value in student.items():
    print(f"{key}:{value}")
for key in student.keys():
    print(f"{key}")
for value in student.values():
    print(f"{value}")
square={num:num**2 for num in range(1,6)}
print(square)
cube={num:num**3 for num in range(1,6)}
print(cube)
del student["age"]
print(student)
grade= student.get("grade","N/A")
print(grade)
phone=student.get("phone")
print(phone)
student["city"]="lucknow"
print(student)
get=student.get("city")
print(get)
get1=student.get("phoneno","not found")
print(get1)
