CatBot
======

CatBot - это бот для Telegram созданный сделать Вашу жизнь лучше, присылая Вам котиков.

Установка
---------
Создайте виртуальное окружение и активируйте его. Потом в виртуальном окружении выполните:
.. code-block:: text
    pip install -r requirements.txt

Положите картинки с котиками в папку images c расширением .jpg

Настройка
---------
Создайте файл settings.py и добавьте туда следующие настройки:
.. code-block:: python
    API_KEY="API ключ, который вы получили от BotFather"

    USER_EMOJI = [':smiley_cat:', ':smiling_imp:', ':panda_face:', ':dog:']

Запуск
------
В активированном виртуальном окружении выполните:
.. code-block:: text
    python3 bot.py