# Generated by Django 4.0.2 on 2022-12-14 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_contact_delete_kadeqoriyalar_remove_postlar_author_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim_soyisim', models.CharField(max_length=20, verbose_name='Ad,Soyad')),
                ('icerik', models.TextField(max_length=1000, verbose_name='icerik')),
                ('tarix', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='posts.post', verbose_name='Post')),
            ],
            options={
                'verbose_name': 'Yorumlar',
                'verbose_name_plural': 'Yorumlar',
            },
        ),
    ]
