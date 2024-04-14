# Telegram-бот для игры ХЛОВО (Икслово)
## Что такое Xлово
**Хлово** - игра, вдохновленная игрой Wordle из газеты The New York Times. Задача игрока – отгадать загаданное слово из 5 букв за 6 попыток, причем после каждой попытки игроку сообщается, какие буквы есть в загаданном слове, а каких нет.
## Как это работает
Игрок отправляет сообщение телеграм-боту, после чего игроку предлагается выбрать режим игры:
1. **Новая игра**: игрок должен угадать случайное слово из общего списка слов;
2. **Слово дня**: игрок должен угадать случайно выбранное слово дня (одинаковое для всех игроков).

## Как это устроено
- `copy_main.py` содержит весь основной код Telegram-бота, за исключением API-токена.
- `xlovo.py` содержит определения функций, необходимых для игры в Хлово.
- `words.txt` содержит допустимые слова.
- `suggestions.txt` содержит слова, предложенные к добавлению.

## Дополнительные использованные ресурсы
Для составления списка слов использовался список русских слов из [этого репозитория](https://github.com/danakt/russian-words) пользователя danakt.
~~~
MIT License

Copyright (c) 2020 Danakt Frost

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
~~~

Для обработки списка слов использовалась библиотека pymorphy2 с последующей частичной ручной проверкой.
