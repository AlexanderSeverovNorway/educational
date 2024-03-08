# Пусть мы хотим обрабатывать некоторые события из уже известных нам логов событий.
# Создадим класс с конструктором:

class Event:
    def __init__(self, timestamp, event_type, session_id):
        self.timestamp = timestamp
        self.type = event_type
        self.session_id = session_id
# Допустим, мы уже распарсили наши логи и получили список словарей вроде такого:

events = [
    {
     "timestamp": 1554583508000,
     "type": "itemViewEvent",
     "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
     "timestamp": 1555296337000,
     "type": "itemViewEvent",
     "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
     "timestamp": 1549461608000,
     "type": "itemBuyEvent",
     "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
]

# Давайте для каждого события в списке создадим соответствующий ему объект с помощью конструктора,
# как мы уже делали. А чтобы убедиться, что объект создаётся, выведем на печать какой-нибудь из атрибутов:

for event in events:
    event_obj = Event(timestamp=event.get("timestamp"),
                      event_type=event.get("type"),
                      session_id=event.get("session_id"))
    print(event_obj.timestamp)

# Здесь мы использовали метод словаря .get(), который не вызовет ошибку, если такого ключа в словаре нет.

# Вместо такого явного разбора словаря в цикле мы могли бы задать нашему классу метод,
# который позволяет инициализировать наш объект напрямую. Для этого давайте поправим объявление
# нашего класса и зададим для каждой переменной её значение по умолчанию,
# чтобы мы могли инициализировать объект без заполнения.
# Это делается с помощью указания значений по умолчанию сразу после названия аргумента:

class Event:
    def __init__(self, timestamp=0, event_type="", session_id=""):
        self.timestamp = timestamp
        self.type = event_type
        self.session_id = session_id
#Отлично, а теперь добавим метод. Не забываем, что метод принимает на вход self первым аргументом.

def init_from_dict(self, event_dict):
        self.timestamp = event_dict.get("timestamp")
        self.type = event_dict.get("type")
        self.session_id = event_dict.get("session_id")
# Метод идет с отступом и должен быть объявлен внутри класса.

# После этого мы скрыли реализацию логики от пользователя — то есть нам уже неважно,
# как это работает, мы знаем, что можем подать на вход словарь с нужными ключами,
# и всё будет работать само.

for event in events:
    event_obj = Event()
    event_obj.init_from_dict(event)
    print(event_obj.timestamp)