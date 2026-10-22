# Текстовый квест "Тёмный замок" — расширенная версия
# Вся логика построена на if / elif / else, без функций и циклов.
# Модуль random нужен только для броска кубика.
import random

print("=============================")
print("        ТЁМНЫЙ ЗАМОК")
print("=============================")
print()
print("        |>>>          |>>>")
print("        |             |")
print("    _  _|_  _      _  _|_  _")
print("   | |_| |_| |    | |_| |_| |")
print("   \\  .  .  /      \\  .  .  /")
print("    \\      /________\\      /")
print("     | []  |  ____  |  [] |")
print("     |     | |    | |     |")
print("  ___|_____|_|____|_|_____|___")
print()
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
    print("=== Глава 1 из 22: Ворота замка ===")
    print("    ____________________")
    print("   /|                  |\\")
    print("  / |   ____    ____   | \\")
    print(" |  |  |    |  |    |  |  |")
    print(" |  |  | [] |  | [] |  |  |")
    print(" |  |  |    |  |    |  |  |")
    print(" |__|__|____|__|____|__|__|")
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
        print("Ты немного отдыхаешь и восстанавливаешь 5 здоровья.")
        health = health + 5
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
    print("=== Глава 2 из 22: Главный зал ===")
    print("        \\ | /")
    print("       -- * --")
    print("         /|\\")
    print("  ____________________")
    print(" |   ______           |")
    print(" |  |  ~~  |    [==]  |")
    print(" |  | ~~~~ |          |")
    print(" |__|______|__________|")
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
        print("Ты немного отдыхаешь и восстанавливаешь 5 здоровья.")
        health = health + 5
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
    print("=== Глава 3 из 22: Библиотека ===")
    print("  _______________________")
    print(" |[][][|][][][|][][][][]|")
    print(" |[][][|][][][|][][][][]|")
    print(" |_______________________|")
    print(" |[][][|][][][|][][][][]|")
    print(" |[][][|][][][|][][][][]|")
    print(" |_______________________|")
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
        print("Ты немного отдыхаешь и восстанавливаешь 5 здоровья.")
        health = health + 5
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
    print("=== Глава 4 из 22: Подвал ===")
    print("     _________")
    print("    /         \\")
    print("   |   _____   |")
    print("   |  |     |  |")
    print("   |  |  .  |  |")
    print("   |__|__:__|__|")
    print(" ~~~~~~~ : ~~~~~~~")
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
        print("Ты немного отдыхаешь и восстанавливаешь 5 здоровья.")
        health = health + 5
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
    print("=== Глава 5 из 22: Оружейная ===")
    print("      |            _____")
    print("     /|\\          /  |  \\")
    print("    / | \\        |   |   |")
    print("      |           \\  |  /")
    print("      |            \\ | /")
    print("   ___|___          \\|/")
    print("      |              V")
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
        print("Ты немного отдыхаешь и восстанавливаешь 5 здоровья.")
        health = health + 5
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
    print("=== Глава 6 из 22: Башня ===")
    print("       /\\")
    print("      /  \\")
    print("     /____\\")
    print("     | [] |")
    print("     |    |")
    print("     | [] |")
    print("     |    |")
    print("   __|____|__")
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
        print("Ты немного отдыхаешь и восстанавливаешь 5 здоровья.")
        health = health + 5
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
    print("=== Глава 7 из 22: Внутренний двор ===")
    print("    (@@@@)    (@@@)")
    print("  (@@@@@@@@) (@@@@@@)")
    print("   (@@@@@@)   (@@@@)")
    print("      ||        ||")
    print(" _____||________||_____")
    print(" ^^^ ^^^ ^^^ ^^^ ^^^ ^^")
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
        print("Ты немного отдыхаешь и восстанавливаешь 5 здоровья.")
        health = health + 5
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

# ---------- Глава 8: Конюшня ----------
if alive:
    print()
    print("=== Глава 8 из 22: Конюшня ===")
    print("       /^^^^^^^^^^\\")
    print("      /    HAY     \\")
    print("     /______________\\")
    print("     |  _        _  |")
    print("     | | |      | | |")
    print("     | |_|      |_| |")
    print("     |______________|")
    print("Ты заходишь в старую конюшню. Пахнет сеном и сыростью.")
    print("1 - Осмотреть стойла")
    print("2 - Забраться на сеновал")
    print("3 - Осмотреть сёдла")
    c = input("Твой выбор: ")

    if c == "1":
        print("Ты идёшь вдоль пустых стойл.")
        if has_torch:
            print("Факел освещает дальние углы.")
            bonus = 1
        else:
            print("В стойлах темно, и ты идёшь на ощупь.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("В сене спрятан кошелёк конюха.")
            gold = gold + 25
            print("Ты получаешь золота: 25")
        elif roll >= 3:
            print("Ты находишь в сене пару монет.")
            gold = gold + 5
            print("Ты получаешь золота: 5")
        else:
            print("Из сена выскакивает крыса и кусает тебя.")
            health = health - 10
            print("Ты теряешь здоровья: 10")

    elif c == "2":
        print("Ты поднимаешься по скрипучей лестнице.")
        if has_shield:
            print("Щит прикрывает тебя от падающих балок.")
            bonus = 1
        else:
            print("Балки скрипят над головой.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("Наверху лежит забытое зелье.")
            has_potion = True
            print("Ты забираешь зелье.")
        elif roll >= 3:
            print("Ты находишь на сеновале несколько монет.")
            gold = gold + 10
            print("Ты получаешь золота: 10")
        else:
            print("Лестница ломается под тобой.")
            health = health - 15
            print("Ты теряешь здоровья: 15")

    elif c == "3":
        print("Ты рассматриваешь старые сёдла.")
        if has_key:
            print("Ключ открывает шкаф со снаряжением.")
            bonus = 1
        else:
            print("Шкаф заперт, и ты шаришь по сёдлам.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("В седельной сумке лежит золото!")
            gold = gold + 30
            print("Ты получаешь золота: 30")
        elif roll >= 3:
            print("В сумке завалялись монеты.")
            gold = gold + 8
            print("Ты получаешь золота: 8")
        else:
            print("Старая подпруга хлещет тебя по лицу.")
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
        print("Ты немного отдыхаешь и восстанавливаешь 5 здоровья.")
        health = health + 5
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

# ---------- Глава 9: Кухня ----------
if alive:
    print()
    print("=== Глава 9 из 22: Кухня ===")
    print("      \\ | /")
    print("     ~~~~~~~")
    print("    (       )")
    print("    |  SUP  |")
    print("    (_______)")
    print("     /|   |\\")
    print("    /_|___|_\\")
    print("Ты попадаешь на огромную кухню с ржавыми котлами и крюками.")
    print("1 - Заглянуть в котёл")
    print("2 - Обыскать кладовую")
    print("3 - Осмотреть печь")
    c = input("Твой выбор: ")

    if c == "1":
        print("Ты подходишь к самому большому котлу.")
        if has_sword:
            print("Ты прощупываешь дно мечом.")
            bonus = 1
        else:
            print("Ты шаришь рукой по дну.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("На дне лежат золотые монеты!")
            gold = gold + 35
            print("Ты получаешь золота: 35")
        elif roll >= 3:
            print("На дне лежит немного монет.")
            gold = gold + 8
            print("Ты получаешь золота: 8")
        else:
            print("Из котла вырывается горячий пар.")
            health = health - 15
            print("Ты теряешь здоровья: 15")

    elif c == "2":
        print("Ты открываешь скрипучую дверь кладовой.")
        if has_torch:
            print("Факел освещает полки с припасами.")
            bonus = 1
        else:
            print("В кладовой совсем темно.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("За мешками ты находишь зелье лечения.")
            has_potion = True
            print("Ты кладёшь зелье в сумку.")
        elif roll >= 3:
            print("Ты находишь пару монет за мешками.")
            gold = gold + 10
            print("Ты получаешь золота: 10")
        else:
            print("С полки падает тяжёлая банка.")
            health = health - 15
            print("Ты теряешь здоровья: 15")

    elif c == "3":
        print("Ты подходишь к большой печи.")
        if has_amulet:
            print("Амулет защищает тебя от жара.")
            bonus = 1
        else:
            print("От печи идёт сильный жар.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("В золе спрятан сундучок с золотом.")
            gold = gold + 40
            print("Ты получаешь золота: 40")
        elif roll >= 3:
            print("В печи лежат остатки монет.")
            gold = gold + 10
            print("Ты получаешь золота: 10")
        else:
            print("Ты обжигаешь руку об угли.")
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
        print("Ты немного отдыхаешь и восстанавливаешь 5 здоровья.")
        health = health + 5
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

# ---------- Глава 10: Зал портретов ----------
if alive:
    print()
    print("=== Глава 10 из 22: Зал портретов ===")
    print("   ______   ______   ______")
    print("  |  __  | |  __  | |  __  |")
    print("  | (oo) | | (..) | | (^^) |")
    print("  |  \\/  | |  --  | |  vv  |")
    print("  |______| |______| |______|")
    print("Ты входишь в длинный зал, где со стен смотрят портреты древних владельцев замка.")
    print("1 - Рассмотреть портреты")
    print("2 - Снять самый большой портрет")
    print("3 - Поговорить с портретом")
    c = input("Твой выбор: ")

    if c == "1":
        print("Ты медленно идёшь вдоль картин.")
        if has_map:
            print("Карта помогает понять, какой портрет главный.")
            bonus = 1
        else:
            print("Все портреты кажутся одинаковыми.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("За одним портретом спрятан тайник с золотом.")
            gold = gold + 35
            print("Ты получаешь золота: 35")
        elif roll >= 3:
            print("Ты находишь монеты в раме одной из картин.")
            gold = gold + 10
            print("Ты получаешь золота: 10")
        else:
            print("Портрет падает на тебя.")
            health = health - 15
            print("Ты теряешь здоровья: 15")

    elif c == "2":
        print("Ты берёшься за раму самого большого портрета.")
        if has_sword:
            print("Ты поддеваешь раму мечом.")
            bonus = 1
        else:
            print("Рама тяжёлая, и ты тянешь её руками.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("За портретом лежит амулет.")
            has_amulet = True
            print("Ты надеваешь амулет.")
        elif roll >= 3:
            print("За портретом пыльная ниша с монетами.")
            gold = gold + 15
            print("Ты получаешь золота: 15")
        else:
            print("Портрет придавливает тебя.")
            health = health - 20
            print("Ты теряешь здоровья: 20")

    elif c == "3":
        print("Ты задаёшь вопрос портрету.")
        if has_amulet:
            print("Амулет помогает тебе услышать ответ.")
            bonus = 1
        else:
            print("Портрет молчит.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("Портрет шепчет, где лежит ключ.")
            has_key = True
            print("Ты находишь ключ там, где сказал портрет.")
        elif roll >= 3:
            print("Портрет рассказывает тебе старую легенду.")
        else:
            print("Портрет кричит так, что закладывает уши.")
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
        print("Ты немного отдыхаешь и восстанавливаешь 5 здоровья.")
        health = health + 5
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

# ---------- Глава 11: Оранжерея ----------
if alive:
    print()
    print("=== Глава 11 из 22: Оранжерея ===")
    print("     \\ | /      \\|/")
    print("    --(*)--    --*--")
    print("      /|\\        |")
    print("  ____|__________|____")
    print(" /   {}    {}    {}   \\")
    print(" |____________________|")
    print("Ты входишь в оранжерею. Растения здесь выросли до самого потолка.")
    print("1 - Пробраться через заросли")
    print("2 - Сорвать странный цветок")
    print("3 - Осмотреть фонтан")
    c = input("Твой выбор: ")

    if c == "1":
        print("Ты раздвигаешь толстые лианы.")
        if has_sword:
            print("Ты прорубаешь проход мечом.")
            bonus = 1
        else:
            print("Лианы цепляются за одежду.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("В зарослях спрятан сундук с золотом.")
            gold = gold + 40
            print("Ты получаешь золота: 40")
        elif roll >= 3:
            print("Ты находишь несколько монет.")
            gold = gold + 10
            print("Ты получаешь золота: 10")
        else:
            print("Лианы туго обвивают тебя.")
            health = health - 20
            print("Ты теряешь здоровья: 20")

    elif c == "2":
        print("Ты протягиваешь руку к светящемуся цветку.")
        if has_amulet:
            print("Амулет защищает тебя от пыльцы.")
            bonus = 1
        else:
            print("Пыльца щекочет нос и кружит голову.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("Из цветка получается целебное зелье.")
            has_potion = True
            print("Ты собираешь зелье из цветка.")
        elif roll >= 3:
            print("Цветок оказывается красивым, но бесполезным.")
            gold = gold + 5
            print("Ты получаешь золота: 5")
        else:
            print("Цветок выпускает ядовитое облако.")
            health = health - 20
            print("Ты теряешь здоровья: 20")

    elif c == "3":
        print("Ты подходишь к высохшему фонтану.")
        if has_torch:
            print("Факел освещает дно фонтана.")
            bonus = 1
        else:
            print("Дно фонтана тонет в тени.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("На дне блестит ключ.")
            has_key = True
            print("Ты достаёшь ключ.")
        elif roll >= 3:
            print("Ты находишь на дне пару монет.")
            gold = gold + 10
            print("Ты получаешь золота: 10")
        else:
            print("Ты поскальзываешься на мокрых камнях.")
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
        print("Ты немного отдыхаешь и восстанавливаешь 5 здоровья.")
        health = health + 5
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

# ---------- Глава 12: Часовая комната ----------
if alive:
    print()
    print("=== Глава 12 из 22: Часовая комната ===")
    print("       _________")
    print("     .'  12     '.")
    print("    /  9   +   3  \\")
    print("    |      |      |")
    print("    \\      6      /")
    print("     '._________.'")
    print("В часовой комнате тикают сотни старых часов, и ни одни не показывают одно время.")
    print("1 - Остановить маятник")
    print("2 - Открыть корпус больших часов")
    print("3 - Перевести стрелки")
    c = input("Твой выбор: ")

    if c == "1":
        print("Ты хватаешься за большой маятник.")
        if has_shield:
            print("Щит защищает тебя от удара маятника.")
            bonus = 1
        else:
            print("Маятник бьёт тебя по руке.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("Механизм открывается, и оттуда падает золото.")
            gold = gold + 40
            print("Ты получаешь золота: 40")
        elif roll >= 3:
            print("Маятник останавливается, и становится тише.")
            gold = gold + 5
            print("Ты получаешь золота: 5")
        else:
            print("Маятник сильно бьёт тебя.")
            health = health - 20
            print("Ты теряешь здоровья: 20")

    elif c == "2":
        print("Ты подходишь к самым большим часам.")
        if has_key:
            print("Ключ подходит к замку на дверце.")
            bonus = 1
        else:
            print("Дверца заедает, и ты долго с ней возишься.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("Внутри спрятана карта замка.")
            has_map = True
            print("Ты забираешь карту.")
        elif roll >= 3:
            print("Внутри только шестерёнки и пара монет.")
            gold = gold + 10
            print("Ты получаешь золота: 10")
        else:
            print("Пружина выскакивает и бьёт тебя.")
            health = health - 15
            print("Ты теряешь здоровья: 15")

    elif c == "3":
        print("Ты тянешься к стрелкам часов.")
        if has_map:
            print("Карта подсказывает нужное время.")
            bonus = 1
        else:
            print("Ты крутишь стрелки наугад.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("Часы бьют, и открывается потайной ящик с золотом.")
            gold = gold + 35
            print("Ты получаешь золота: 35")
        elif roll >= 3:
            print("Часы бьют полночь, но ничего не происходит.")
        else:
            print("Часы звонят так громко, что у тебя звенит в голове.")
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
        print("Ты немного отдыхаешь и восстанавливаешь 5 здоровья.")
        health = health + 5
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

# ---------- Глава 13: Тюрьма ----------
if alive:
    print()
    print("=== Глава 13 из 22: Тюрьма ===")
    print("  ||  ||  ||  ||  ||")
    print("  ||  ||  ||  ||  ||")
    print("  ====================")
    print("  ||  ||  ||  ||  ||")
    print("  ||  ||  ||  ||  ||")
    print("Ты спускаешься в тюрьму. Камеры давно пусты, но воздух всё ещё тяжёлый.")
    print("1 - Осмотреть камеры")
    print("2 - Открыть дверь стражи")
    print("3 - Поговорить с призраком")
    c = input("Твой выбор: ")

    if c == "1":
        print("Ты идёшь по коридору мимо решёток.")
        if has_torch:
            print("Факел показывает надписи на стенах.")
            bonus = 1
        else:
            print("Ты почти ничего не видишь.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("В одной из камер лежит спрятанное золото.")
            gold = gold + 35
            print("Ты получаешь золота: 35")
        elif roll >= 3:
            print("Ты находишь в камере старые монеты.")
            gold = gold + 10
            print("Ты получаешь золота: 10")
        else:
            print("Ржавая решётка падает рядом и задевает тебя.")
            health = health - 15
            print("Ты теряешь здоровья: 15")

    elif c == "2":
        print("Ты подходишь к двери комнаты стражи.")
        if has_key:
            print("Ключ открывает замок с первого раза.")
            bonus = 1
        else:
            print("Ты ломаешь замок плечом.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("В комнате стражи лежит щит и мешок монет.")
            gold = gold + 20
            print("Ты получаешь золота: 20")
            has_shield = True
            print("Ты берёшь щит.")
        elif roll >= 3:
            print("Ты находишь стол с пыльными монетами.")
            gold = gold + 10
            print("Ты получаешь золота: 10")
        else:
            print("Дверь падает на тебя.")
            health = health - 15
            print("Ты теряешь здоровья: 15")

    elif c == "3":
        print("Ты тихо зовёшь того, кто здесь жил.")
        if has_amulet:
            print("Амулет успокаивает призрака.")
            bonus = 1
        else:
            print("Призрак смотрит на тебя недоверчиво.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("Призрак показывает тебе тайник с золотом.")
            gold = gold + 40
            print("Ты получаешь золота: 40")
        elif roll >= 3:
            print("Призрак благодарит тебя за разговор.")
        else:
            print("Призрак пугает тебя до дрожи.")
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
        print("Ты немного отдыхаешь и восстанавливаешь 5 здоровья.")
        health = health + 5
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

# ---------- Глава 14: Лаборатория ----------
if alive:
    print()
    print("=== Глава 14 из 22: Лаборатория ===")
    print("    __      ___     _")
    print("   |  |    /   \\   | |")
    print("   |~~|   |~~~~~|  |~|")
    print("  /~~~~\\  |~~~~~|  |~|")
    print(" |~~~~~~| |_____|  |_|")
    print("  \\____/")
    print("Ты находишь алхимическую лабораторию. Колбы с цветными жидкостями стоят на столах.")
    print("1 - Смешать зелья")
    print("2 - Обыскать шкафы")
    print("3 - Проверить котёл с зельем")
    c = input("Твой выбор: ")

    if c == "1":
        print("Ты берёшь две колбы и смешиваешь содержимое.")
        if has_map:
            print("Рецепт на карте подсказывает пропорции.")
            bonus = 1
        else:
            print("Ты смешиваешь жидкости наугад.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("Получается отличное лечебное зелье!")
            has_potion = True
            print("Ты наливаешь зелье во флягу.")
        elif roll >= 3:
            print("Получается мутная жидкость без свойств.")
        else:
            print("Колбы взрываются у тебя в руках.")
            health = health - 25
            print("Ты теряешь здоровья: 25")

    elif c == "2":
        print("Ты открываешь шкафы с пыльными склянками.")
        if has_key:
            print("Ключ отпирает самый дальний шкаф.")
            bonus = 1
        else:
            print("Дальний шкаф закрыт, и ты осматриваешь другие.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("В шкафу стоит ящик с золотом.")
            gold = gold + 35
            print("Ты получаешь золота: 35")
        elif roll >= 3:
            print("Ты находишь несколько монет.")
            gold = gold + 10
            print("Ты получаешь золота: 10")
        else:
            print("Склянка разбивается, и пары жгут горло.")
            health = health - 15
            print("Ты теряешь здоровья: 15")

    elif c == "3":
        print("Ты заглядываешь в булькающий котёл.")
        if has_shield:
            print("Щит защищает тебя от брызг.")
            bonus = 1
        else:
            print("Горячие брызги летят тебе в лицо.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("На дне котла лежит золотой слиток.")
            gold = gold + 45
            print("Ты получаешь золота: 45")
        elif roll >= 3:
            print("Ты вылавливаешь пару монет.")
            gold = gold + 8
            print("Ты получаешь золота: 8")
        else:
            print("Брызги обжигают тебе руки.")
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
        print("Ты немного отдыхаешь и восстанавливаешь 5 здоровья.")
        health = health + 5
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

# ---------- Глава 15: Крыша замка ----------
if alive:
    print()
    print("=== Глава 15 из 22: Крыша замка ===")
    print("   /\\_/\\      ____")
    print("  ( o.o )    /____\\")
    print("   > ^ <    /|    |\\")
    print("  /|   |\\  / |    | \\")
    print(" ^^^^^^^^^^^^^^^^^^^^^^")
    print("Ты выходишь на крышу замка. Каменные горгульи смотрят на тебя сверху вниз.")
    print("1 - Пройти по краю крыши")
    print("2 - Осмотреть горгулью")
    print("3 - Сесть и осмотреться")
    c = input("Твой выбор: ")

    if c == "1":
        print("Ты идёшь по узкому краю.")
        if has_shield:
            print("Щит помогает удержать равновесие на ветру.")
            bonus = 1
        else:
            print("Сильный ветер почти сбивает тебя с ног.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("На краю лежит забытый кошелёк.")
            gold = gold + 30
            print("Ты получаешь золота: 30")
        elif roll >= 3:
            print("Ты благополучно доходишь до другой башни.")
            gold = gold + 5
            print("Ты получаешь золота: 5")
        else:
            print("Ветер сбивает тебя, и ты ударяешься о камни.")
            health = health - 20
            print("Ты теряешь здоровья: 20")

    elif c == "2":
        print("Ты подходишь к самой большой горгулье.")
        if has_sword:
            print("Ты стучишь по камню рукоятью меча.")
            bonus = 1
        else:
            print("Ты стучишь по камню кулаком.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("В горгулье спрятан тайник с золотом.")
            gold = gold + 40
            print("Ты получаешь золота: 40")
        elif roll >= 3:
            print("В трещине камня лежат монеты.")
            gold = gold + 10
            print("Ты получаешь золота: 10")
        else:
            print("Горгулья оживает и бьёт тебя лапой.")
            health = health - 20
            print("Ты теряешь здоровья: 20")

    elif c == "3":
        print("Ты садишься на холодные камни.")
        if has_map:
            print("Карта показывает на пейзаж, который ты видишь.")
            bonus = 1
        else:
            print("Ты просто смотришь на звёзды.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("Ты замечаешь во дворе спрятанный сундук.")
            gold = gold + 25
            print("Ты получаешь золота: 25")
        elif roll >= 3:
            print("Ты немного отдыхаешь, и это придаёт тебе сил.")
        else:
            print("Холодный ветер пробирает тебя до костей.")
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
        print("Ты немного отдыхаешь и восстанавливаешь 5 здоровья.")
        health = health + 5
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

# ---------- Глава 16: Тайный проход ----------
if alive:
    print()
    print("=== Глава 16 из 22: Тайный проход ===")
    print("  |\\            /|")
    print("  | \\          / |")
    print("  |  \\  ____  /  |")
    print("  |   \\|    |/   |")
    print("  |    |    |    |")
    print("  |   /|____|\\   |")
    print("  |  /          \\ |")
    print("За стеной открывается узкий тайный проход. Воздух внутри затхлый.")
    print("1 - Идти вперёд")
    print("2 - Искать скрытые двери")
    print("3 - Позвать на помощь")
    c = input("Твой выбор: ")

    if c == "1":
        print("Ты осторожно идёшь по проходу.")
        if has_torch:
            print("Факел освещает паутину на стенах.")
            bonus = 1
        else:
            print("Ты идёшь в полной темноте.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("В конце прохода лежит мешок золота.")
            gold = gold + 40
            print("Ты получаешь золота: 40")
        elif roll >= 3:
            print("Ты доходишь до конца прохода без приключений.")
            gold = gold + 5
            print("Ты получаешь золота: 5")
        else:
            print("Ты попадаешь в ловушку с иглами.")
            health = health - 20
            print("Ты теряешь здоровья: 20")

    elif c == "2":
        print("Ты ощупываешь стены прохода.")
        if has_map:
            print("Карта показывает потайные двери.")
            bonus = 1
        else:
            print("Ты нажимаешь на камни наугад.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("Одна из стен открывается, и за ней стоит сундук.")
            gold = gold + 40
            print("Ты получаешь золота: 40")
        elif roll >= 3:
            print("Ты находишь нишу с парой монет.")
            gold = gold + 10
            print("Ты получаешь золота: 10")
        else:
            print("Часть стены обрушивается на тебя.")
            health = health - 20
            print("Ты теряешь здоровья: 20")

    elif c == "3":
        print("Ты громко зовёшь на помощь.")
        if has_amulet:
            print("Амулет откликается тёплым светом.")
            bonus = 1
        else:
            print("Эхо возвращается к тебе пустым.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("Тебе отвечает добрый дух и дарит зелье.")
            has_potion = True
            print("Ты берёшь зелье.")
        elif roll >= 3:
            print("Ты слышишь далёкий шорох.")
        else:
            print("Твой крик пугает летучих мышей.")
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
        print("Ты немного отдыхаешь и восстанавливаешь 5 здоровья.")
        health = health + 5
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

# ---------- Глава 17: Зеркальный зал ----------
if alive:
    print()
    print("=== Глава 17 из 22: Зеркальный зал ===")
    print("  .----.  .----.  .----.")
    print("  |    |  |    |  |    |")
    print("  | /\\ |  | /\\ |  | /\\ |")
    print("  |/__\\|  |/__\\|  |/__\\|")
    print("  '----'  '----'  '----'")
    print("Ты входишь в зал, где сотни зеркал отражают тебя со всех сторон.")
    print("1 - Разбить зеркало")
    print("2 - Найти настоящий проход")
    print("3 - Поговорить с отражением")
    c = input("Твой выбор: ")

    if c == "1":
        print("Ты замахиваешься на ближайшее зеркало.")
        if has_sword:
            print("Ты ударяешь по зеркалу мечом.")
            bonus = 1
        else:
            print("Ты бьёшь по зеркалу рукой.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("За зеркалом открывается тайник с золотом.")
            gold = gold + 35
            print("Ты получаешь золота: 35")
        elif roll >= 3:
            print("Зеркало разбивается, и ты находишь монеты среди осколков.")
            gold = gold + 8
            print("Ты получаешь золота: 8")
        else:
            print("Осколки сильно режут тебя.")
            health = health - 20
            print("Ты теряешь здоровья: 20")

    elif c == "2":
        print("Ты осторожно идёшь между зеркалами.")
        if has_map:
            print("Карта помогает не потеряться среди отражений.")
            bonus = 1
        else:
            print("Ты путаешься между отражениями.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("В конце зала ты находишь ключ.")
            has_key = True
            print("Ты берёшь ключ.")
        elif roll >= 3:
            print("Ты благополучно проходишь зал.")
            gold = gold + 5
            print("Ты получаешь золота: 5")
        else:
            print("Ты врезаешься в зеркало и ушибаешься.")
            health = health - 10
            print("Ты теряешь здоровья: 10")

    elif c == "3":
        print("Ты останавливаешься перед большим зеркалом.")
        if has_amulet:
            print("Амулет делает отражение дружелюбным.")
            bonus = 1
        else:
            print("Отражение смотрит на тебя злобно.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("Отражение дарит тебе золото из зазеркалья.")
            gold = gold + 45
            print("Ты получаешь золота: 45")
        elif roll >= 3:
            print("Отражение кивает тебе и исчезает.")
        else:
            print("Отражение бьёт тебя изнутри зеркала.")
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
        print("Ты немного отдыхаешь и восстанавливаешь 5 здоровья.")
        health = health + 5
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

# ---------- Глава 18: Кладбище ----------
if alive:
    print()
    print("=== Глава 18 из 22: Кладбище ===")
    print("      _|_        _|_       _")
    print("       |          |       _|_")
    print("    ___|___    ___|___     |")
    print("   /       \\  /       \\  __|__")
    print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("За стеной замка находится старое кладбище. Над могилами стелется туман.")
    print("1 - Осмотреть склеп")
    print("2 - Пройти между могил")
    print("3 - Помолиться в часовне")
    c = input("Твой выбор: ")

    if c == "1":
        print("Ты подходишь к каменному склепу.")
        if has_key:
            print("Ключ открывает тяжёлую дверь склепа.")
            bonus = 1
        else:
            print("Ты с трудом сдвигаешь тяжёлую плиту.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("В склепе лежат фамильные драгоценности.")
            gold = gold + 45
            print("Ты получаешь золота: 45")
        elif roll >= 3:
            print("В склепе ты находишь несколько монет.")
            gold = gold + 10
            print("Ты получаешь золота: 10")
        else:
            print("Из склепа вырывается холодный дух.")
            health = health - 20
            print("Ты теряешь здоровья: 20")

    elif c == "2":
        print("Ты идёшь между старых надгробий.")
        if has_torch:
            print("Факел отгоняет туман.")
            bonus = 1
        else:
            print("Туман не даёт тебе ничего разглядеть.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("Ты находишь забытый кошелёк у надгробия.")
            gold = gold + 30
            print("Ты получаешь золота: 30")
        elif roll >= 3:
            print("Ты спокойно проходишь кладбище.")
            gold = gold + 5
            print("Ты получаешь золота: 5")
        else:
            print("Ты спотыкаешься о камень и падаешь.")
            health = health - 10
            print("Ты теряешь здоровья: 10")

    elif c == "3":
        print("Ты заходишь в маленькую часовню.")
        if has_amulet:
            print("Амулет светится в святом месте.")
            bonus = 1
        else:
            print("В часовне тихо и холодно.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("Ты получаешь благословение и зелье.")
            has_potion = True
            print("Ты забираешь зелье.")
        elif roll >= 3:
            print("Тебе становится спокойнее.")
        else:
            print("Старая балка падает с потолка.")
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
        print("Ты немного отдыхаешь и восстанавливаешь 5 здоровья.")
        health = health + 5
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

# ---------- Глава 19: Музыкальный салон ----------
if alive:
    print()
    print("=== Глава 19 из 22: Музыкальный салон ===")
    print("   _________________")
    print("  | | || | | || || | |")
    print("  | | || | | || || | |")
    print("  | |_||_| |_||_||_| |")
    print("  |__|__|___|__|__|__|")
    print("В салоне стоит старый рояль, а на стенах висят скрипки и арфы.")
    print("1 - Сыграть на рояле")
    print("2 - Осмотреть арфу")
    print("3 - Взять скрипку")
    c = input("Твой выбор: ")

    if c == "1":
        print("Ты садишься за пыльный рояль.")
        if has_map:
            print("Ноты с карты помогают сыграть мелодию.")
            bonus = 1
        else:
            print("Ты нажимаешь клавиши наугад.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("Крышка рояля поднимается, и там лежит золото.")
            gold = gold + 40
            print("Ты получаешь золота: 40")
        elif roll >= 3:
            print("Ты играешь, и мелодия звучит неплохо.")
            gold = gold + 5
            print("Ты получаешь золота: 5")
        else:
            print("Рояль издаёт жуткий звук, и у тебя звенит в ушах.")
            health = health - 10
            print("Ты теряешь здоровья: 10")

    elif c == "2":
        print("Ты подходишь к золочёной арфе.")
        if has_sword:
            print("Ты осторожно перерезаешь запутанную струну мечом.")
            bonus = 1
        else:
            print("Струны запутаны, и ты рвёшь их руками.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("В арфе спрятан мешочек с золотом.")
            gold = gold + 35
            print("Ты получаешь золота: 35")
        elif roll >= 3:
            print("Ты находишь в арфе пару монет.")
            gold = gold + 10
            print("Ты получаешь золота: 10")
        else:
            print("Струна лопается и хлещет тебя по лицу.")
            health = health - 15
            print("Ты теряешь здоровья: 15")

    elif c == "3":
        print("Ты снимаешь старую скрипку со стены.")
        if has_amulet:
            print("Амулет заставляет скрипку звучать чисто.")
            bonus = 1
        else:
            print("Скрипка играет фальшиво.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("Мелодия открывает потайной ящик с ключом.")
            has_key = True
            print("Ты берёшь ключ.")
        elif roll >= 3:
            print("Ты играешь простую мелодию.")
        else:
            print("Смычок ломается и ранит тебя.")
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
        print("Ты немного отдыхаешь и восстанавливаешь 5 здоровья.")
        health = health + 5
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

# ---------- Глава 20: Обсерватория ----------
if alive:
    print()
    print("=== Глава 20 из 22: Обсерватория ===")
    print("    *      .      *")
    print("  .     __/\\__  .     *")
    print("       /      \\")
    print("      |  ____  |===\\")
    print("      | |    |       \\==o")
    print("      |_|____|_")
    print("На самом верху замка находится обсерватория с огромным телескопом.")
    print("1 - Посмотреть в телескоп")
    print("2 - Осмотреть стол с чертежами")
    print("3 - Открыть купол")
    c = input("Твой выбор: ")

    if c == "1":
        print("Ты приникаешь к окуляру.")
        if has_map:
            print("Карта звёзд помогает навести телескоп.")
            bonus = 1
        else:
            print("Ты наводишь телескоп наугад.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("Ты видишь на земле сундук с золотом и запоминаешь место.")
            gold = gold + 35
            print("Ты получаешь золота: 35")
        elif roll >= 3:
            print("Ты видишь красивое звёздное небо.")
        else:
            print("Телескоп падает и бьёт тебя.")
            health = health - 20
            print("Ты теряешь здоровья: 20")

    elif c == "2":
        print("Ты подходишь к столу астронома.")
        if has_torch:
            print("Факел освещает мелкий почерк на чертежах.")
            bonus = 1
        else:
            print("Чертежи слишком тёмные, чтобы их читать.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("Под чертежами лежит мешок монет.")
            gold = gold + 30
            print("Ты получаешь золота: 30")
        elif roll >= 3:
            print("Под чертежами ты находишь пару монет.")
            gold = gold + 8
            print("Ты получаешь золота: 8")
        else:
            print("Стопка бумаг рассыпается, и ты режешься о край.")
            health = health - 10
            print("Ты теряешь здоровья: 10")

    elif c == "3":
        print("Ты тянешь рычаг купола.")
        if has_shield:
            print("Щит прикрывает тебя от падающего снега.")
            bonus = 1
        else:
            print("Холодный снег падает тебе на голову.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("Лунный свет открывает потайной люк с золотом.")
            gold = gold + 40
            print("Ты получаешь золота: 40")
        elif roll >= 3:
            print("Купол открывается, и ты любуешься звёздами.")
        else:
            print("Рычаг срывается и бьёт тебя.")
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
        print("Ты немного отдыхаешь и восстанавливаешь 5 здоровья.")
        health = health + 5
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

# ---------- Глава 21: Пещера дракона ----------
if alive:
    print()
    print("=== Глава 21 из 22: Пещера дракона ===")
    print("         /\\  /\\")
    print("        /  \\/  \\___")
    print("       / (o)  (o)  \\==>")
    print("      |   ______    |")
    print("       \\  \\VVVV/   /")
    print("        \\__\\__/___/")
    print("Лестница ведёт в пещеру, где спит огромный дракон на горе золота.")
    print("1 - Подкрасться и взять золото")
    print("2 - Сразиться с драконом")
    print("3 - Обойти пещеру стороной")
    c = input("Твой выбор: ")

    if c == "1":
        print("Ты тихо подкрадываешься к золоту.")
        if has_amulet:
            print("Амулет гасит шум твоих шагов.")
            bonus = 1
        else:
            print("Каждый шаг эхом отдаётся в пещере.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("Ты набираешь целую сумку золота и уходишь незамеченным!")
            gold = gold + 80
            print("Ты получаешь золота: 80")
        elif roll >= 3:
            print("Ты уносишь горсть монет.")
            gold = gold + 25
            print("Ты получаешь золота: 25")
        else:
            print("Дракон просыпается и дышит на тебя огнём.")
            health = health - 30
            print("Ты теряешь здоровья: 30")

    elif c == "2":
        print("Ты поднимаешь оружие и идёшь на дракона.")
        if has_sword:
            print("Меч блестит в свете костра.")
            bonus = 1
        else:
            print("У тебя нет подходящего оружия.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("Ты побеждаешь дракона и получаешь его сокровища!")
            gold = gold + 120
            print("Ты получаешь золота: 120")
        elif roll >= 3:
            print("Ты ранишь дракона, и он отступает.")
            gold = gold + 40
            print("Ты получаешь золота: 40")
        else:
            print("Дракон бьёт тебя хвостом.")
            health = health - 35
            print("Ты теряешь здоровья: 35")

    elif c == "3":
        print("Ты идёшь вдоль стены пещеры.")
        if has_map:
            print("Карта подсказывает безопасный путь.")
            bonus = 1
        else:
            print("Ты идёшь по камням наугад.")
            bonus = 0
        roll = random.randint(1, 6) + bonus
        print("Бросок кубика: " + str(roll))
        if roll >= 6:
            print("Ты находишь в стене тайник с золотом.")
            gold = gold + 40
            print("Ты получаешь золота: 40")
        elif roll >= 3:
            print("Ты обходишь пещеру и выходишь к двери.")
        else:
            print("Камень падает и задевает тебя.")
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
        print("Ты немного отдыхаешь и восстанавливаешь 5 здоровья.")
        health = health + 5
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

# ---------- Глава 22: Тронный зал ----------
if alive:
    print()
    print("=== Глава 22 из 22: Тронный зал ===")
    print("       _________")
    print("      |  *   *  |")
    print("      |_________|")
    print("       |  ___  |")
    print("     __|_|   |_|__")
    print("    |             |")
    print("    |_____________|")
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
        print("Ты немного отдыхаешь и восстанавливаешь 5 здоровья.")
        health = health + 5
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
print("Пройдено глав: " + str(done) + " из 22")
print("Здоровье: " + str(health))
print("Золото: " + str(gold))

if gold >= 700:
    rank = "Легендарный охотник за сокровищами"
elif gold >= 500:
    rank = "Великий искатель приключений"
elif gold >= 350:
    rank = "Богатый путешественник"
elif gold >= 200:
    rank = "Опытный авантюрист"
elif gold >= 100:
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
    if done >= 22:
        if gold >= 600:
            print("Ты прошёл весь замок и вышел с огромным богатством. О тебе сложат легенды!")
        elif gold >= 300:
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
if done >= 22:
    print("- Прошёл замок до конца")
    achieved = True
if gold >= 500:
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
if alive:
    if done >= 22:
        print("      ______________")
        print("     /\\             \\")
        print("    /  \\_____________\\")
        print("    \\  /_____________/")
        print("     \\/ ($) ($) ($) |")
        print("      |_____________|")
else:
    print("       _______")
    print("      /       \\")
    print("     |  O   O  |")
    print("     |    ^    |")
    print("      \\  ===  /")
    print("       |_|_|_|")

print()
print("Спасибо за игру, " + name + "!")
print("Запусти игру снова, чтобы попробовать другой путь.")
print("Конец.")
