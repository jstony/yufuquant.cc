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
            name='GridStrategyParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='创建于')),
                ('modified_at', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='修改于')),
                ('min_price', models.FloatField(verbose_name='最低价格')),
                ('max_price', models.FloatField(verbose_name='最高价格')),
                ('num_grids', models.IntegerField(verbose_name='网格数量')),
                ('max_leverage', models.FloatField(verbose_name='最大杠杆')),
                ('principal', models.FloatField(verbose_name='投入本金')),
                ('take_profit_range', models.FloatField(verbose_name='止盈间距')),
                ('robot', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='grid_strategy_parameter', to='robots.Robot', verbose_name='机器人')),
            ],
            options={
                'verbose_name': '网格策略参数',
                'verbose_name_plural': '网格策略参数',
            },
        ),
        migrations.CreateModel(
            name='Grid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_qty', models.FloatField(verbose_name='仓位数量')),
                ('entry_price', models.FloatField(verbose_name='入场价格')),
                ('exit_price', models.FloatField(verbose_name='出场价格')),
                ('filled_qty', models.FloatField(verbose_name='已开仓数量')),
                ('associated_order_id', models.CharField(blank=True, max_length=100, verbose_name='关联订单id')),
                ('locked', models.BooleanField(default=False, verbose_name='锁仓')),
                ('created_at', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='创建于')),
                ('modified_at', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='修改于')),
                ('level', models.IntegerField(verbose_name='层')),
                ('robot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grids', to='robots.Robot', verbose_name='机器人')),
            ],
            options={
                'verbose_name': '网格',
                'verbose_name_plural': '网格',
            },
        ),
    ]
