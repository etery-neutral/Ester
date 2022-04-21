from telebot import TeleBot
import wikipedia
import logging
import pyowm
from random import choice


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

# Заготовки для проекта

bot = TeleBot('5201323744:AAHbbiY1SfYQgbjbEx64mu7S-DGFx25R4xo')

wikipedia.set_lang("ru")

dashes = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']

d_1 = ["Не всё так плохо, как ты думаешь.", "Не повезло здесь – значит повезёт в другом.",
       "Это ещё не показатель удачи.", "Вот тебе совет: поддерживай себя в форме.",
       "Надеюсь, ставку Вы не делали.", "Episode I: The Phantom Menace."]
d_2 = ["Хм, напомни, а зачем ты бросаешь кость?...Впрочем, неважно.", "Совет на день: прочти книгу.",
       "Небольшой совет: избавься от ненужного мусора.", "Бывают в жизни огорчения.",
       "Что ж, попробуй ещё.", "Episode II - Attack of the Clones."]
d_3 = ["Поздравляю с достижением внутреннего равновесия.", "Получи совет: расслабься!",
       "Помни: если ты ошибся, то проще признать это, чем упорствовать в ошибке.",
       "Не забывай: Не жди шансов, а сам создавай возможности.", "Может, протестируешь другие команды?)",
       "Episode III - Revenge of the Sith."]
d_4 = ["Лучше, чем половина, но ты можешь лучше.", "Попробуй сегодня поймать вдохновение.",
       "Проводите время с дорогими людьми. Это действительно важно.",
       "Обращай внимание на красоту незначительных маленьких вещей, порой это приятно удивляет.",
       "Не банальны ли мои советы?", "Отдохни от гаджетов немного."]
d_5 = ["Молодец, ты почти у цели!", "Думай всегда на несколько шагов вперед.",
       "Оставляй себе личное пространство. Это просто необходимо иногда, понимаешь?",
       "Помни о хорошем сне. Это играет большую роль.",
       "Если головоломка не сложилась, и тебе уже не собрать пазлы — начни сначала.", "Давай жить в моменте."]
d_6 = ["Что ж, цель достигнута. А теперь отдохни.", "Иногда нужно быть загадкой для других, не так ли?)",
       "Прислушивайся к своим желаниям.", "Надеюсь, ты не будешь останавливаться на достигнутом.",
       "Запиши мысли в блокнот, кто знает, может ты станешь успешным. Да и для тебя будет полезным.",
       "Помедитируй: https://www.youtube.com/watch?v=_ng9KyDSUG4 ."]

# Предсказания для гороскопа

part_1 = ["Запаситесь терпением: оно сегодня потребуется вам для общения с окружающими. ",
          "У вас многое будет получаться хорошо. ",
          "Не будьте слишком доверчивы. ",
          "Вы легко найдете общий язык с самыми разными людьми, поладите даже с теми, с кем прежде много спорили. ",
          "Занимайтесь сложными и важными делами. ",
          "Готовьтесь действовать быстро. ",
          "День обещает денежные поступления и удачные сделки.",
          "Будьте готовы к спорам. ",
          "Важно сохранять самообладание в начале дня. ",
          "Не стройте иллюзий. ",
          "Настройтесь на серьезный лад. ",
          "Не стоит торопиться. "]
part_2 = ["Будьте внимательны, старайтесь избежать даже мелких ошибок. ",
          "Вы сможете добиться заметного прогресса, если проявите настойчивость. ",
          "Просто будьте готовы к трудностям, не требуйте от себя невозможного и не спешите. ",
          "Будет шанс справиться с тем, что долго не получалось. ",
          "Неожиданно могут появиться новые задачи, требующие решения. ",
          "Сегодня у вас многое будет получаться. ",
          "Найти общий язык с окружающими будет непросто, даже давние знакомые порой могут понимать вас неправильно. ",
          "Вас ждет напряженный и плодотворный день. ",
          "Вероятны какие-то неожиданные события, происшествия, из-за которых придется менять планы. ",
          "Сегодня вам очень пригодится умение смотреть на вещи объективно, не переоценивать свои возможности. ",
          "День отлично подойдет для того, чтобы отдавать распоряжения, решать организационные вопросы, "
          "а также объединять людей, цели которых схожи. ",
          "Будет возможность укрепить деловые отношения. ", ""]
part_3 = ["Влияние позитивных тенденций будет усиливаться со временем, "
          "вторая половина дня сложится гораздо удачнее и интереснее первой. ",
          "Во второй половине дня будет много суеты и неразберихи. ",
          "Позже наступит спокойное и благоприятное время, хорошо подходящее для общения с близкими и семейных дел. ",
          "Вторая половина дня хорошо подойдет для семейных дел. ",
          "Хорошо пройдут и деловые, и личные встречи. ",
          "День хорошо подойдет для саморазвития. ",
          "Вторая половина дня принесет интересные предложения. ",
          "Влияние позитивных тенденций будет преобладать в сфере личных отношений. ",
          "Не исключены приятные события в семье, перемены к лучшему в отношениях с близкими. ",
          "День будет благоприятным с точки зрения личных отношений. ",
          "Ваши таланты, знания и умения будут востребованы, всем принесут пользу. ",
          "Вторая половина дня – время приятных и полезных встреч. "]
part_4 = ["Чем ближе вечер, тем проще вам будет сосредоточиться на делах,"
          " тем больше шансов отлично справиться с чем-то сложным. ",
          "Помните о своих приоритетах и старайтесь не отвлекаться от того, что считаете самым важным. ",
          "Семейные отношения будут складываться гармонично, а разногласия,"
          " которые огорчали всех, останутся в прошлом. ",
          "Могут появиться хорошие идеи, касающиеся бизнеса. ",
          "Не исключено начало дружеских или романтических отношений с человеком,"
          " совсем не похожим на ваших старых знакомых. ",
          "Не исключено начало романтической истории. ",
          "Возможны интересные предложения, касающиеся работы, заметный карьерный рост. ",
          "Не исключено появление мелких проблем, решение которых потребует незапланированных расходов. ",
          "Не спешите с решениями, старайтесь не действовать под влиянием эмоций. ",
          "Ситуация в деловой сфере может быть неоднозначной. ",
          "Стоит прислушаться к советам, которые будут давать близкие и другие люди, которые хорошо вас знают. ",
          "Общение с близкими подарит массу позитивных эмоций. "]
part_5 = ["Настройтесь на перемены – их будет много, однако как поступить "
          "будет зависеть только от вашей разумности и рациональности. ",
          "Вечер обещает приятные известия от давних знакомых. ",
          "Интуиция подскажет, как стоит себя вести, что лучше говорить и делать. ",
          "Удастся избежать ошибок, быстро получить нужный результат. ",
          "Важно сохранить самообладание и не сердиться из-за пустяков. ",
          "Вечер обещает приятные встречи, а также знакомства, которые запомнятся надолго. ",
          "Вечер подойдет для маленького семейного праздника. ",
          "Вечер будет полон идей и планов, неожиданных открытий, а порой и настоящих озарений. ",
          "Старайтесь проводить больше времени с теми, кто вам дорог. ",
          "Вечером стоит избегать перегрузок: вам полезно будет отдохнуть. ",
          "Когда появится возможность порадовать или приятно удивить любимого человека, вы ее не упустите.",
          "Прислушайтесь к советам тех, чьему опыту и здравому смыслу доверяете."]

zodiac = ['овен', 'телец', 'близнецы', 'рак', 'лев', 'дева',
          'весы', 'скорпион', 'стрелец', 'козерог', 'водолей', 'рыбы']


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Рада приветствовать тебя, пользователь!"
                                      " Меня зовут Ester. Я буду твоим помощником. "
                                      "Чтобы узнать список возможных команд, нажми на кнопку /help. "
                                      "Информация обо мне доступна по кнопке /info. "
                                      "Приятного времени суток.")


@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, "Список команд:")
    command_list = {'/info': "информация о боте.",
                    '/horoscope': "Ваш гороскоп на сегодня.",
                    '/dice': "бросок игральной кости.",
                    '/weather': "погода в указанном городе.",
                    '/wiki': "поиск информации в Wikipedia.",
                    '/about_updates': "справка об обновлениях."
                    }
    for command, info in command_list.items():
        bot.send_message(message.chat.id, f"{command}: {info}")


@bot.message_handler(commands=["info"])
def info(message):
    bot.send_message(message.chat.id, "Бот, который поможет пользователю с погодой, "
                                      "найдёт нужную информацию, предскажет судьбу.")
    bot.send_message(message.chat.id, "(Планируется создание новых полезных функций, ждите...)")


@bot.message_handler(commands=["about_updates"])
def updates(message):
    upg_list = ["диалог", "генератор идей", "психологический тест", "заметки с напоминанием", "и другое."]
    bot.send_message(message.chat.id, ', '.join(upg_list).capitalize())


def get_location(lat, lon):
    url = f"https://vandex.ru/pogoda/maps/nowcast?lat={lat}&lon={lon}&via=hnav&le_Lightning=1"
    return url


def wthr(city: str):
    owm = pyowm.OWM("260fddc18fe3251807b2aa898d548020")
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city)
    wther = observation.weather
    location = get_location(observation.location.lat, observation.location.lon)
    temperature = wther.temperature("celsius")
    return temperature, location


def get_weather(message):
    city = message.text
    try:
        w = wthr(city)
        bot.send_message(message.chat.id, f'Температура: {round(w[0]["temp"])}°C,' 
                                          f' чувствуется как {round(w[0]["feels_like"])} °C. ')
        # bot.send_message(message.chat.id, w[1])
        bot.register_next_step_handler(message, get_weather)
    except Exception:
        bot.send_message(message.chat.id, "Солнышко ли, дождик – не знаю. Попробуй в другой разок.")


@bot.message_handler(commands=['weather'])
def weather(message):
    bot.send_message(message.chat.id, "Введите город:")
    bot.register_next_step_handler(message, get_weather)

    @bot.message_handler(content_types="text")
    def txt(ms):
        bot.send_message(ms.chat.id, str(get_weather(ms.text)))


@bot.message_handler(commands=["horoscope"])
def horo(message):
    bot.send_message(message.chat.id, "Какой у Вас знак зодиака:")

    @bot.message_handler(content_types="text")
    def astro(msg):
        if str(msg.text).lower() in zodiac:
            if "овен" in str(msg.text).lower():
                predictions = choice(part_1) + choice(part_2) + choice(part_3) + choice(part_4) + choice(part_5)
                bot.send_message(msg.chat.id, f"Для Овнов: {predictions}")
                oven = open("signs/овен.jpg", "rb")
                bot.send_photo(msg.chat.id, oven)

            elif "телец" in str(msg.text).lower():
                predictions = choice(part_1) + choice(part_2) + choice(part_3) + choice(part_4) + choice(part_5)
                bot.send_message(msg.chat.id, f"Для Тельцов: {predictions}")
                telec = open("signs/телец.jpg", "rb")
                bot.send_photo(msg.chat.id, telec)

            elif "близнецы" in str(msg.text).lower():
                predictions = choice(part_1) + choice(part_2) + choice(part_3) + choice(part_4) + choice(part_5)
                bot.send_message(msg.chat.id, f"Для Близнецов: {predictions}")
                twins = open("signs/близнецы.jpg", "rb")
                bot.send_photo(msg.chat.id, twins)

            elif "рак" in str(msg.text).lower():
                predictions = choice(part_1) + choice(part_2) + choice(part_3) + choice(part_4) + choice(part_5)
                bot.send_message(msg.chat.id, f"Для Раков: {predictions}")
                rak = open("signs/рак.jpg", "rb")
                bot.send_photo(msg.chat.id, rak)

            elif "лев" in str(msg.text).lower():
                predictions = choice(part_1) + choice(part_2) + choice(part_3) + choice(part_4) + choice(part_5)
                bot.send_message(msg.chat.id, f"Для Львов: {predictions}")
                lion = open("signs/лев.jpg", "rb")
                bot.send_photo(msg.chat.id, lion)

            elif "дева" in str(msg.text).lower():
                predictions = choice(part_1) + choice(part_2) + choice(part_3) + choice(part_4) + choice(part_5)
                bot.send_message(msg.chat.id, f"Для Дев: {predictions}")
                deva = open("signs/дева.jpg", "rb")
                bot.send_photo(msg.chat.id, deva)

            elif "весы" in str(msg.text).lower():
                predictions = choice(part_1) + choice(part_2) + choice(part_3) + choice(part_4) + choice(part_5)
                bot.send_message(msg.chat.id, f"Для Весов: {predictions}")
                vesi = open("signs/весы.jpg", "rb")
                bot.send_photo(msg.chat.id, vesi)

            elif "скорпион" in str(msg.text).lower():
                predictions = choice(part_1) + choice(part_2) + choice(part_3) + choice(part_4) + choice(part_5)
                bot.send_message(msg.chat.id, f"Для Скорпионов: {predictions}")
                scorpio = open("signs/скорпион.jpg", "rb")
                bot.send_photo(msg.chat.id, scorpio)

            elif "стрелец" in str(msg.text).lower():
                predictions = choice(part_1) + choice(part_2) + choice(part_3) + choice(part_4) + choice(part_5)
                bot.send_message(msg.chat.id, f"Для Стрельцов: {predictions}")
                strelec = open("signs/стрелец.jpg", "rb")
                bot.send_photo(msg.chat.id, strelec)

            elif "козерог" in str(msg.text).lower():
                predictions = choice(part_1) + choice(part_2) + choice(part_3) + choice(part_4) + choice(part_5)
                bot.send_message(msg.chat.id, f"Для Козерогов: {predictions}")
                koza = open("signs/козерог.jpg", "rb")
                bot.send_photo(msg.chat.id, koza)

            elif "водолей" in str(msg.text).lower():
                predictions = choice(part_1) + choice(part_2) + choice(part_3) + choice(part_4) + choice(part_5)
                bot.send_message(msg.chat.id, f"Для Водолеев: {predictions}")
                water_guy = open("signs/водолей.jpg", "rb")
                bot.send_photo(msg.chat.id, water_guy)

            elif "рыбы" in str(msg.text).lower():
                predictions = choice(part_1) + choice(part_2) + choice(part_3) + choice(part_4) + choice(part_5)
                bot.send_message(msg.chat.id, f"Для Рыб: {predictions}")
                fish = open("signs/рыбы.jpg", "rb")
                bot.send_photo(msg.chat.id, fish)

        else:
            bot.send_message(msg.chat.id, "Интересная, однако, Вы личность."
                             "Свяжитесь с разработчиком, и мы добавим для Вас ежедневный уникальный гороскоп.")
            crt = open("signs/creature.jpg", "rb")
            bot.send_photo(msg.chat.id, crt)


@bot.message_handler(commands=["dice"])
def dice(message):
    prt = choice(dashes)
    if prt == '\u2680':
        bot.send_message(message.chat.id, '\u2680')
        bot.send_message(message.chat.id, choice(d_1))

    elif prt == '\u2681':
        bot.send_message(message.chat.id, '\u2681')
        bot.send_message(message.chat.id, choice(d_2))

    elif prt == '\u2682':
        bot.send_message(message.chat.id, '\u2682')
        bot.send_message(message.chat.id, choice(d_3))

    elif prt == '\u2683':
        bot.send_message(message.chat.id, '\u2683')
        bot.send_message(message.chat.id, choice(d_4))

    elif prt == '\u2684':
        bot.send_message(message.chat.id, '\u2684')
        bot.send_message(message.chat.id, choice(d_5))

    elif prt == '\u2685':
        bot.send_message(message.chat.id, '\u2685')
        bot.send_message(message.chat.id, choice(d_6))


def find_wiki(res):
    try:
        text = wikipedia.page(res)
        wktxt = text.content[:900]
        fnd = wktxt.split(".")[:-1]
        rsp = ""
        for el in fnd:
            if "==" not in el:
                if len(el.strip()) > 3:
                    rsp += el + '.'
            else:
                break

        return rsp

    except Exception:
        return "Информация в энциклопедии по данному запросу отсутствует."


@bot.message_handler(commands=["wiki"])
def wiki(message):
    bot.send_message(message.chat.id, "Введите интересующую Вас информацию:")

    @bot.message_handler(content_types="text")
    def text_page(mes):
        bot.send_message(mes.chat.id, find_wiki(mes.text))


bot.polling()