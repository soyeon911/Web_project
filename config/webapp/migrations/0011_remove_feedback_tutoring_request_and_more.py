# Generated by Django 5.1.3 on 2024-11-14 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_dotulink'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='tutoring_request',
        ),
        migrations.RemoveField(
            model_name='link',
            name='tutoring_request',
        ),
        migrations.RemoveField(
            model_name='link',
            name='user',
        ),
        migrations.DeleteModel(
            name='Major',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tutoringrequest',
            name='tutee_email',
        ),
        migrations.RemoveField(
            model_name='tutoringrequest',
            name='tutor_email',
        ),
        migrations.DeleteModel(
            name='Feedback',
        ),
        migrations.DeleteModel(
            name='Link',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.DeleteModel(
            name='TutoringRequest',
        ),
    ]
