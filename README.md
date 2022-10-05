# Сервис FoodPlan

Роман и Лариса за долгое время у них накопили большую библиотеку рецептов в 
Instagram. Их рецепты нравятся многим, и у них собралось довольно много 
поклонников. Для монетизации этого капитала решено сделать свой сайт с рецептами
по подписке. Чтобы он не  был “очередным”, сайт будет не просто выдавать 
рецепты, а ещё и возьмёт на себя много работ по планированию рациона, затратам
на еду, диетам и так далее. На данный момент важно быстро запустить какой-то 
прототип, чтобы начать работы. Если на услугу будет спрос, сервис начнут активно
спонсировать и развивать.

Сайт будет предлагать рецепты Романа и Ларисы, с которыми пользователь уже 
знаком. Чтобы избавиться от фрустрации от выбора среди сотен рецептов — сайт 
будет выбирать рецепты за пользователя, а тот уже по итогу скажет, понравилось 
ему или нет. Сайт соберёт список покупок, подстроится под диету и аллергии и 
так далее. Короче, за небольшое вознаграждение (около 100 руб. в месяц) избавит
пользователей от кучи проблем с планированием рациона.

## Запуск

- Рекомендуется использовать виртуальное окружение для запуска проекта
- Для корректной работы Вам необходим Python версии 3.6 и выше
- Скачайте код
- Установите зависимости командой `pip install -r requirements.txt`
- Создайте файл базы данных и сразу примените все миграции командой `python3 manage.py migrate`
- Запустите сервер командой `python3 manage.py runserver`

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, 
создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком 
формате: `ПЕРЕМЕННАЯ=значение`.

Доступные переменные:
- `DEBUG` — дебаг-режим. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта
- `ALLOWED_HOSTS` — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts).

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
