# Generated by Django 5.0.3 on 2024-03-25 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaignmanagment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newcampaignmodel',
            name='age_group',
        ),
        migrations.RemoveField(
            model_name='newcampaignmodel',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='newcampaignmodel',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='newcampaignmodel',
            name='location',
        ),
        migrations.RemoveField(
            model_name='newcampaignmodel',
            name='platform',
        ),
    ]
