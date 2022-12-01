from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('quantity', models.IntegerField()),
                ('trailer', models.URLField()),
                ('genre', models.CharField(choices=[('POP', 'POP'), ('ROCK', 'ROCK'), ('INDIE', 'INDIE'), ('SOUNDTRACK','SOUNDTRACK'), ('LO-FI', 'LO-FI')], max_length=100)),
            ],
        ),
    ]