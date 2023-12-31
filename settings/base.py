from pathlib import Path
import sys
import os


# Хранит в себе ПОЛНЫЙ путь до проекта
BASE_DIR = Path(__file__).resolve().parent.parent
# C://Program Files/Django
sys.path.append(BASE_DIR)
# C://Program Files/Django/apps
sys.path.append(os.path.join(BASE_DIR, 'apps'))

# Ключ за деплоя
SECRET_KEY = 'django-insecure-&*m8tm2t*(f&c2ep2yntic!x^+$3$xf)=_@c)dt&v%qxmz7erp'

# Режим дебага
DEBUG = True

# Все разрешённые хосты
ALLOWED_HOSTS = []

# Установленные приложения
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'products.apps.ProductsConfig'
]

# Промежуточные слои
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Путь до файла urls.py
ROOT_URLCONF = 'settings.urls'

# Настройка шаблонов. html файлы
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Путь до файла wsgi.py
WSGI_APPLICATION = 'settings.wsgi.application'

# Текущая рабочая для проекта база данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Язык приложение
LANGUAGE_CODE = 'ru-RU'

# Время
TIME_ZONE = 'Asia/Almaty'

# Не знаю
USE_I18N = True

# Используем ли timezone
USE_TZ = True

# Путь до статичных файлов
STATIC_URL = 'static/'

# Шайтан штука
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'