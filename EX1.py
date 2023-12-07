d = { "Иванов":20, "Сидоров":68, "Петров":26, "Смирнов":68}
d["Негодин"] = 50
d["Вакутагин"] = 100

mini = 102
maxi = -1
avg = sum(d.values())/len(d.keys())
print(f"Average mark: {round(avg, 2)}")
print("Список участников, балл которых выше среднего:")
for stud in d.keys():
    if d[stud] > avg:
        print(stud)
    if d[stud] > maxi:
        maxi = d[stud]
    if d[stud] < mini:
        mini = d[stud]
print("Максимальный балл:")
for stud in d.keys():
    if d[stud] == maxi:
        print(f"{stud}: {maxi}")
print("Минимальный балл:")
for stud in d.keys():
    if d[stud] == mini:
        print(f"{stud}: {mini}")