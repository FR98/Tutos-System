# Generated by Django 3.0.5 on 2020-08-22 00:37

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0001_initial'),
        ('auth', '0011_update_proxy_permissions'),
        ('institutions', '0002_auto_20200510_2225'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone', models.PositiveIntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], editable=False, max_length=30)),
                ('birthdate', models.DateField()),
                ('is_tutor', models.BooleanField(default=False)),
                ('career', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='institutions.Career')),
                ('institution', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='institutions.Institution')),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='locations.Language')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='locations.Location')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
