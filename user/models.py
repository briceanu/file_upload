from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):

    user_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    # cvs is the name of the folder where the file will be stored
    # "user_cv": "http://localhost:8000/media/cvs/learning.py",
    user_cv = models.FileField(upload_to='cvs',null=True,blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
