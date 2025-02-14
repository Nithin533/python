student = {
    "name" :"Nithin",
    "roll number":"1RUA24BCA0063",
    "class":"BCA",
}
for key in student:
  print(student[key])
student["Gender"]="Boy"
print(student["Gender"])
print()
x=str(input("Enter the key : "))
if x in student:
  print("Hi")
else:
    print("Bye")
