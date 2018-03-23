class DatabaseAppsRouter(object):

    def db_for_read(self, model, **hints):
        if model._meta.app_label  == 'logger':
            return 'logger'
        else:
            return 'default'
        return None
 
    # def db_for_write(self, model, **hints):
    #     """
    #     Point all operations on myapp models to 'other'
    #     """
    #     if model._meta.app_label == 'myapp2':
    #         return 'my_db_2'
    #     return None
 
    # def allow_syncdb(self, db, model):
    #     """
    #     Make sure the 'myapp2' app only appears on the 'other' db
    #     """
    #     if db == 'my_db_2':
    #         return model._meta.app_label == 'myapp2'
    #     elif model._meta.app_label == 'myapp2':
    #         return False
    #     return None