import os

SECRET_KEY = '0338ae10aa8322fbc08ace06a6336eeee1146d8697511c3bf95fc568bbaf2825'

MYSQL_USER = 'std_2072_exam'
MYSQL_PASSWORD = 'qwerty1234'
MYSQL_HOST = 'std-mysql.ist.mospolytech.ru'
MYSQL_DATABASE = 'std_2072_exam'

ADMIN_ROLE_ID = 1
MODER_ROLE_ID = 2
USER_ROLE_ID = 3
# путь к сохранению обложек
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'media', 'images')