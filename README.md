# Скрипт для улучшения успеваемости в электронном дневнике

## Описание

Этот скрипт предназначен для автоматизации улучшения успеваемости школьников в электронном дневнике. Он позволяет:

*   Исправлять плохие оценки (2 и 3) на хорошие (5).
*   Удалять замечания от учителей.
*   Добавлять похвалу от учителя за последний урок по предмету.


## Требования

*   Для работы скрипта понадобится файл БД и развернутый сайт
<!-- *   Адрес сайта http://127.0.0.1:8000/ -->
*   Python 3.7 или выше
*   Django (версия, совместимая с вашим проектом электронного дневника)


## Установка

1.  Установите Python 3.
2.  Установите Django:

```bash
pip install Django
```

    Убедитесь, что установленная версия Django совместима с вашим проектом электронного дневника.
3.  Загрузите файлы скрипта (my_script.py) в папку вашего Django проекта.


## Использование

1.  Откройте консоль сервера, на котором запущен ваш Django проект.
2.  Запустите Django shell:

```bash
python manage.py shell
```
3.  Импортируйте нужные модели:
```bash
from datacenter.models import Schoolkid, Mark, Chastisement, Lesson, Commendation
```
4. Имортируйте модуль:
```bash
import random
```

5.  В блоке:
``` 
if __name__ == "__main__":
``` 
Найдите переменную `child`, замените "Фролов Иван" на имя ученика, успеваемость которого вы хотите улучшить и скопируйте ёё в Django shell:

```bash
child = Schoolkid.objects.get(full_name__contains="Фролов Иван")
```

## Описание функций

 Для исправления оценок используйте функцию ` fix_marks ` с аргументом `child`, скопируйте в Django shell:

```bash
fix_marks(child)
```

Чтобы удалить все замечания ученика используйте функцию `remove_chastisements` с аргументом `child`,  скопируйте в Django shell:

```bash
remove_chastisements(child)
```

Для создания похвалы ученика по указанному предмету используйте функцию `create_commendation` с аргументами `child` и `subject_name`: строка с названием предмета (например, `"Математика"`), скопируйте в Django shell:

```bash
create_commendation(child, "Математика")
```

## Пример вывода консоли (краткий):
* Ученик: Фролов Иван
* Исправлено оценок: 2
* Удалено замечаний: 1
* Похвала создана!


## Дополнительная информация

*   **Официальная документация Django:**  [https://docs.djangoproject.com/](https://docs.djangoproject.com/)


## Дисклеймер

Данный скрипт разработан в образовательных целях

