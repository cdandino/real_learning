# Generated by Django 2.0.1 on 2018-01-20 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('textbook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.FloatField()),
                ('title', models.CharField(max_length=50)),
                ('subtitle', models.CharField(max_length=500)),
                ('intro', models.CharField(max_length=3000)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.FloatField()),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='textbook',
            name='cover_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='section',
            name='chapter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='textbook.Textbook'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='textbook',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='textbook.Textbook'),
        ),
    ]
