# Парсер документации Python при помощи Scrapy

Асинхронный парсер документации (PEP) с сайта http://peps.python.org/. 
Собранная информация сохраняется в csv-файлы: 
* Список стандартов PEP в формате - Номер PEP, Наименование, Статус.
* Количество стандартов PEP вообще и в разрезе статусов.


## Установка и запуск

Клонируйте проект:
```
git clone git@github.com:vavilovnv/scrapy_parser_pep.git
```

Создайте виртуальное окружение:
```
python3 -m venv venv
```

Активируйте venv:
```
. /venv/bin/activate
```

Установите зависимости:
```
pip install -r requirements.txt
```

Запустите парсинг сайта при помощи spider с именем pep:
```
scrapy crawl pep
```

