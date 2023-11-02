import json
import csv
import os
def igrok_choice(prompt, options):
    print(prompt)
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
    while True:
        try:
            choice = int(input("Ваш выбор: "))
            if choice < 1 or choice > len(options):
                print("Пожалуйста, выберите допустимый вариант.")
            else:
                return choice
        except ValueError:
            print("Пожалуйста, введите число.")

def input_choice(choice, person):
    if choice == 1:
        print("\"Погода - супер, Экзамены сданы..\"")
    elif choice == 2:
        print("\"Нет, я все-таки симпатичная. Пусть и немного уставшая.\"")

def gg(person):
    print(person)

def delete_save():
    if os.path.exists("person.json"):
        os.remove("person.json")
    else:
        print("Файл не существует")

def save_to_csv(person):
    csv_columns = ['Имя', 'Стойкость', 'Дипломатия']
    csv_file = "person.csv"
    try:
        with open(csv_file, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns, delimiter=';')

            if csvfile.tell() == 0:
                writer.writeheader()
            writer.writerow(person)
    except IOError:
            print("I/O error")
def game():
    print("Добро пожаловать в игру-новеллу!")

    name = input("Введите имя главной героини: ")

    person = {
        "Имя": name,
        "Стойкость": 0,
        "Дипломатия": 0
    }
    name = person['Имя']


    with open('person.json','w') as file:
        json.dump(person, file, indent=4)
    with open('person.json','r') as file:
        person = json.load(file)
    print(person)

    print(
        "Вам предстоит сделать выбор. Выбирайте с умом, ведь каждый выбор повлияет на историю, в той или иной степени.")

    print(f"\n{name}: \"Вот и закончился учебный год\"\n")

    choice = igrok_choice("\"Свобода! Каникулы!\"",
                         ['Выглянуть в окно', 'Посмотреть в зеркало'])
    input_choice(choice, person)

    print(f"\n{name}: \"Поверить не могу, что не нужно будет рано вставать. Высплюсь, наконец..\"\n")

    print("Настя: \"Кто как. Это ты все сдала. А у меня еще хвосты.\"\n")

    print(f"{name}: \"Беда. Но диплом МПТ за красивые глаза не дают.\"\n")

    print("Настя: \"А жаль. Кстати, мы идем сегодня на вечеринку в честь окончания курса?\"\n")

    choice = igrok_choice(f"\n{name}: \"Ну..\"",
                         ['Конечно же согласиться', 'Усомниться, будет ли там весело'])
    if choice == 1:
        print(f"{name}: \"Почему бы и не пойти? Попрощаться с одногруппниками надо. Правда ведь?\"\n")
        print("Настя: \"Да. Многие уедут из общаги.\"\n")
    else:
        print(f"{name}: \"Даже не знаю.. В прошлый раз было скучно. Вряд ли теперь будет иначе\"\n")
        print("Настя: \"Эй! Ты что хочешь оставить меня одну?\"\n")

    print("Тук-тук\n")

    print("Настя: \"Я открою.\"\n")

    print("Эдик: \"Привет, девочки! Как настроение?\"\n")

    print("Настя: \"Эдик? Свали из женского крыла.\"\n")

    print(f"Эдик: \"Вообще-то я по делу, {name}, тебе посылка.\"\n")

    print(f"{name}: \"От кого?\"\n")

    print("Эдик: \"Без понятия.\"\n")

    print(f"{name} взяла посылку и отошла к окну.\n")

    choice = igrok_choice(f"{name}: \"Странно..\"",
                         ['Потрясти посылку', 'Прощупать посылку'])
    if choice == 1:
        print("...\nОчень легкая, но внутри точно что-то есть)\n")
    else:
        print("...\nПохоже, полупустая картонная коробка.\n")

    print(f"{name}: \"Интересно, кто прислал?\"\n")

    print(
        "...\nНебольшая коробка была завернута в обычную почтовую бумагу. Но ни штемпелей, ни имени отправителя не было.\n")

    print(f"{name} разорвала бумагу и открыла коробку.\n")

    print("Внутри была открытка и маска.\n")

    print(
        f"{name}: \"Приглашение на маскарад.. вампиров?! Что за чушь? Форма одежды любая. Вход при наличии маски.. И адрес.\"\n")

    print(f"Настя: \"{name}, что там? От кого?\"\n")

    print(f"{name}: \"Посмотри сама\"\n")

    print("Настя: \"Забавно.. Но это же сегодня вечером!\"\n")

    choice = igrok_choice(
         f"{name}:\"Да, думаю съездить туда.\"\n  Эдик: \"Стоп, стоп! {name}, ты решила слиться? Оставайся с нами. Тебе многие будут рады.\"\n ...\n Парень обнял {name} за плечи,\n Подсказка: Некоторые решения меняют характер {name}, \n Одни повышают её  👊Стойкость - силу духа, твёрдость характера. \n Другие 📚 Дипломатию -умение договориться, обаяние и рассудительность. \n Выбирайте то, что подходит именно вам.",
        ['Резко сбросить руку нахала', 'Отойти, не провоцируя конфликт'])

    if choice == 1:
        print(f"Пошел вон. Что за хамство? В следующий раз руку отгрызу. (+1 Стойкость)\n")


        with open('person.json', 'r') as file:
            person = json.load(file)
        person["Стойкость"] = 1
        with open('person.json', 'w') as file:
            json.dump(person, file, indent=4)

    else:
        print(f"Не приставай. Это лишнее. Так мы можем поругаться (+1 Дипломатия)\n")


        with open('person.json', 'r') as file:
            person = json.load(file)
        person["Дипломатия"] = 1
        with open('person.json', 'w') as file:
            json.dump(person, file, indent=4)

    print("Эдик уходит из комнаты\n")

    print("Настя: \"Ты уверена, что хочешь туда поехать? Приглашение неизвестно от кого.\"\n")

    choice = igrok_choice(
        f"{name}: \"Хмм..\"",
        ['Ты права, лучше проведу время с вами.', 'Да, я решила, что поеду.'])

    if choice == 1:
        print(f"\nВечером {name} пошла на вечеринку со своими одногруппниками и хорошо провела время.")
    else:
        print(
            f"\nВечером {name} вызвала такси и поехала по указанному в письме адресу. По приезде её встретил высокий мужчина в черной маске и ударил по голове. {name} отключилась.")

    with open('person.json', 'r') as file:
        person = json.load(file)
    print(person)

    with open('person.json', 'r') as file:
        person = json.load(file)
    save_to_csv(person)
    delete_save()

game()

