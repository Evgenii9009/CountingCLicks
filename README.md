# Обрезка ссылок с помощью Битли
Скрипт служит для работы со ссылками. При вводе ссылки он выводит её укороченную версию, а в случае введения уже укороченной сылки выведет статистику переходов по ней.

### Как установить

Вам потребуется сервисный токен API VK, его можно получить, создав приложение по [ссылке](https://id.vk.com/about/business/go/docs/ru/vkid/latest/vk-id/connection/create-application)

Токен необходимо добавить в переменную окружения 'VKAPI_TOKEN'


Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
Рекомендуется использовать [virtualenv\venv](https://docs.python.org/3/library/venv.html)


#### Пример запуска скрипта с обычной ссылкой:

`python main.py --name https://dvmn.org/modules/web-api/lesson/migration-from-website`

![Screenshot from 2024-11-29 12-39-35](https://github.com/user-attachments/assets/863dbcb6-30f3-4cef-8a31-5e939979d6e9)

#### Пример запуска скрипта с уже укороченной ссылкой:

`python main.py --name https://vk.cc/cx80Y1`

![Screenshot from 2024-11-29 12-44-36](https://github.com/user-attachments/assets/53424f9c-8127-4df4-8395-e5e892ac0dfb)


Рекомендуется использовать [virtualenv\venv](https://docs.python.org/3/library/venv.html)

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
