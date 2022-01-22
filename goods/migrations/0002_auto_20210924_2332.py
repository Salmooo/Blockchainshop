# Generated by Django 2.2.7 on 2021-09-24 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodsorder',
            name='is_settle',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=100, verbose_name='是否结算'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='pay_way',
            field=models.CharField(choices=[('All', 'All'), ('ETH', 'ETH'), ('USDT', 'USDT')], default='All', max_length=100, verbose_name='支持支付的方式'),
        ),
        migrations.AlterField(
            model_name='goodsorder',
            name='pay_way',
            field=models.CharField(choices=[('All', 'All'), ('ETH', 'ETH'), ('USDT', 'USDT')], default='件', max_length=100, verbose_name='计量方式'),
        ),
    ]