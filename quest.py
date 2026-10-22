# Текстовый квест "Тёмный замок" — расширенная версия
# Вся логика построена на if / elif / else, без функций и циклов.
# Модуль random нужен только для броска кубика.
import random

print("=============================")
print("        ТЁМНЫЙ ЗАМОК")
print("=============================")
name = input("Как тебя зовут, путник? ")

if name == "":
    name = "Безымянный"
    print("Ты не назвал имени, будешь зваться Безымянный.")
else:
    print("Приветствую, " + name + "!")

health = 100
gold = 0
alive = True
done = 0
has_sword = False
has_torch = False
has_shield = False
has_map = False
has_key = False
has_potion = False
has_amulet = False

print()
print("Перед тобой старый замок. Выбери стартовое снаряжение:")
print("1 - Меч (бонус в бою)")
print("2 - Факел (бонус в темноте)")
print("3 - Щит (защита от ловушек)")
start = input("Твой выбор: ")

if start == "1":
    has_sword = True
    print("Ты берёшь меч.")
elif start == "2":
    has_torch = True
    print("Ты берёшь факел.")
elif start == "3":
    has_shield = True
    print("Ты берёшь щит.")
else:
    print("Ты не выбрал снаряжение и идёшь с пустыми руками.")

# ---------- Глава 1: Ворота замка ----------
if alive:
    print()
    print("=== Глава 1 из 8: Ворота замка ===")
    print("Ты стоишь перед тяжёлыми воротами замка. Ночь, дует холодный ветер.")
    print("1 - Постучать в ворота")
    print("2 - Перелезть через стену")
    print("3 - Обойти замок вокруг")
    c = input("Твой выбор: ")

    if c == "1":
        print("Ты стучишь в тяжёлые ворота.")
        if has_torch:
            print("Свет факела виден издалека, и стражник быстро отвечает.")
            bonus = 1
        else:
            print("В темноте тебя долго не замечают.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("Стражник узнаёт в тебе героя и дарит кошелёк.")
            gold = gold + 20
            print("Ты получаешь золота: 20")
        elif roll >= 3:
            print("Стражник пускает тебя без лишних вопросов.")
            gold = gold + 5
            print("Ты получаешь золота: 5")
        else:
            print("Стражник бросает в тебя камень.")
            health = health - 15
            print("Ты теряешь здоровья: 15")

    elif c == "2":
        print("Ты подходишь к высокой стене.")
        if has_map:
            print("По карте ты находишь удобное место для подъёма.")
            bonus = 1
        else:
            print("Ты лезешь наугад по скользким камням.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("Наверху ты находишь забытый мешок с монетами.")
            gold = gold + 30
            print("Ты получаешь золота: 30")
        elif roll >= 3:
            print("Ты благополучно спускаешься во двор.")
        else:
            print("Ты срываешься и падаешь вниз.")
            health = health - 20
            print("Ты теряешь здоровья: 20")

    elif c == "3":
        print("Ты идёшь вдоль глубокого рва.")
        if has_torch:
            print("Факел освещает узкую тропу.")
            bonus = 1
        else:
            print("Тропа почти не видна в темноте.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("Ты находишь в траве старую карту!")
            has_map = True
            print("Ты забираешь карту себе.")
        elif roll >= 3:
            print("Ты обходишь замок и возвращаешься к воротам.")
        else:
            print("Ты оступаешься и падаешь в ров.")
            health = health - 10
            print("Ты теряешь здоровья: 10")

    else:
        print("Ты замешкался, и время ушло зря. Тебя задела ловушка.")
        health = health - 10

    if health <= 0:
        print("Силы покидают тебя. Ты погибаешь в замке...")
        alive = False
    else:
        done = done + 1
        if health > 100:
            health = 100
        print("Здоровье: " + str(health) + " | Золото: " + str(gold))
        if health < 40:
            if has_potion:
                print("Здоровье низкое. Выпить зелье?")
                print("1 - Да")
                print("2 - Нет")
                d = input("Твой выбор: ")
                if d == "1":
                    health = health + 40
                    has_potion = False
                    print("Ты пьёшь зелье. Здоровье: " + str(health))
                elif d == "2":
                    print("Ты бережёшь зелье на потом.")
                else:
                    print("Ты не понял вопроса и убираешь зелье обратно.")
            else:
                print("Здоровье низкое, а зелья нет. Будь осторожен.")

# ---------- Глава 2: Главный зал ----------
if alive:
    print()
    print("=== Глава 2 из 8: Главный зал ===")
    print("Внутри замка огромный зал с рваными гобеленами и холодным камином.")
    print("1 - Осмотреть камин")
    print("2 - Снять гобелен со стены")
    print("3 - Пройти к лестнице")
    c = input("Твой выбор: ")

    if c == "1":
        print("Ты подходишь к камину.")
        if has_torch:
            print("Ты светишь факелом в дымоход.")
            bonus = 1
        else:
            print("В камине слишком темно.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("В золе лежит зелье лечения!")
            has_potion = True
            print("Ты забираешь зелье.")
        elif roll >= 3:
            print("Ты находишь несколько обгоревших монет.")
            gold = gold + 10
            print("Ты получаешь золота: 10")
        else:
            print("Из дымохода сыплются горящие угли.")
            health = health - 15
            print("Ты теряешь здоровья: 15")

    elif c == "2":
        print("Ты хватаешься за край гобелена.")
        if has_sword:
            print("Ты срезаешь гобелен мечом.")
            bonus = 1
        else:
            print("Гобелен тяжёлый, и ты рвёшь его руками.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("За гобеленом спрятан тайник с золотом!")
            gold = gold + 40
            print("Ты получаешь золота: 40")
        elif roll >= 3:
            print("За гобеленом только пыльная стена.")
        else:
            print("Гобелен падает и придавливает тебя.")
            health = health - 20
            print("Ты теряешь здоровья: 20")

    elif c == "3":
        print("Ты идёшь через зал к лестнице.")
        if has_shield:
            print("Щит прикрывает тебя от стрел-ловушек.")
            bonus = 1
        else:
            print("Ты идёшь без прикрытия.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("Ты находишь безопасный путь и ключ на перилах.")
            has_key = True
            print("Ты берёшь ключ.")
        elif roll >= 3:
            print("Ты спокойно доходишь до лестницы.")
            gold = gold + 5
            print("Ты получаешь золота: 5")
        else:
            print("Стрела-ловушка задевает твою руку.")
            health = health - 15
            print("Ты теряешь здоровья: 15")

    else:
        print("Ты замешкался, и время ушло зря. Тебя задела ловушка.")
        health = health - 10

    if health <= 0:
        print("Силы покидают тебя. Ты погибаешь в замке...")
        alive = False
    else:
        done = done + 1
        if health > 100:
            health = 100
        print("Здоровье: " + str(health) + " | Золото: " + str(gold))
        if health < 40:
            if has_potion:
                print("Здоровье низкое. Выпить зелье?")
                print("1 - Да")
                print("2 - Нет")
                d = input("Твой выбор: ")
                if d == "1":
                    health = health + 40
                    has_potion = False
                    print("Ты пьёшь зелье. Здоровье: " + str(health))
                elif d == "2":
                    print("Ты бережёшь зелье на потом.")
                else:
                    print("Ты не понял вопроса и убираешь зелье обратно.")
            else:
                print("Здоровье низкое, а зелья нет. Будь осторожен.")

# ---------- Глава 3: Библиотека ----------
if alive:
    print()
    print("=== Глава 3 из 8: Библиотека ===")
    print("Ты входишь в библиотеку. Пыльные книги стоят до самого потолка.")
    print("1 - Читать старую книгу")
    print("2 - Искать тайник за полками")
    print("3 - Зажечь свечи")
    c = input("Твой выбор: ")

    if c == "1":
        print("Ты открываешь толстый том.")
        if has_map:
            print("Карта помогает найти нужную страницу.")
            bonus = 1
        else:
            print("Ты листаешь книги наугад.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("В книге спрятан план тайного хода и золото!")
            gold = gold + 35
            print("Ты получаешь золота: 35")
        elif roll >= 3:
            print("Ты узнаёшь пару полезных фактов о замке.")
            gold = gold + 5
            print("Ты получаешь золота: 5")
        else:
            print("Книга проклята и обжигает руки.")
            health = health - 15
            print("Ты теряешь здоровья: 15")

    elif c == "2":
        print("Ты ощупываешь деревянные полки.")
        if has_key:
            print("Ключ подходит к замочной скважине.")
            bonus = 1
        else:
            print("Замочная скважина закрыта, придётся взламывать.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("Тайник открыт, внутри лежит амулет защиты!")
            has_amulet = True
            print("Ты надеваешь амулет.")
        elif roll >= 3:
            print("Внутри лежат старые монеты.")
            gold = gold + 20
            print("Ты получаешь золота: 20")
        else:
            print("Тяжёлая полка падает на тебя.")
            health = health - 20
            print("Ты теряешь здоровья: 20")

    elif c == "3":
        print("Ты подходишь к подсвечникам.")
        if has_torch:
            print("Ты легко зажигаешь свечи от факела.")
            bonus = 1
        else:
            print("У тебя нет огня, и ты долго ищешь способ зажечь свечи.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("Свет открывает надпись на полу, а под плиткой лежит золото.")
            gold = gold + 25
            print("Ты получаешь золота: 25")
        elif roll >= 3:
            print("В библиотеке становится светлее.")
        else:
            print("Огонь перекидывается на занавеску.")
            health = health - 15
            print("Ты теряешь здоровья: 15")

    else:
        print("Ты замешкался, и время ушло зря. Тебя задела ловушка.")
        health = health - 10

    if health <= 0:
        print("Силы покидают тебя. Ты погибаешь в замке...")
        alive = False
    else:
        done = done + 1
        if health > 100:
            health = 100
        print("Здоровье: " + str(health) + " | Золото: " + str(gold))
        if health < 40:
            if has_potion:
                print("Здоровье низкое. Выпить зелье?")
                print("1 - Да")
                print("2 - Нет")
                d = input("Твой выбор: ")
                if d == "1":
                    health = health + 40
                    has_potion = False
                    print("Ты пьёшь зелье. Здоровье: " + str(health))
                elif d == "2":
                    print("Ты бережёшь зелье на потом.")
                else:
                    print("Ты не понял вопроса и убираешь зелье обратно.")
            else:
                print("Здоровье низкое, а зелья нет. Будь осторожен.")

# ---------- Глава 4: Подвал ----------
if alive:
    print()
    print("=== Глава 4 из 8: Подвал ===")
    print("Лестница ведёт в сырой подвал. Слышно, как капает вода.")
    print("1 - Открыть бочки")
    print("2 - Пройти по узкому мосту")
    print("3 - Заглянуть в тёмную нишу")
    c = input("Твой выбор: ")

    if c == "1":
        print("Ты подходишь к ряду бочек.")
        if has_sword:
            print("Ты поддеваешь крышку мечом.")
            bonus = 1
        else:
            print("Ты открываешь бочки голыми руками.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("В одной из бочек монеты вместо вина!")
            gold = gold + 45
            print("Ты получаешь золота: 45")
        elif roll >= 3:
            print("В бочке остатки старого вина.")
            gold = gold + 5
            print("Ты получаешь золота: 5")
        else:
            print("Из бочки вырывается едкий пар.")
            health = health - 15
            print("Ты теряешь здоровья: 15")

    elif c == "2":
        print("Ты ступаешь на мост над чёрной водой.")
        if has_shield:
            print("Щит помогает держать равновесие.")
            bonus = 1
        else:
            print("Мост сильно шатается под ногами.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("На другой стороне ты находишь зелье лечения.")
            has_potion = True
            print("Ты прячешь зелье в сумку.")
        elif roll >= 3:
            print("Ты благополучно переходишь на другую сторону.")
            gold = gold + 10
            print("Ты получаешь золота: 10")
        else:
            print("Ты соскальзываешь и падаешь в холодную воду.")
            health = health - 20
            print("Ты теряешь здоровья: 20")

    elif c == "3":
        print("Ты склоняешься над нишей в стене.")
        if has_torch:
            print("Факел освещает старый сундук.")
            bonus = 1
        else:
            print("Ты шаришь рукой в темноте.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("Сундук доверху набит золотом!")
            gold = gold + 50
            print("Ты получаешь золота: 50")
        elif roll >= 3:
            print("В нише лежит пара монет.")
            gold = gold + 10
            print("Ты получаешь золота: 10")
        else:
            print("Из ниши выскакивает крыса и кусает тебя.")
            health = health - 10
            print("Ты теряешь здоровья: 10")

    else:
        print("Ты замешкался, и время ушло зря. Тебя задела ловушка.")
        health = health - 10

    if health <= 0:
        print("Силы покидают тебя. Ты погибаешь в замке...")
        alive = False
    else:
        done = done + 1
        if health > 100:
            health = 100
        print("Здоровье: " + str(health) + " | Золото: " + str(gold))
        if health < 40:
            if has_potion:
                print("Здоровье низкое. Выпить зелье?")
                print("1 - Да")
                print("2 - Нет")
                d = input("Твой выбор: ")
                if d == "1":
                    health = health + 40
                    has_potion = False
                    print("Ты пьёшь зелье. Здоровье: " + str(health))
                elif d == "2":
                    print("Ты бережёшь зелье на потом.")
                else:
                    print("Ты не понял вопроса и убираешь зелье обратно.")
            else:
                print("Здоровье низкое, а зелья нет. Будь осторожен.")

# ---------- Глава 5: Оружейная ----------
if alive:
    print()
    print("=== Глава 5 из 8: Оружейная ===")
    print("За железной дверью находится оружейная, полная ржавых доспехов.")
    print("1 - Взять меч со стены")
    print("2 - Примерить доспехи")
    print("3 - Обыскать стойки с копьями")
    c = input("Твой выбор: ")

    if c == "1":
        print("Ты тянешься к висящему мечу.")
        if has_amulet:
            print("Амулет слабо светится, и меч не кажется ржавым.")
            bonus = 1
        else:
            print("Меч ржавый, но всё ещё тяжёлый.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("Это зачарованный клинок!")
            has_sword = True
            print("Теперь у тебя есть меч.")
        elif roll >= 3:
            print("Ты не берёшь меч, но находишь пару монет в подставке.")
            gold = gold + 10
            print("Ты получаешь золота: 10")
        else:
            print("Меч падает тебе на ногу.")
            health = health - 15
            print("Ты теряешь здоровья: 15")

    elif c == "2":
        print("Ты подходишь к стойке с доспехами.")
        if has_key:
            print("Ключ открывает витрину с лучшими доспехами.")
            bonus = 1
        else:
            print("Витрина заперта, и ты берёшь то, что осталось.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("Доспехи сидят идеально, а в шлеме спрятаны монеты.")
            gold = gold + 30
            print("Ты получаешь золота: 30")
        elif roll >= 3:
            print("Доспехи тяжёлые, но тебе подходят.")
        else:
            print("Доспехи рассыпаются и ранят тебя.")
            health = health - 15
            print("Ты теряешь здоровья: 15")

    elif c == "3":
        print("Ты проверяешь стойки одну за другой.")
        if has_map:
            print("Карта показывает, где искать тайник.")
            bonus = 1
        else:
            print("Ты просто ощупываешь все стойки.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("Ты находишь крепкий щит!")
            has_shield = True
            print("Ты берёшь щит.")
        elif roll >= 3:
            print("Ты находишь несколько монет.")
            gold = gold + 15
            print("Ты получаешь золота: 15")
        else:
            print("Копьё соскальзывает и царапает тебя.")
            health = health - 10
            print("Ты теряешь здоровья: 10")

    else:
        print("Ты замешкался, и время ушло зря. Тебя задела ловушка.")
        health = health - 10

    if health <= 0:
        print("Силы покидают тебя. Ты погибаешь в замке...")
        alive = False
    else:
        done = done + 1
        if health > 100:
            health = 100
        print("Здоровье: " + str(health) + " | Золото: " + str(gold))
        if health < 40:
            if has_potion:
                print("Здоровье низкое. Выпить зелье?")
                print("1 - Да")
                print("2 - Нет")
                d = input("Твой выбор: ")
                if d == "1":
                    health = health + 40
                    has_potion = False
                    print("Ты пьёшь зелье. Здоровье: " + str(health))
                elif d == "2":
                    print("Ты бережёшь зелье на потом.")
                else:
                    print("Ты не понял вопроса и убираешь зелье обратно.")
            else:
                print("Здоровье низкое, а зелья нет. Будь осторожен.")

# ---------- Глава 6: Башня ----------
if alive:
    print()
    print("=== Глава 6 из 8: Башня ===")
    print("Винтовая лестница ведёт вверх. На вершине башни горит странный свет.")
    print("1 - Подняться быстро")
    print("2 - Идти медленно вдоль стены")
    print("3 - Позвать того, кто наверху")
    c = input("Твой выбор: ")

    if c == "1":
        print("Ты бежишь вверх по ступеням.")
        if has_potion:
            print("Ты уверенно идёшь, зная, что у тебя есть зелье.")
            bonus = 1
        else:
            print("Ты боишься устать и идёшь с оглядкой.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("На вершине лежит мешок золота.")
            gold = gold + 40
            print("Ты получаешь золота: 40")
        elif roll >= 3:
            print("Ты добираешься до верха и отдыхаешь.")
            gold = gold + 5
            print("Ты получаешь золота: 5")
        else:
            print("Ступени обрушиваются под ногами.")
            health = health - 25
            print("Ты теряешь здоровья: 25")

    elif c == "2":
        print("Ты осторожно поднимаешься по лестнице.")
        if has_shield:
            print("Щит защищает от падающих сверху камней.")
            bonus = 1
        else:
            print("Камни падают прямо на тебя.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("Ты замечаешь потайную дверь с сокровищами.")
            gold = gold + 30
            print("Ты получаешь золота: 30")
        elif roll >= 3:
            print("Ты спокойно поднимаешься наверх.")
            gold = gold + 10
            print("Ты получаешь золота: 10")
        else:
            print("Камень попадает тебе в плечо.")
            health = health - 15
            print("Ты теряешь здоровья: 15")

    elif c == "3":
        print("Ты громко кричишь вверх.")
        if has_amulet:
            print("Амулет защищает тебя от злых духов.")
            bonus = 1
        else:
            print("Эхо разносит твой голос по башне.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("Добрый призрак дарит тебе зелье.")
            has_potion = True
            print("Ты забираешь зелье.")
        elif roll >= 3:
            print("Ответа нет, но ты слышишь тихий шорох.")
        else:
            print("Злой дух проклинает тебя.")
            health = health - 20
            print("Ты теряешь здоровья: 20")

    else:
        print("Ты замешкался, и время ушло зря. Тебя задела ловушка.")
        health = health - 10

    if health <= 0:
        print("Силы покидают тебя. Ты погибаешь в замке...")
        alive = False
    else:
        done = done + 1
        if health > 100:
            health = 100
        print("Здоровье: " + str(health) + " | Золото: " + str(gold))
        if health < 40:
            if has_potion:
                print("Здоровье низкое. Выпить зелье?")
                print("1 - Да")
                print("2 - Нет")
                d = input("Твой выбор: ")
                if d == "1":
                    health = health + 40
                    has_potion = False
                    print("Ты пьёшь зелье. Здоровье: " + str(health))
                elif d == "2":
                    print("Ты бережёшь зелье на потом.")
                else:
                    print("Ты не понял вопроса и убираешь зелье обратно.")
            else:
                print("Здоровье низкое, а зелья нет. Будь осторожен.")

# ---------- Глава 7: Внутренний двор ----------
if alive:
    print()
    print("=== Глава 7 из 8: Внутренний двор ===")
    print("Ты выходишь во внутренний двор, где разрослись колючие кусты.")
    print("1 - Идти по тропинке")
    print("2 - Срезать путь через кусты")
    print("3 - Искать колодец")
    c = input("Твой выбор: ")

    if c == "1":
        print("Ты идёшь по узкой тропинке.")
        if has_map:
            print("Карта показывает безопасный путь.")
            bonus = 1
        else:
            print("Тропинка то и дело разветвляется.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("В центре сада стоит фонтан с золотыми монетами.")
            gold = gold + 35
            print("Ты получаешь золота: 35")
        elif roll >= 3:
            print("Ты проходишь сад без приключений.")
            gold = gold + 5
            print("Ты получаешь золота: 5")
        else:
            print("Колючие лозы хватают тебя за ноги.")
            health = health - 15
            print("Ты теряешь здоровья: 15")

    elif c == "2":
        print("Ты решительно идёшь через заросли.")
        if has_sword:
            print("Ты прорубаешь дорогу мечом.")
            bonus = 1
        else:
            print("Ты продираешься сквозь колючки.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("За кустами спрятан сундучок с золотом.")
            gold = gold + 30
            print("Ты получаешь золота: 30")
        elif roll >= 3:
            print("Ты выходишь на другую сторону сада.")
        else:
            print("Колючки сильно царапают тебя.")
            health = health - 20
            print("Ты теряешь здоровья: 20")

    elif c == "3":
        print("Ты идёшь на звук воды.")
        if has_torch:
            print("Факел освещает колодец.")
            bonus = 1
        else:
            print("Ты нащупываешь колодец в темноте.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("На дне блестит ключ!")
            has_key = True
            print("Ты достаёшь ключ.")
        elif roll >= 3:
            print("Ты находишь колодец, но в нём ничего нет.")
        else:
            print("Ты оступаешься у края и ударяешься.")
            health = health - 10
            print("Ты теряешь здоровья: 10")

    else:
        print("Ты замешкался, и время ушло зря. Тебя задела ловушка.")
        health = health - 10

    if health <= 0:
        print("Силы покидают тебя. Ты погибаешь в замке...")
        alive = False
    else:
        done = done + 1
        if health > 100:
            health = 100
        print("Здоровье: " + str(health) + " | Золото: " + str(gold))
        if health < 40:
            if has_potion:
                print("Здоровье низкое. Выпить зелье?")
                print("1 - Да")
                print("2 - Нет")
                d = input("Твой выбор: ")
                if d == "1":
                    health = health + 40
                    has_potion = False
                    print("Ты пьёшь зелье. Здоровье: " + str(health))
                elif d == "2":
                    print("Ты бережёшь зелье на потом.")
                else:
                    print("Ты не понял вопроса и убираешь зелье обратно.")
            else:
                print("Здоровье низкое, а зелья нет. Будь осторожен.")

# ---------- Глава 8: Тронный зал ----------
if alive:
    print()
    print("=== Глава 8 из 8: Тронный зал ===")
    print("Огромные двери ведут в тронный зал. На троне сидит Король-призрак.")
    print("1 - Сразиться с королём")
    print("2 - Договориться с королём")
    print("3 - Тихо украсть корону")
    c = input("Твой выбор: ")

    if c == "1":
        print("Ты бросаешься на призрака.")
        if has_sword:
            print("Меч светится в твоих руках.")
            bonus = 1
        else:
            print("У тебя нет настоящего оружия.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("Ты побеждаешь Короля-призрака и забираешь его сокровища!")
            gold = gold + 150
            print("Ты получаешь золота: 150")
        elif roll >= 3:
            print("Ты ранишь призрака, и он отступает, оставив монеты.")
            gold = gold + 50
            print("Ты получаешь золота: 50")
        else:
            print("Призрак бьёт тебя ледяной рукой.")
            health = health - 35
            print("Ты теряешь здоровья: 35")

    elif c == "2":
        print("Ты кланяешься и начинаешь говорить.")
        if has_amulet:
            print("Амулет заставляет призрака слушать.")
            bonus = 1
        else:
            print("Призрак не верит твоим словам.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("Король дарит тебе часть своей казны.")
            gold = gold + 120
            print("Ты получаешь золота: 120")
        elif roll >= 3:
            print("Король даёт тебе пару монет и отпускает.")
            gold = gold + 40
            print("Ты получаешь золота: 40")
        else:
            print("Король злится и проклинает тебя.")
            health = health - 30
            print("Ты теряешь здоровья: 30")

    elif c == "3":
        print("Ты крадёшься вдоль стены.")
        if has_key:
            print("Ключ открывает шкатулку с короной.")
            bonus = 1
        else:
            print("Ты вскрываешь шкатулку, и она скрипит.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("Ты уносишь корону, не разбудив призрака!")
            gold = gold + 130
            print("Ты получаешь золота: 130")
        elif roll >= 3:
            print("Ты хватаешь горсть драгоценностей.")
            gold = gold + 45
            print("Ты получаешь золота: 45")
        else:
            print("Призрак просыпается и бьёт тебя.")
            health = health - 30
            print("Ты теряешь здоровья: 30")

    else:
        print("Ты замешкался, и время ушло зря. Тебя задела ловушка.")
        health = health - 10

    if health <= 0:
        print("Силы покидают тебя. Ты погибаешь в замке...")
        alive = False
    else:
        done = done + 1
        if health > 100:
            health = 100
        print("Здоровье: " + str(health) + " | Золото: " + str(gold))
        if health < 40:
            if has_potion:
                print("Здоровье низкое. Выпить зелье?")
                print("1 - Да")
                print("2 - Нет")
                d = input("Твой выбор: ")
                if d == "1":
                    health = health + 40
                    has_potion = False
                    print("Ты пьёшь зелье. Здоровье: " + str(health))
                elif d == "2":
                    print("Ты бережёшь зелье на потом.")
                else:
                    print("Ты не понял вопроса и убираешь зелье обратно.")
            else:
                print("Здоровье низкое, а зелья нет. Будь осторожен.")

# ---------- Итоги ----------
print()
print("=============================")
print("           ИТОГИ")
print("=============================")
print("Игрок: " + name)
print("Пройдено глав: " + str(done) + " из 8")
print("Здоровье: " + str(health))
print("Золото: " + str(gold))

if gold >= 500:
    rank = "Легендарный охотник за сокровищами"
elif gold >= 350:
    rank = "Великий искатель приключений"
elif gold >= 200:
    rank = "Богатый путешественник"
elif gold >= 100:
    rank = "Опытный авантюрист"
elif gold >= 50:
    rank = "Скромный странник"
elif gold > 0:
    rank = "Бедный бродяга"
else:
    rank = "Неудачник"
print("Звание: " + rank)

if alive:
    if health >= 80:
        print("Статус: жив и полон сил")
    elif health >= 50:
        print("Статус: жив, но слегка потрёпан")
    elif health >= 20:
        print("Статус: тяжело ранен")
    else:
        print("Статус: едва жив")
else:
    print("Статус: погиб в замке")

print("Снаряжение:")
if has_sword:
    print("- Меч")
if has_torch:
    print("- Факел")
if has_shield:
    print("- Щит")
if has_map:
    print("- Карта")
if has_key:
    print("- Ключ")
if has_potion:
    print("- Зелье лечения")
if has_amulet:
    print("- Амулет защиты")
if not has_sword and not has_torch and not has_shield and not has_map and not has_key and not has_potion and not has_amulet:
    print("- Ничего")

if alive:
    if done >= 8:
        if gold >= 400:
            print("Ты прошёл весь замок и вышел с огромным богатством. О тебе сложат легенды!")
        elif gold >= 200:
            print("Ты прошёл весь замок и вернулся домой с хорошей добычей.")
        else:
            print("Ты прошёл весь замок, но добыча оказалась скромной.")
    else:
        print("Ты покинул замок раньше времени, но остался жив.")
else:
    if gold >= 100:
        print("Ты погиб, но успел собрать немало золота. Его найдут другие искатели.")
    elif gold > 0:
        print("Ты погиб, оставив в замке пару монет.")
    else:
        print("Ты погиб, не найдя ни одной монеты.")

print()
print("Достижения:")
achieved = False
if done >= 8:
    print("- Прошёл замок до конца")
    achieved = True
if gold >= 300:
    print("- Кладоискатель")
    achieved = True
if alive and health == 100:
    print("- Ни одной царапины")
    achieved = True
if has_sword and has_shield and has_amulet:
    print("- Полностью экипирован")
    achieved = True
if has_potion:
    print("- Сберёг зелье")
    achieved = True
if has_map and has_key:
    print("- Знаток замка")
    achieved = True
if not alive:
    print("- Пал смертью храбрых")
    achieved = True
if not achieved:
    print("- Пока нет достижений")

print()
print("Спасибо за игру, " + name + "!")
print("Запусти игру снова, чтобы попробовать другой путь.")
print("Конец.")
