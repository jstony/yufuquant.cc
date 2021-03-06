# Generated by Django 3.0.7 on 2020-07-03 11:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('robots', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='创建于')),
                ('modified_at', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='修改于')),
                ('direction', models.SmallIntegerField(choices=[(-1, '空'), (0, '无'), (1, '多')], default=0, verbose_name='方向')),
                ('qty', models.FloatField(default=0, verbose_name='数量')),
                ('avg_price', models.FloatField(default=0, verbose_name='均价')),
                ('unrealized_pnl', models.FloatField(default=0, verbose_name='未结盈亏')),
                ('liq_price', models.FloatField(default=0, verbose_name='强平价')),
                ('leverage', models.FloatField(default=0, verbose_name='杠杆')),
                ('robot', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='robots.Robot', verbose_name='机器人')),
            ],
            options={
                'verbose_name': '仓位',
                'verbose_name_plural': '仓位',
            },
        ),
    ]
