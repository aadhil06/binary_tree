# Generated by Django 4.2.1 on 2023-05-29 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BinaryTreeNode',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('parent_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='binary_app.binarytreenode')),
            ],
        ),
    ]
