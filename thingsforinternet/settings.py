# -*- coding: utf-8 -*-

# Django settings for thingsforinternet project.
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

BASE_DIR = os.path.dirname(__file__)

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(BASE_DIR, 'thingsforinternet.db3').replace('\\', '/'),                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'zh-cn'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static').replace('\\', '/')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'global_static').replace('\\', '/'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '4r*s+98oelyas_pp(macb%gy=8#$#qt(^si_id#7731b%@+xj1'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'mobileesp.middleware.MobileDetectionMiddleware',
    'mobi.middleware.MobileDetectionMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
)

ROOT_URLCONF = 'thingsforinternet.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'thingsforinternet.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates').replace('\\', '/'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'south',
    'markdown_deux',
    'thingsforinternet',
    'accounts',
    'dh',
    'resume',
    'huntjob',
    'interview',
    'offer',
    'exchange',
    'resources',
    'lab',
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

COOKIE_MAX_AGE = 1 * 30 * 24 * 60 * 60  # one month

# 搜索设置
SEARCH_ENGINE = {
    'google': 'https://www.google.com/search?q=%s',
    'bing': 'http://cn.bing.com/search?q=%s',
    'baidu': 'http://www.baidu.com/s?wd=%s&ie=utf-8',
    'sof': 'http://stackoverflow.com/search?q=%s',
}

# 分页设置
SITE_PER_PAGE = 20
TIPS_PER_PAGE = 99

# 验证码设置
GEE_TEST = {
    'base_url': 'api.geetest.com/get.php?gt=',

    'captcha_id': 'a40fd3b0d712165c5d13e6f747e948d4',
    'private_key': '0f1a37e33c9ed10dd2e133fe2ae9c459',

    # 嵌入式
    # 'product': 'embed',

    # 浮动式
    'product': 'float',

    # 弹出式
    # 'product': 'popup&popupbtnid=submit-button',
}

# 邮件设置
SEND_EMAIL = {
    'username': 'kimi.huang@tt4it.com',
    'password': 'tt4it'
}

# 七牛设置
QINIU = {
    'domain': 'http://7xnqhw.com1.z0.glb.clouddn.com/',
    'access_key': 'm7C_7pGrIvY8tfaYKkYBwfpjGAv7A4ahtMUyrHHp',
    'secret_key': 'hmSPYHvmA2QBJYZk-1hD_w3nyffybERpkwIfdc-t',
    'bucket': 'tt4it',
}

# 图片压缩设置
PNG_QUANT_PATH = '/home/diors/work/pngquant/pngquant'
QUANT_IMG_PATH = '/home/diors/work/pngquant/quant/'

BEFORE_QUANT = '%s{0}.png' % (QUANT_IMG_PATH, )
AFTER_QUANT = '%s{0}_quant.png' % (QUANT_IMG_PATH, )

QUANT_CMD = r'%s --quality=65-80 %s{0}.png --force --ext _quant.png' % (PNG_QUANT_PATH, QUANT_IMG_PATH)

try:
    from local_settings import *
except ImportError:
    pass
