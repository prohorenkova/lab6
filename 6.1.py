countries_dict = {"Австрия": "Вена", "Алжир": "Алжир", "Белоруссия": "Минск", "Германия": "Берлин",
                  "Ирландия": "Дублин", "Тайвань": "Тайпей", "Нидерладны": "Амстердам",
                  "Франция": "Париж", "Конго": "Браззавиль", "Филиппины": "Манила", "Чехия": "Прага",
                  "Албания": "Тирана", "Бутан": "Тхимпху",
                  "Гаити": "Порт-о-Пренс", "Сербия": "Белград"}

print(countries_dict)
print(countries_dict["Конго"])
for key in sorted(countries_dict):
    print(key, " - ", countries_dict[key])
