list = []
num = int(input("Enter number of elements : "))
for i in range(0, num):
    element = int(input("Enter the numbers : "))
    list.append(element)
print("Your input list : ")
print(list)
print("Positive numbers from list are : ")
for num in list:
    if num>=0:
       print(num,end = " ")
