# test_blog_py

Отредактируйте файл settings.py, укажите логин и пароль для почтового ящика

```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py loaddata db-init
'''

База будет инициирована и в ней будет два пользователя user1, user2 c паролями 'user1user1' и 'user2user2' соответственно.
Этим пользователям нужно в админке указать email.
