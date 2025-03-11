# Чат-бот для помощи клиентам
Работу выполнил студент группы М8О-114СВ-24 Красавин М.А.

## В проекте реализовано:
* Чат-бот с возможностью ведения диалога и понимания контекстных вопросов
* Файлы тестирования работы чат-бота
* Дашборд с информацией о запросах пользователей
## Стек:
* IDE `PyCharm` 2024.3
* ЯП `Python` 3.10
* Фреймворк `Rasa` 3.6.21 для разработки и обучения чат-бота
* Фреймворк `Flask` 3.1.0 для реализации веб-версии чат-бота
* Библиотека `SQLAlchemy` для логирования запросов в БД
* СУБД `PostgreSQL`/ `PgAdmin` для управления реляционной БД
* Фреймворк `Streamlit` для визуализации дашборда
* `Aiogram, Pandas, Numpy, Tensorflow` и другие зависимые и необходимые библиотеки
## Установка зависимостей
Для того, чтобы проект заработал, необходимы библиотеки, которые можно установить, выполнив команду `pip install -r requirements.txt`

# Использование бота
Бот реализован в виде веб-интерфейса на локал хосте и в виде бота telegram
## Для использования веб-версии порядок действий следующий:
* В консоли ввести команду `rasa shell` для запуска бота
* Во втором окне выполнить команду `python app.py` и перейти по ссылке в появившемся окне
* Бот готов к использованию!
## Для использования telegram-бота необходимо:
* Активировать туннель для доступа к локальному серверу (в данном случае использовался российский `xTunnel`), для этого в директории исполняемого файла выполнить команду `xTunnel 5005`
* В первой строке консоли должно быть `Status: Connected`. После этого копируем `public address` в `credentials.yml` в строку `webhook_url` в таком формате: `"<ссылка>/webhooks/telegram/webhook"`
* В консоли выполняем команду `rasa run --enable-api --cors "*"`
* Сам бот можно найти по [ссылке](https://t.me/helpabitbot) или по нику `@helpabitbot`
* Бот готов к использованию!
## Типичный сценарий использования бота
Приветсвие - желание открыть счет - форма собственности - обороты - благодарность - прощание

Примечание: для подключения к серверу используется библиотека `aiogram`, которая по умолчанию скачивается последней версии. Rasa работает только с версиями ниже 2.26. Поэтому при появлении ошибок необходимо удалить эту библиотеку и выполнить команду `pip install aiogram==2.25.2`

## Тестирование бота
Для тестирования бота необходимо ввести в консоль команду `rasa test --model models/20250311-162726-roaring-ordnance.tar.gz --stories tests/test_stories.yml --out results 2>&1 | tee results/test_results.txt`

Результаты сохраняются по пути `results/test_results.txt`, в котором можно ознакомиться с основными метриками для оценки алгоритмов машинного обучения

## Логирование запросов и аналитика использования
Для того, чтобы получить информацию об использовании бота, в проекте реализован дашборд. Чтобы воспользоваться им, нужно попользоваться ботом, чтобы БД пополнилась информацией, а затем воспользоваться командой `streamlit run dashboard.py`, который выдаст информацию в удобном для понимания виде

## Демонстрация работы
Работу бота посмотреть на [видео](https://disk.yandex.ru/d/qTC6pMnMnrru6g)
 
