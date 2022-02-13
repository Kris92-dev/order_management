# Generated by Django 3.1.9 on 2022-02-13 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consumer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email_id', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product1_num', models.IntegerField(default=0)),
                ('product2_num', models.IntegerField(default=0)),
                ('product3_num', models.IntegerField(default=0)),
                ('product4_num', models.IntegerField(default=0)),
                ('consumer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app1.consumer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_order_amount', models.FloatField()),
                ('total_paid_amount', models.FloatField()),
                ('total_pending', models.FloatField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app1.orders')),
            ],
        ),
        migrations.AddField(
            model_name='orders',
            name='product1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='product1', to='app1.product'),
        ),
        migrations.AddField(
            model_name='orders',
            name='product2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='product2', to='app1.product'),
        ),
        migrations.AddField(
            model_name='orders',
            name='product3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='product3', to='app1.product'),
        ),
        migrations.AddField(
            model_name='orders',
            name='product4',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='product4', to='app1.product'),
        ),
    ]
