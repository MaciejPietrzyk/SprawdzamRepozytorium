numbers = [10, 20, 30, 40, 50]
print(numbers[0])
print(numbers[2])
print(numbers[-1])
numbers.append(60)
numbers.remove(30)
print(numbers[0])
print(numbers[2])
print(numbers[-1])

print(len(numbers))

temperatures = [18, 21, 19, 25, 30, 22, 17]

print(max(temperatures))
print(min(temperatures))
for temperature in temperatures:
     if temperature > 20:
        print(temperature)
print(sum(temperatures)/len(temperatures))

numbers = [22,11,22,66,34,1,5,3,22,74,67]
for number in numbers:
    if number > 10:
        print(number*33)

sales = [1200, 500, 3000, 800, 1500, 4500]
for sale in sales:
    print(f"tylko sprzedaz {sale}")
for sale in sales:
    if sale > 1000:
     print(f"powyzej 1000 {sale}")

scores = [45, 78, 91, 33, 67, 88, 52]
for score in scores:
    if score >= 90:
        print("Excelent")
    elif score >= 70:
        print("Good")
    elif score >= 50:
        print("Pass")
    else:
        print("Fail")