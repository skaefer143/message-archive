# Generated by Django 3.1.6 on 2021-03-19 03:20

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_sent', models.DateTimeField()),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('phone_num', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('facebook_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=512)),
                ('internal_image_url', models.CharField(max_length=512)),
                ('external_image_url', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='FacebookMessage',
            fields=[
                ('message_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='messagestore.message')),
                ('message_type', models.CharField(choices=[('generic', 'Generic'), ('call', 'Call')], max_length=32)),
                ('external_share_url', models.CharField(max_length=512)),
                ('call_duration', models.PositiveBigIntegerField(blank=True, null=True)),
            ],
            bases=('messagestore.message',),
        ),
        migrations.CreateModel(
            name='TextMessage',
            fields=[
                ('message_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='messagestore.message')),
            ],
            bases=('messagestore.message',),
        ),
        migrations.AddField(
            model_name='message',
            name='recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipient_messages', to='messagestore.person'),
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender_messages', to='messagestore.person'),
        ),
    ]