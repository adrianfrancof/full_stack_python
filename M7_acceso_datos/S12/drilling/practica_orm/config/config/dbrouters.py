class DBRouter:

    def db_for_read(self, model, **hints):

        if model._meta.app_label == 'producto':
            return 'default'
        return None

    def db_for_write(self, model, **hints):

        if model._meta.app_label == 'producto':
            return 'default'
        return None

    def allow_relation(self, obj1, obj2, **hints):

        if obj1._state.db == 'default' and obj2._state.db == 'default':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):

        if db == 'default':
            return app_label == 'producto'
        return None