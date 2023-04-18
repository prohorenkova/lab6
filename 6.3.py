import random

students = {"Смирнова", "Журавлёв", "Кашин", "Соколова", "Васильева", "Морозов", "Миронов", "Зорин", "Симанова",
            "Чугунова"}
languages = {"Русский", "Английский", "Корейский", "Испанский", "Китайский"}

s_l = {}

for st in students:
    n = random.randint(1, 3)
    s_l[st] = random.sample(list(languages), n)

unique_l = set()
for i in s_l:
    unique_l = unique_l.union(set(s_l[i]))


print("Языки которые знают студенты: ", sorted(unique_l), f" ({len(unique_l)})")

china = [i for i in s_l if "Китайский" in s_l[i]]
print("Студенты которые знают китайский язык: ", china)