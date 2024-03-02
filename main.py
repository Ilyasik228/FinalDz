database = {
    "https://en.wikipedia.org/wiki/Islam": "Религия Ислам",
    "https://en.wikipedia.org/wiki/Muhammad": "Пророк Мухаммед",
    "https://en.wikipedia.org/wiki/Azerbaijan": "Страна Азербайджан",
}

query = input("Введите информацию для поиска: ")

# Поиск информации в базе данных и вывод результатов
found = False
for site, content in database.items():
    if query.lower() in content.lower():
        print(f"Информация найдена на сайте: {site}")
        found = True

if not found:
    print("Информация не найдена на сайтах в базе данных :(")