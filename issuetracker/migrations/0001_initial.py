# Generated by Django 2.0.6 on 2018-06-04 01:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('submitted_date', models.DateField(auto_now_add=True)),
                ('description', models.TextField(blank=True)),
                ('priority', models.IntegerField(choices=[(1, 'Critical'), (2, 'High'), (3, 'Low')], default=1)),
                ('status', models.IntegerField(choices=[(1, 'Open'), (2, 'Resolved'), (3, 'Closed')], default=1)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='issuetracker.Category')),
                ('solver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('submitter', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='submitter', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'issue',
                'verbose_name_plural': 'issues',
                'ordering': ('status', 'submitted_date', 'title'),
            },
        ),
    ]
