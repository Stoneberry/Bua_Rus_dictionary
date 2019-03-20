# Bua_Rus_dictionary

* Элекстронный словарь бурятского языка.
* Источник - НКРЯ (параллельный корпус)
* Подготовили - Анастасия Костяницына, Артем Копецкий

Электронный словарь формируется автоматически на основе параллельного корпуса НКРЯ. 

#### Код: 
* RUSCORPORA_parser:
  - Обработка НКРЯ (API): программа делает запросы русских слов в НКРЯ, получает пары: русский текст и бурятский текст, в которых встретилось слово и грамматический разбор всех слов в этих предложениях.
  - Полученные данные оформляются в структуру Entry, которая хранит в себе лемму на бурятском языке, возможные части речи для этой леммы, переводы на русский язык и примеры (пары: русский текст и бурятский текст, информацию об источнике бурятского текста).
* TEI parser - Обарабатывает все Entry для каждого слова, создает словарь и записывает его в формате tei. 
* flask_dict - сайт словаря.



Сайт: http://stonewebsite.pythonanywhere.com/
