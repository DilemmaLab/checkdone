# checkdone
Simple To-Do Service

Использованные framework'и:
1) Django - основной, front- и back-end. 
2) Bootstrap - стили.
База данных - MySQL.

Работа над проектом.
# 1. Установка и настройка основных компонентов.
1.1. LAMP (Linux Apache(2), MySQL-Server, PHP(5)):
$ sudo apt-get install lamp-server^
1.2. Python-Django и Python-MySQL:
$ sudo apt-get install python-django
$ sudo apt-get install python-mysqldb
1.3. mod_wsgi (для запуска Django-проекта под Apache):
$ sudo apt-get install libapache2-mod-wsgi

# 2. Django-проект.
	2.1. Создаем Django-Project:
		 ~ $ mkdir DjangoProjects
		 ~ $ mv DjangoProjects PycharmProjects/
		 ~ $ cd PycharmProjects/DjangoProjects/
		 ~/PycharmProjects/DjangoProjects $ django-admin startproject checkdone
		 ~/PycharmProjects/DjangoProjects $ cd checkdone/
		 ~/PycharmProjects/DjangoProjects/checkdone $ python manage.py migrate
	
	Можем создать администратора в Sqlite3.db (не обязательно, он не мигрирует на MySQL):
		 ~/PycharmProjects/DjangoProjects/checkdone $ python manage.py createsuperuser
		 ~/PycharmProjects/DjangoProjects/checkdone $ python manage.py shell
		>>> from django.contrib.auth.models import User
		>>> User.objects.get(username="root", is_superuser=True).delete()
			(1, {u'auth.User': 1, u'admin.LogEntry': 0, u'auth.User_groups': 0, u'auth.User_user_permissions': 0})

	2.2. Переходим на MySQL. Создаем БД и администратора:
	~ $ mysql -u root -p***
	mysql> CREATE DATABASE django_db;
  mysql> CREATE USER IF NOT EXISTS 'dj_root'@'localhost' IDENTIFIED BY '***';
  mysql> GRANT ALL PRIVILEGES ON django_db.* TO 'dj_root'@'localhost';
  В файле settings.py включаем поддержку MySQL:
			 ~/PycharmProjects/DjangoProjects/checkdone $ gedit  checkdone/settings.py
			DATABASES = {
			    'default': {
			        'ENGINE': 'django.db.backends.mysql',
			        'NAME': 'django_db',
			        'USER': 'root',
			        'PASSWORD': '******',
			        'HOST': '',	# Set to empty string for localhost. Not used with sqlite3.
			        'PORT': '',	# Set to empty string for default. Not used with sqlite3.
			    }
			}
	
	2.3. Осуществляем миграцию:
	~/PycharmProjects/DjangoProjects/checkdone $ python manage.py migrate
	
	2.4. Создаем приложение todos:
    ~/PycharmProjects/DjangoProjects/checkdone $ python manage.py startapp todos
    
	2.5. Подключаем наше приложение к прочим:
  	INSTALLED_APPS = [
      ...,
      'todos',
      ...,
    ]
    
  2.6. Создаем модель Todo в models.py. Затем:
  $ python manage.py makemigrations todos
  $ python manage.py migrate
  
  2.7. Подключаем доступ к модели через интерфейс администратора:
      в admin.py:
        admin.site.register(Todo)
        
  2.8. Создаем собственную форму в forms.py.
  2.9. Создаем необходимые функции добавления, вывода, удаления и поиска контента в views.py.
  2.10. Прописываем все необходимые url'ы в urls.py.
  2.11. Создаем базовый шаблон index.html в templates/basic, в нем подключаем все библиотеки; создаем шаблоны вывода всех данных из модели (todo.html), добавления новой задачи (add.html), формы поиска (search_form.html), собственной страницы 404. Отдельно создаем шаблон вывода результатов поиска (search_result.html), поскольку в нем мы будем использовать подсветку найденных слов для удобства пользователя.
  
  2.12. Прописываем необходимые сведения для поиска сервером static-файлов .css и .js:
	  INSTALLED_APPS = [
    ...,
    'django.contrib.staticfiles',
    ...,
    ]
    ...
    STATIC_ROOT = os.path.join(BASE_DIR, '/static')
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "checkdone/templates/static"),
        'checkdone/templates/static',
    ]
    
  2.13. Создаем собственные фильтры для обработки вывода результатов поиска (todos_extras.py) и включаем их в settings.py:
  INSTALLED_APPS = [
    ...,
    'todos.templatetags.todos_extras',
  ]

3. Подготовка в релиз:
3.1. Меняем в settings.py
	3.1.1. Выключаем вывод ошибок (Debugg-mode):
			DEBUG = False
      Кстати, мы это делаем не только из соображений безопасности, но и потому, что наша красивая custom'ная страница 404 не будет отображаться в debug-mode.
	3.1.2. Разрешаем любые хосты:
			ALLOWED_HOSTS = ['*']
-------------------------------------------------------------------------------------------------------------------------------
Currently we have following Unresolved Problematic Issues in our project:
1) When we set up new task with DoneDate custom value, entered by user in "Done on date" field, DoneDate variable still defines with None-value, and not with user custom input. Therefore, even if we (or user) customizes "Done on date" with date, different from current one, and check "Done", we still receive done task with current date (produced from timezone.now()-function). It's very weird behaviour and currently is not explained. Note: Probably, problem could occurs in Form-implementation or in implementation of Template "Done on date" field, because View.add_new receives already None-value. 
2) We don't have Ajax-technology on our site (and mostly Jquery as well) - they're in plans, but currently Ajax and Jquery are not implemented. (Sorry, I know, it was required option, but trying to do my best and implement good service, I had no time to implement it - in other case either I would pass the deadline, or made much buggy service). 3) Also, User Account options - Registration, Login/logout, Settings, as well as its technical issues like Sessions, Cookies, Password encryption (md5-hash with salt) - are not implemented yet. 
4) Implemented Search-service at site do not handle with Cyrillic symbols, although DataBase and all of its tables are "ALTER" setted up with default "CHARSET" as "utf8" and "COLLATE" as "utf8_general_ci" (and currently this behaviour is not explained). 
5) Currently there is no following options here on site: -- no ascend/descend ordering on fields; -- no availability to change Text, Details, Deadline and Progress of submitted tasks, as well as DoneDate and Done-status of task, already checked as done. 
6) Also, view of Details, implemented with Bootstrap "dropdown-menu" is not very useful, because it have troubles with Copying content-text and doesn't support adequate Formatting of text (like <b>bold</b> and <br>, \n and &para; new-line symbols), so it should be better re-implemented.
Issue (5) is really simple, and I know how to implement it, but didn't want to break the deadline. May be something also, but now it's all discovered.
