# Generated by Django 2.2.7 on 2021-09-24 13:39

import common.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='资产名称')),
                ('chain_name', models.CharField(max_length=100, verbose_name='链名称')),
                ('usd_price', common.models.DecField(decimal_places=30, max_digits=65, max_length=100, verbose_name='美元价格')),
                ('cny_price', common.models.DecField(decimal_places=30, max_digits=65, max_length=100, verbose_name='人民币价格')),
                ('unit', models.CharField(max_length=100, verbose_name='币种精度')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否是有效')),
            ],
            options={
                'verbose_name': '资产表',
                'verbose_name_plural': '资产表',
            },
        ),
    ]
