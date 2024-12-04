> https://docs.djangoproject.com/en/5.1/topics/db/multi-db/
1. Configurar base de datos opcional a conectar
> proyecto/settings.py
```
'local': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
```

2. Crear archivo dbrouters.py e internamente una clase DBRouters
> https://docs.djangoproject.com/en/5.1/topics/db/multi-db/#topics-db-multi-db-routing

