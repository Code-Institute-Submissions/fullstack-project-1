{"changed":true,"filter":false,"title":"settings.py","tooltip":"/fullstack/settings.py","value":"\"\"\"\nDjango settings for fullstack project.\n\nGenerated by 'django-admin startproject' using Django 1.11.24.\n\nFor more information on this file, see\nhttps://docs.djangoproject.com/en/1.11/topics/settings/\n\nFor the full list of settings and their values, see\nhttps://docs.djangoproject.com/en/1.11/ref/settings/\n\"\"\"\n\nimport os\nimport env\nimport  dj_database_url\n\n# Build paths inside the project like this: os.path.join(BASE_DIR, ...)\nBASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\n\n\n# Quick-start development settings - unsuitable for production\n# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/\n\n# SECURITY WARNING: keep the secret key used in production secret!\nSECRET_KEY = os.environ.get(\"SECRET_KEY\")\n\n# SECURITY WARNING: don't run with debug turned on in production!\nDEBUG = True\n\nALLOWED_HOSTS = [\"0fabdde0b8c444a2a3db4427fb5179dc.vfs.cloud9.us-west-2.amazonaws.com\"]\n\n\n# Application definition\n\nINSTALLED_APPS = [\n    'django.contrib.admin',\n    'django.contrib.auth',\n    'django.contrib.contenttypes',\n    'django.contrib.sessions',\n    'django.contrib.messages',\n    'django.contrib.staticfiles',\n    'django_forms_bootstrap',\n    'accounts',\n    'products',\n    'cart',\n    'checkout',\n    'storages',\n    'subscribe',\n]\n\nMIDDLEWARE = [\n    'django.middleware.security.SecurityMiddleware',\n    'django.contrib.sessions.middleware.SessionMiddleware',\n    'django.middleware.common.CommonMiddleware',\n    'django.middleware.csrf.CsrfViewMiddleware',\n    'django.contrib.auth.middleware.AuthenticationMiddleware',\n    'django.contrib.messages.middleware.MessageMiddleware',\n    'django.middleware.clickjacking.XFrameOptionsMiddleware',\n]\n\nROOT_URLCONF = 'fullstack.urls'\n\nTEMPLATES = [\n    {\n        'BACKEND': 'django.template.backends.django.DjangoTemplates',\n        'DIRS': [os.path.join(BASE_DIR, 'templates')],\n        'APP_DIRS': True,\n        'OPTIONS': {\n            'context_processors': [\n                'django.template.context_processors.debug',\n                'django.template.context_processors.request',\n                'django.contrib.auth.context_processors.auth',\n                'django.contrib.messages.context_processors.messages',\n                'django.template.context_processors.media',\n                'cart.contexts.cart_contents'\n            ],\n        },\n    },\n]\n\nWSGI_APPLICATION = 'fullstack.wsgi.application'\n\n\n# Database\n# https://docs.djangoproject.com/en/1.11/ref/settings/#databases\n\nif \"DATABASE_URL\" in os.environ:\n    DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}\nelse:\n    print(\"Database URL not found. Using SQLite instead\")\n    DATABASES = {\n        'default': {\n            'ENGINE': 'django.db.backends.sqlite3',\n            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),\n        }\n    }\n\n#DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}\n\n# Password validation\n# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators\n\nAUTH_PASSWORD_VALIDATORS = [\n    {\n        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',\n    },\n    {\n        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',\n    },\n    {\n        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',\n    },\n    {\n        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',\n    },\n]\n\nAUTHENTICATION_BACKENDS = [\n    'django.contrib.auth.backends.ModelBackend',\n    'accounts.backends.CaseInsensitiveAuth'\n]\n\n# Internationalization\n# https://docs.djangoproject.com/en/1.11/topics/i18n/\n\nLANGUAGE_CODE = 'en-us'\n\nTIME_ZONE = 'UTC'\n\nUSE_I18N = True\n\nUSE_L10N = True\n\nUSE_TZ = True\n\n\n# Static files (CSS, JavaScript, Images)\n# https://docs.djangoproject.com/en/1.11/howto/static-files/\n\n\nAWS_S3_OBJECT_PARAMETERS = {\n    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',\n    'CacheControl': 'max-age=94608000',\n}\n\nAWS_STORAGE_BUCKET_NAME = 'fullstack-project'\nAWS_S3_REGION_NAME = 'us-west-2'\nAWS_ACCESS_KEY_ID = os.environ.get(\"AWS_ACCESS_KEY_ID\")\nAWS_SECRET_ACCESS_KEY = os.environ.get(\"AWS_SECRET_ACCESS_KEY\")\n\nAWS_S3_CUSTOM_DOMAIN = '%s.s3-us-west-2.amazonaws.com'% AWS_STORAGE_BUCKET_NAME \n\nSTATICFILES_LOCATION = 'static/'\nSTATICFILES_STORAGE = 'custom_storages.StaticStorage'\n\nSTATIC_URL = '/static/'\nSTATICFILES_DIRS = (\n    os.path.join(BASE_DIR, \"static\"),\n    )\n\nMEDIAFILES_LOCATION = 'media'\nDEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'\n\nMEDIA_ROOT = os.path.join(BASE_DIR, 'media')\nMEDIA_URL = \"https://%s/%s/\" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)\n\nSTRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE')\nSTRIPE_SECRET = os.getenv('STRIPE_SECRET')\n\nMESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'","undoManager":{"mark":-2,"position":71,"stack":[[{"start":{"row":159,"column":23},"end":{"row":159,"column":63},"action":"remove","lines":["storages.backends.s3boto3.S3Boto3Storage"],"id":265},{"start":{"row":159,"column":23},"end":{"row":159,"column":24},"action":"insert","lines":["c"]},{"start":{"row":159,"column":24},"end":{"row":159,"column":25},"action":"insert","lines":["u"]},{"start":{"row":159,"column":25},"end":{"row":159,"column":26},"action":"insert","lines":["s"]},{"start":{"row":159,"column":26},"end":{"row":159,"column":27},"action":"insert","lines":["t"]},{"start":{"row":159,"column":27},"end":{"row":159,"column":28},"action":"insert","lines":["o"]},{"start":{"row":159,"column":28},"end":{"row":159,"column":29},"action":"insert","lines":["m"]},{"start":{"row":159,"column":29},"end":{"row":159,"column":30},"action":"insert","lines":["e"]},{"start":{"row":159,"column":30},"end":{"row":159,"column":31},"action":"insert","lines":["r"]}],[{"start":{"row":159,"column":30},"end":{"row":159,"column":31},"action":"remove","lines":["r"],"id":266},{"start":{"row":159,"column":29},"end":{"row":159,"column":30},"action":"remove","lines":["e"]}],[{"start":{"row":159,"column":29},"end":{"row":159,"column":30},"action":"insert","lines":["_"],"id":267},{"start":{"row":159,"column":30},"end":{"row":159,"column":31},"action":"insert","lines":["s"]},{"start":{"row":159,"column":31},"end":{"row":159,"column":32},"action":"insert","lines":["o"]}],[{"start":{"row":159,"column":31},"end":{"row":159,"column":32},"action":"remove","lines":["o"],"id":268}],[{"start":{"row":159,"column":31},"end":{"row":159,"column":32},"action":"insert","lines":["t"],"id":269}],[{"start":{"row":159,"column":23},"end":{"row":159,"column":32},"action":"remove","lines":["custom_st"],"id":270},{"start":{"row":159,"column":23},"end":{"row":159,"column":38},"action":"insert","lines":["custom_storages"]}],[{"start":{"row":159,"column":38},"end":{"row":159,"column":39},"action":"insert","lines":["."],"id":271},{"start":{"row":159,"column":39},"end":{"row":159,"column":40},"action":"insert","lines":["S"]},{"start":{"row":159,"column":40},"end":{"row":159,"column":41},"action":"insert","lines":["t"]},{"start":{"row":159,"column":41},"end":{"row":159,"column":42},"action":"insert","lines":["a"]},{"start":{"row":159,"column":42},"end":{"row":159,"column":43},"action":"insert","lines":["t"]},{"start":{"row":159,"column":43},"end":{"row":159,"column":44},"action":"insert","lines":["i"]},{"start":{"row":159,"column":44},"end":{"row":159,"column":45},"action":"insert","lines":["c"]},{"start":{"row":159,"column":45},"end":{"row":159,"column":46},"action":"insert","lines":["S"]}],[{"start":{"row":159,"column":39},"end":{"row":159,"column":46},"action":"remove","lines":["StaticS"],"id":272},{"start":{"row":159,"column":39},"end":{"row":159,"column":52},"action":"insert","lines":["StaticStorage"]}],[{"start":{"row":103,"column":0},"end":{"row":103,"column":1},"action":"insert","lines":["#"],"id":273}],[{"start":{"row":101,"column":0},"end":{"row":101,"column":1},"action":"remove","lines":["#"],"id":274}],[{"start":{"row":100,"column":0},"end":{"row":100,"column":1},"action":"remove","lines":["#"],"id":275}],[{"start":{"row":99,"column":0},"end":{"row":99,"column":1},"action":"remove","lines":["#"],"id":276}],[{"start":{"row":98,"column":0},"end":{"row":98,"column":1},"action":"remove","lines":["#"],"id":277}],[{"start":{"row":97,"column":0},"end":{"row":97,"column":1},"action":"remove","lines":["#"],"id":278}],[{"start":{"row":96,"column":0},"end":{"row":96,"column":1},"action":"remove","lines":["#"],"id":279}],[{"start":{"row":95,"column":0},"end":{"row":95,"column":1},"action":"remove","lines":["#"],"id":280}],[{"start":{"row":94,"column":0},"end":{"row":94,"column":1},"action":"remove","lines":["#"],"id":281}],[{"start":{"row":93,"column":0},"end":{"row":93,"column":1},"action":"remove","lines":["#"],"id":282}],[{"start":{"row":92,"column":0},"end":{"row":92,"column":1},"action":"remove","lines":["#"],"id":283}],[{"start":{"row":103,"column":0},"end":{"row":103,"column":1},"action":"remove","lines":["#"],"id":284}],[{"start":{"row":101,"column":0},"end":{"row":101,"column":1},"action":"insert","lines":["#"],"id":285}],[{"start":{"row":100,"column":0},"end":{"row":100,"column":1},"action":"insert","lines":["#"],"id":286}],[{"start":{"row":99,"column":0},"end":{"row":99,"column":1},"action":"insert","lines":["#"],"id":287}],[{"start":{"row":98,"column":0},"end":{"row":98,"column":1},"action":"insert","lines":["#"],"id":288}],[{"start":{"row":97,"column":0},"end":{"row":97,"column":1},"action":"insert","lines":["#"],"id":289}],[{"start":{"row":96,"column":0},"end":{"row":96,"column":1},"action":"insert","lines":["#"],"id":290}],[{"start":{"row":95,"column":0},"end":{"row":95,"column":1},"action":"insert","lines":["#"],"id":291}],[{"start":{"row":94,"column":0},"end":{"row":94,"column":1},"action":"insert","lines":["#"],"id":292}],[{"start":{"row":92,"column":0},"end":{"row":92,"column":1},"action":"insert","lines":["#"],"id":293}],[{"start":{"row":93,"column":0},"end":{"row":93,"column":1},"action":"insert","lines":["#"],"id":294}],[{"start":{"row":161,"column":13},"end":{"row":161,"column":23},"action":"remove","lines":["'/static/'"],"id":295},{"start":{"row":161,"column":13},"end":{"row":161,"column":75},"action":"insert","lines":["\"https://%s/%s/\" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)"]}],[{"start":{"row":161,"column":59},"end":{"row":161,"column":60},"action":"remove","lines":["A"],"id":296},{"start":{"row":161,"column":58},"end":{"row":161,"column":59},"action":"remove","lines":["I"]},{"start":{"row":161,"column":57},"end":{"row":161,"column":58},"action":"remove","lines":["D"]},{"start":{"row":161,"column":56},"end":{"row":161,"column":57},"action":"remove","lines":["E"]}],[{"start":{"row":161,"column":55},"end":{"row":161,"column":56},"action":"remove","lines":["M"],"id":297}],[{"start":{"row":161,"column":55},"end":{"row":161,"column":56},"action":"insert","lines":["S"],"id":298},{"start":{"row":161,"column":56},"end":{"row":161,"column":57},"action":"insert","lines":["T"]},{"start":{"row":161,"column":57},"end":{"row":161,"column":58},"action":"insert","lines":["A"]},{"start":{"row":161,"column":58},"end":{"row":161,"column":59},"action":"insert","lines":["T"]},{"start":{"row":161,"column":59},"end":{"row":161,"column":60},"action":"insert","lines":["I"]},{"start":{"row":161,"column":60},"end":{"row":161,"column":61},"action":"insert","lines":["C"]}],[{"start":{"row":161,"column":13},"end":{"row":161,"column":76},"action":"remove","lines":["\"https://%s/%s/\" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)"],"id":299},{"start":{"row":161,"column":13},"end":{"row":161,"column":14},"action":"insert","lines":["?"]}],[{"start":{"row":161,"column":13},"end":{"row":161,"column":14},"action":"remove","lines":["?"],"id":300}],[{"start":{"row":161,"column":13},"end":{"row":161,"column":15},"action":"insert","lines":["''"],"id":301}],[{"start":{"row":161,"column":14},"end":{"row":161,"column":15},"action":"insert","lines":["s"],"id":302},{"start":{"row":161,"column":15},"end":{"row":161,"column":16},"action":"insert","lines":["t"]},{"start":{"row":161,"column":16},"end":{"row":161,"column":17},"action":"insert","lines":["a"]},{"start":{"row":161,"column":17},"end":{"row":161,"column":18},"action":"insert","lines":["t"]},{"start":{"row":161,"column":18},"end":{"row":161,"column":19},"action":"insert","lines":["c"]}],[{"start":{"row":161,"column":18},"end":{"row":161,"column":19},"action":"remove","lines":["c"],"id":303}],[{"start":{"row":161,"column":18},"end":{"row":161,"column":19},"action":"insert","lines":["i"],"id":304},{"start":{"row":161,"column":19},"end":{"row":161,"column":20},"action":"insert","lines":["c"]}],[{"start":{"row":161,"column":14},"end":{"row":161,"column":15},"action":"insert","lines":["/"],"id":305}],[{"start":{"row":161,"column":21},"end":{"row":161,"column":22},"action":"insert","lines":["/"],"id":306}],[{"start":{"row":156,"column":29},"end":{"row":156,"column":30},"action":"insert","lines":["-"],"id":307},{"start":{"row":156,"column":30},"end":{"row":156,"column":31},"action":"insert","lines":["u"]},{"start":{"row":156,"column":31},"end":{"row":156,"column":32},"action":"insert","lines":["s"]}],[{"start":{"row":156,"column":32},"end":{"row":156,"column":33},"action":"insert","lines":["-"],"id":308},{"start":{"row":156,"column":33},"end":{"row":156,"column":34},"action":"insert","lines":["w"]},{"start":{"row":156,"column":34},"end":{"row":156,"column":35},"action":"insert","lines":["e"]},{"start":{"row":156,"column":35},"end":{"row":156,"column":36},"action":"insert","lines":["s"]},{"start":{"row":156,"column":36},"end":{"row":156,"column":37},"action":"insert","lines":["t"]}],[{"start":{"row":156,"column":37},"end":{"row":156,"column":38},"action":"insert","lines":["-"],"id":309},{"start":{"row":156,"column":38},"end":{"row":156,"column":39},"action":"insert","lines":["2"]}],[{"start":{"row":158,"column":24},"end":{"row":158,"column":25},"action":"insert","lines":["/"],"id":310}],[{"start":{"row":158,"column":31},"end":{"row":158,"column":32},"action":"insert","lines":["/"],"id":311}],[{"start":{"row":158,"column":24},"end":{"row":158,"column":25},"action":"remove","lines":["/"],"id":312}],[{"start":{"row":158,"column":30},"end":{"row":158,"column":31},"action":"remove","lines":["/"],"id":313}],[{"start":{"row":158,"column":30},"end":{"row":158,"column":31},"action":"insert","lines":["/"],"id":314}],[{"start":{"row":156,"column":53},"end":{"row":156,"column":54},"action":"remove","lines":[" "],"id":315}],[{"start":{"row":92,"column":0},"end":{"row":92,"column":1},"action":"remove","lines":["#"],"id":316}],[{"start":{"row":93,"column":0},"end":{"row":93,"column":1},"action":"remove","lines":["#"],"id":317}],[{"start":{"row":94,"column":0},"end":{"row":94,"column":1},"action":"remove","lines":["#"],"id":318}],[{"start":{"row":95,"column":0},"end":{"row":95,"column":1},"action":"remove","lines":["#"],"id":319}],[{"start":{"row":96,"column":0},"end":{"row":96,"column":1},"action":"remove","lines":["#"],"id":320}],[{"start":{"row":97,"column":0},"end":{"row":97,"column":1},"action":"remove","lines":["#"],"id":321}],[{"start":{"row":98,"column":0},"end":{"row":98,"column":1},"action":"remove","lines":["#"],"id":322}],[{"start":{"row":99,"column":0},"end":{"row":99,"column":1},"action":"remove","lines":["#"],"id":323}],[{"start":{"row":100,"column":0},"end":{"row":100,"column":1},"action":"remove","lines":["#"],"id":324}],[{"start":{"row":101,"column":0},"end":{"row":101,"column":1},"action":"remove","lines":["#"],"id":325}],[{"start":{"row":103,"column":0},"end":{"row":103,"column":1},"action":"insert","lines":["#"],"id":326}],[{"start":{"row":46,"column":15},"end":{"row":47,"column":0},"action":"insert","lines":["",""],"id":327},{"start":{"row":47,"column":0},"end":{"row":47,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":47,"column":4},"end":{"row":47,"column":6},"action":"insert","lines":["''"],"id":328}],[{"start":{"row":47,"column":5},"end":{"row":47,"column":6},"action":"insert","lines":["p"],"id":329},{"start":{"row":47,"column":6},"end":{"row":47,"column":7},"action":"insert","lines":["o"]},{"start":{"row":47,"column":7},"end":{"row":47,"column":8},"action":"insert","lines":["s"]},{"start":{"row":47,"column":8},"end":{"row":47,"column":9},"action":"insert","lines":["t"]},{"start":{"row":47,"column":9},"end":{"row":47,"column":10},"action":"insert","lines":["a"]},{"start":{"row":47,"column":10},"end":{"row":47,"column":11},"action":"insert","lines":["s"]}],[{"start":{"row":47,"column":10},"end":{"row":47,"column":11},"action":"remove","lines":["s"],"id":330},{"start":{"row":47,"column":9},"end":{"row":47,"column":10},"action":"remove","lines":["a"]}],[{"start":{"row":47,"column":9},"end":{"row":47,"column":10},"action":"insert","lines":["s"],"id":331}],[{"start":{"row":47,"column":11},"end":{"row":47,"column":12},"action":"insert","lines":["<"],"id":332}],[{"start":{"row":47,"column":11},"end":{"row":47,"column":12},"action":"remove","lines":["<"],"id":333}],[{"start":{"row":47,"column":11},"end":{"row":47,"column":12},"action":"insert","lines":[","],"id":334}],[{"start":{"row":47,"column":5},"end":{"row":47,"column":10},"action":"remove","lines":["posts"],"id":335},{"start":{"row":47,"column":5},"end":{"row":47,"column":6},"action":"insert","lines":["s"]},{"start":{"row":47,"column":6},"end":{"row":47,"column":7},"action":"insert","lines":["u"]},{"start":{"row":47,"column":7},"end":{"row":47,"column":8},"action":"insert","lines":["b"]},{"start":{"row":47,"column":8},"end":{"row":47,"column":9},"action":"insert","lines":["s"]},{"start":{"row":47,"column":9},"end":{"row":47,"column":10},"action":"insert","lines":["c"]},{"start":{"row":47,"column":10},"end":{"row":47,"column":11},"action":"insert","lines":["r"]},{"start":{"row":47,"column":11},"end":{"row":47,"column":12},"action":"insert","lines":["i"]},{"start":{"row":47,"column":12},"end":{"row":47,"column":13},"action":"insert","lines":["b"]},{"start":{"row":47,"column":13},"end":{"row":47,"column":14},"action":"insert","lines":["e"]}],[{"start":{"row":86,"column":0},"end":{"row":91,"column":2},"action":"remove","lines":["#DATABASES = {","#    'default': {","#        'ENGINE': 'django.db.backends.sqlite3',","#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","#    }","#}"],"id":336},{"start":{"row":85,"column":0},"end":{"row":86,"column":0},"action":"remove","lines":["",""]},{"start":{"row":84,"column":64},"end":{"row":85,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":96,"column":0},"end":{"row":96,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1581285774420}