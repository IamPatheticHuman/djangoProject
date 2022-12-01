from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0002_add'),
    ]

    operations = [
        migrations.DeleteModel(
            name='video',
        ),
    ]