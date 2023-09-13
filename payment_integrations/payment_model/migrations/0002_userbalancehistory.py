# Generated by Django 4.2.5 on 2023-09-13 09:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payment_model', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBalanceHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(verbose_name='Summa')),
                ('operation', models.IntegerField(choices=[(1, "Hisob to'ldirildi"), (2, 'Hisob raqamidan pul yechib olindi')], verbose_name='Bajarilgan amal')),
                ('prev_balance', models.FloatField(verbose_name="O'zgarishdan oldingi balans")),
                ('new_balance', models.FloatField(verbose_name="O'zgarishdan keyingi balans")),
                ('comment', models.TextField(blank=True, null=True, verbose_name="Qo'shimcha ma'lumot")),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Vaqt')),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
                ('transaction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='hist', to='payment_model.transaction')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='balance_history', to=settings.AUTH_USER_MODEL, verbose_name='Foydalanuvchi')),
            ],
            options={
                'verbose_name': 'Foydalanuvchi hisobi tarixi',
                'verbose_name_plural': 'Foydalanuvchi hisobi tarixlari',
                'db_table': 'balance_history',
            },
        ),
    ]
