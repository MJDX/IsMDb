# Generated by Django 2.2.1 on 2019-05-30 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=255)),
                ('last_name', models.CharField(blank=True, max_length=255)),
                ('profile_picture_url', models.ImageField(default='default_cast.png', upload_to='gallery')),
                ('role', models.CharField(choices=[('Director', 'Director'), ('Writer', 'Writer'), ('Actor', 'Actor')], max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='memberID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Member'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='reviewID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='review.MovieReview'),
        ),
        migrations.AlterField(
            model_name='moviecast',
            name='castID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='review.Staff'),
        ),
        migrations.AlterField(
            model_name='moviecast',
            name='movieID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='review.MovieReview'),
        ),
        migrations.AlterField(
            model_name='moviereview',
            name='cover',
            field=models.ImageField(default='default_cast.png', upload_to='gallery'),
        ),
        migrations.AlterField(
            model_name='moviereview',
            name='genre',
            field=models.CharField(choices=[('Action', 'Action'), ('Comedy', 'Comedy'), ('Drama', 'Drama'), ('Family', 'Family'), ('Romance', 'Romance'), ('Sci-Fi', 'Sci-Fi')], max_length=255),
        ),
        migrations.AlterField(
            model_name='moviereview',
            name='time',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='reactcomment',
            name='commentID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='review.Comment'),
        ),
        migrations.AlterField(
            model_name='reactcomment',
            name='memberID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Member'),
        ),
        migrations.AlterField(
            model_name='reportcomment',
            name='commentID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='review.Comment'),
        ),
        migrations.AlterField(
            model_name='reportcomment',
            name='memberID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Member'),
        ),
        migrations.AlterField(
            model_name='reportmember',
            name='reportedID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reportmember_reported', to='user.Member'),
        ),
        migrations.AlterField(
            model_name='reportmember',
            name='reporterID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reportmember_reporter', to='user.Member'),
        ),
        migrations.AlterField(
            model_name='reportreview',
            name='memberID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Member'),
        ),
        migrations.AlterField(
            model_name='reportreview',
            name='reviewID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='review.MovieReview'),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='memberID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Member'),
        ),
        migrations.AlterField(
            model_name='upvote',
            name='memberID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Member'),
        ),
        migrations.AlterField(
            model_name='upvote',
            name='suggestionID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='review.Suggestion'),
        ),
        migrations.DeleteModel(
            name='Cast',
        ),
    ]
