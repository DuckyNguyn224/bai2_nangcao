from django.db import migrations
from django.utils import timezone

def create_sample_post(apps, schema_editor):
    Post = apps.get_model('first_app', 'Post')
    if not Post.objects.filter(pk=1).exists():
        Post.objects.create(
            id=1,
            title='Sample Post',
            content='This is a sample post content.',
            published_date=timezone.now(),
            author='Admin'
        )

class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0007_alter_comment_created_on'),
    ]

    operations = [
        migrations.RunPython(create_sample_post),
    ]
