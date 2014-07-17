from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30, blank=False, default='')
    password = models.CharField(max_length=512, blank=False, default='')
    email = models.CharField(max_length=100, blank = False, default='')
    created_time = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = u'users';
        
class Client(models.Model):
    client_id = models.CharField(max_length=36, blank=False, default='')
    client_secret = models.CharField(max_length=512, blank=False, default='')
    client_desc = models.CharField(max_length = 512, blank=True, default='')
    created_time = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = u'clients';
        
class AccessToken(models.Model):
    user = models.ForeignKey(User, related_name="access_tokens_users")
    client = models.ForeignKey(Client, related_name='access_tokens_clients')
    
    access_token = models.CharField(max_length = 512, blank=False, default='')
    refresh_token = models.CharField(max_length = 36, blank=False, default='')
    last_gen_time = models.DateTimeField()
    expires = models.IntegerField(blank=False, default=1800)
    
    class Meta:
        db_table = u'accesstokens';
    