# Форматирование цены


Скрипт превращает данные о цене из базы данных `20500.00` в строку формата `20 500`

Запускается как отдельный модуль и как самостоятельная программа

```python
'20500'     # 20 500
 20500.00   # 20 500
 20500.55   # 20 500.55
 2          # 2
'2000,60'   # None
'dsdsd'     # None
```
### Пример работы срипта

```bash
> python format_price.py 20500.00
20 500
```
# Требования
Совестимые OC:
* Linux,
* Windows
* MacOS

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5 выше

# Как работать
> Запуск в командной строке для всех ОС одинаковый
Стандатной командой `python` (на некоторых компьютерах `python3`).
```bash
$ python format_price.py [-h] price

positional arguments:
  price       Напишите цену товара

optional arguments:
  -h, --help  show this help message and exit

```

> Использоваение модуля внутри программы

```python
from format_price import format_price

my_price = format_price('4435653.333')
print(my_price)
# 4 435 653.333

```

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
