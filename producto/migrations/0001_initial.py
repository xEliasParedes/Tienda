# Generated by Django 4.1.2 on 2023-07-07 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(db_column='id_categoria', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id_comuna', models.AutoField(db_column='id_comuna', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id_marca', models.CharField(db_column='id_marca', max_length=2, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=35)),
                ('categoria', models.ForeignKey(db_column='id_categoria', on_delete=django.db.models.deletion.CASCADE, to='producto.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=35)),
                ('cantidad', models.CharField(max_length=3)),
                ('descripcion', models.CharField(max_length=330)),
                ('precio_new', models.CharField(max_length=6)),
                ('precio_old', models.CharField(max_length=6)),
                ('dis_despacho', models.BooleanField()),
                ('dis_retiro', models.BooleanField()),
                ('marca', models.ForeignKey(db_column='id_marca', on_delete=django.db.models.deletion.CASCADE, to='producto.marca')),
            ],
        ),
        migrations.CreateModel(
            name='Provedor',
            fields=[
                ('id_provedor', models.CharField(db_column='id_provedor', max_length=2, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id_region', models.AutoField(db_column='id_region', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id_sucursal', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=50)),
                ('comuna', models.ForeignKey(db_column='id_comuna', on_delete=django.db.models.deletion.CASCADE, to='producto.comuna')),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Categoria',
            fields=[
                ('id_sub_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('categoria', models.ForeignKey(db_column='id_categoria', on_delete=django.db.models.deletion.CASCADE, to='producto.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Retiro',
            fields=[
                ('id_soli_ret', models.AutoField(db_column='id_soli_ret', primary_key=True, serialize=False)),
                ('receptor', models.CharField(max_length=65)),
                ('producto', models.ForeignKey(db_column='id_producto', on_delete=django.db.models.deletion.CASCADE, to='producto.producto')),
                ('sucursal', models.ForeignKey(db_column='id_sucursal', on_delete=django.db.models.deletion.CASCADE, to='producto.sucursal')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='provedor',
            field=models.ForeignKey(db_column='id_provedor', on_delete=django.db.models.deletion.CASCADE, to='producto.provedor'),
        ),
        migrations.AddField(
            model_name='producto',
            name='sub_categoria',
            field=models.ForeignKey(db_column='id_sub_categoria', on_delete=django.db.models.deletion.CASCADE, to='producto.sub_categoria'),
        ),
        migrations.CreateModel(
            name='Despacho',
            fields=[
                ('id_soli_des', models.AutoField(db_column='id_soli_des', primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=100)),
                ('num_casa_dep', models.CharField(blank=True, max_length=3, null=True)),
                ('info_add', models.CharField(blank=True, max_length=100, null=True)),
                ('receptor', models.CharField(max_length=65)),
                ('comuna', models.ForeignKey(db_column='id_comuna', on_delete=django.db.models.deletion.CASCADE, to='producto.comuna')),
                ('producto', models.ForeignKey(db_column='id_producto', on_delete=django.db.models.deletion.CASCADE, to='producto.producto')),
            ],
        ),
        migrations.AddField(
            model_name='comuna',
            name='region',
            field=models.ForeignKey(db_column='id_region', on_delete=django.db.models.deletion.CASCADE, to='producto.region'),
        ),
    ]
