users = [
    {"id": 1, "name": "Ania", "age": 25, "city": "Warszawa"},
    {"id": 2, "name": "Kamil", "age": 17, "city": "Kraków"},
    {"id": 3, "name": "Ola", "age": 31, "city": "Warszawa"},
    {"id": 4, "name": "Piotr", "age": 22, "city": "Gdańsk"},
    {"id": 5, "name": "Ewa", "age": 16, "city": "Kraków"}
]

print("----IMIONA----")

for user in users:
    print(user["name"])

print("----PEŁNOLETNI----")

for user in users:
    if user["age"] > 18:
        print(user["name"])

print("----LICZNIK----")

print(len(users))

print("----NOWA LISTA----")

adults = []

for adult in users:
    if adult["age"] > 18:
        adults.append(adult)

for adult in adults:
    print(adult["name"])

print("----ŚREDNI WIEK----")

total_age = 0

for user in users:
    total_age = total_age + user["age"]

average_age = total_age /len(users)
print(average_age)

print("----KRAKOWIAKI----")

def get_users_from_city(users,city):

    results = []
    for user in users:
        if user['city'] == city:
            results.append({
                "name": user["name"],
                "city": user["city"]
            })

    return results

print(get_users_from_city(users,"Warszawa" ))
