# Generated by Django 3.0.8 on 2020-11-06 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('http_host', models.TextField(blank=True, null=True)),
                ('http_referrer', models.TextField(blank=True, null=True)),
                ('http_user_agent', models.TextField(blank=True, null=True)),
                ('remote_addr', models.TextField(blank=True, null=True)),
                ('remote_host', models.TextField(blank=True, null=True)),
                ('remote_user', models.TextField(blank=True, null=True)),
                ('server_name', models.TextField(blank=True, null=True)),
                ('server_port', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
