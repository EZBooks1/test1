# Generated by Django 2.2.6 on 2019-10-23 01:27

from django.db import migrations


class Migration(migrations.Migration):

   dependencies = 
   [
      ('users', '0005_auto_20191022_2018'),
   ]

   operations = 
   [
      migrations.RemoveField
      (
         model_name='user_profile',
         name='is_staff',
      ),
   ]