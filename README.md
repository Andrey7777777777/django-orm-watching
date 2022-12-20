
 # Пульт охраны банка
 Пульт охраны - это сайт, который можно подключить к удаленной базе данных с визитами и карточками пропуска сотрудников банка.

 ### Как установить
 Python3 должен быть уже установлен. 
 Затем используйте `pip` (или `pip3`) для установки зависимостей:
 ```
 pip install -r requirements.txt
 ```
 Параметры подлючения к БД находятся в файле `.env`. Создайте и заполните.
 `DB_HOST` - IP адрес или доменное имя БД
 
 `DB_PORT` - Порт БД
 
 `DB_NAME` - Имя БД
 
 `DB_USER` - Имя пользователя БД
 
 `DB_PASSWORD` - Пароль пользователя БД
 
 `'SECRET_KEY'` - Секретный ключ, при желании можно поменять на ваш

 При желании, для включения отладочной системы в файле .env дабавляем следующую нажпись:
 ```
 DEBUG=True
```
По умолчанию DEBUG отключен


 ### Как запустить
 ```
 python manage.py runserver 0.0.0.0:8000
 ```
 Открыть в браузере http://0.0.0.0:8000/

 ### Цель проекта
 Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
