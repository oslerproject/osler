# Generated by Django 3.0.5 on 2020-05-10 04:15

from django.db import migrations, models
import osler.core.models
import osler.core.validators
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActionInstruction',
            fields=[
                ('instruction', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ActionItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('written_datetime', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('completion_date', models.DateTimeField(blank=True, null=True)),
                ('due_date', models.DateField(help_text='MM/DD/YYYY')),
                ('priority', models.BooleanField(default=False, help_text='Check this box if this action item is high priority')),
                ('comments', models.TextField()),
            ],
            options={
                'ordering': ['-written_datetime', '-last_modified'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContactMethod',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('written_datetime', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('image', models.FileField(help_text='Please deidentify all file names before upload! Delete all files after upload!', upload_to=osler.core.models.make_filepath, verbose_name='PDF File or Image Upload')),
                ('comments', models.TextField()),
            ],
            options={
                'ordering': ['-written_datetime', '-last_modified'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Ethnicity',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'ethnicities',
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('long_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('short_name', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalActionItem',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('written_datetime', models.DateTimeField(blank=True, editable=False)),
                ('last_modified', models.DateTimeField(blank=True, editable=False)),
                ('completion_date', models.DateTimeField(blank=True, null=True)),
                ('due_date', models.DateField(help_text='MM/DD/YYYY')),
                ('priority', models.BooleanField(default=False, help_text='Check this box if this action item is high priority')),
                ('comments', models.TextField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical action item',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalDocument',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('written_datetime', models.DateTimeField(blank=True, editable=False)),
                ('last_modified', models.DateTimeField(blank=True, editable=False)),
                ('title', models.CharField(max_length=200)),
                ('image', models.TextField(help_text='Please deidentify all file names before upload! Delete all files after upload!', max_length=100, verbose_name='PDF File or Image Upload')),
                ('comments', models.TextField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical document',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalPatient',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, validators=[osler.core.validators.validate_name])),
                ('last_name', models.CharField(max_length=100, validators=[osler.core.validators.validate_name])),
                ('middle_name', models.CharField(blank=True, max_length=100, validators=[osler.core.validators.validate_name])),
                ('phone', models.CharField(blank=True, max_length=40, null=True)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(default='St. Louis', max_length=50)),
                ('state', models.CharField(default='MO', max_length=2)),
                ('zip_code', models.CharField(max_length=5, validators=[osler.core.validators.validate_zip])),
                ('country', models.CharField(default='USA', max_length=100)),
                ('pcp_preferred_zip', models.CharField(blank=True, max_length=5, null=True, validators=[osler.core.validators.validate_zip])),
                ('date_of_birth', models.DateField(help_text='MM/DD/YYYY', validators=[osler.core.validators.validate_birth_date])),
                ('patient_comfortable_with_english', models.BooleanField(default=True)),
                ('alternate_phone_1_owner', models.CharField(blank=True, max_length=40, null=True)),
                ('alternate_phone_1', models.CharField(blank=True, max_length=40, null=True)),
                ('alternate_phone_2_owner', models.CharField(blank=True, max_length=40, null=True)),
                ('alternate_phone_2', models.CharField(blank=True, max_length=40, null=True)),
                ('alternate_phone_3_owner', models.CharField(blank=True, max_length=40, null=True)),
                ('alternate_phone_3', models.CharField(blank=True, max_length=40, null=True)),
                ('alternate_phone_4_owner', models.CharField(blank=True, max_length=40, null=True)),
                ('alternate_phone_4', models.CharField(blank=True, max_length=40, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('needs_workup', models.BooleanField(default=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical patient',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalProvider',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, validators=[osler.core.validators.validate_name])),
                ('last_name', models.CharField(max_length=100, validators=[osler.core.validators.validate_name])),
                ('middle_name', models.CharField(blank=True, max_length=100, validators=[osler.core.validators.validate_name])),
                ('phone', models.CharField(blank=True, max_length=40, null=True)),
                ('needs_updating', models.BooleanField(default=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical provider',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Outcome',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, validators=[osler.core.validators.validate_name])),
                ('last_name', models.CharField(max_length=100, validators=[osler.core.validators.validate_name])),
                ('middle_name', models.CharField(blank=True, max_length=100, validators=[osler.core.validators.validate_name])),
                ('phone', models.CharField(blank=True, max_length=40, null=True)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(default='St. Louis', max_length=50)),
                ('state', models.CharField(default='MO', max_length=2)),
                ('zip_code', models.CharField(max_length=5, validators=[osler.core.validators.validate_zip])),
                ('country', models.CharField(default='USA', max_length=100)),
                ('pcp_preferred_zip', models.CharField(blank=True, max_length=5, null=True, validators=[osler.core.validators.validate_zip])),
                ('date_of_birth', models.DateField(help_text='MM/DD/YYYY', validators=[osler.core.validators.validate_birth_date])),
                ('patient_comfortable_with_english', models.BooleanField(default=True)),
                ('alternate_phone_1_owner', models.CharField(blank=True, max_length=40, null=True)),
                ('alternate_phone_1', models.CharField(blank=True, max_length=40, null=True)),
                ('alternate_phone_2_owner', models.CharField(blank=True, max_length=40, null=True)),
                ('alternate_phone_2', models.CharField(blank=True, max_length=40, null=True)),
                ('alternate_phone_3_owner', models.CharField(blank=True, max_length=40, null=True)),
                ('alternate_phone_3', models.CharField(blank=True, max_length=40, null=True)),
                ('alternate_phone_4_owner', models.CharField(blank=True, max_length=40, null=True)),
                ('alternate_phone_4', models.CharField(blank=True, max_length=40, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('needs_workup', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, validators=[osler.core.validators.validate_name])),
                ('last_name', models.CharField(max_length=100, validators=[osler.core.validators.validate_name])),
                ('middle_name', models.CharField(blank=True, max_length=100, validators=[osler.core.validators.validate_name])),
                ('phone', models.CharField(blank=True, max_length=40, null=True)),
                ('needs_updating', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProviderType',
            fields=[
                ('long_name', models.CharField(max_length=100)),
                ('short_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('signs_charts', models.BooleanField(default=False)),
                ('staff_view', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ReferralType',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('is_fqhc', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReferralLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('address', models.TextField()),
                ('care_availiable', models.ManyToManyField(to='core.ReferralType')),
            ],
        ),
    ]