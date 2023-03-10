# Generated by Django 4.1.4 on 2023-01-29 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('name', models.CharField(max_length=150)),
                ('mobile', models.CharField(max_length=20)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nationality', models.CharField(choices=[('AFGHANISTAN', 'AFGHANISTAN'), ('ALBANIA', 'ALBANIA'), ('ALGERIA', 'ALGERIA'), ('ANDORRA', 'ANDORRA'), ('ANGOLA', 'ANGOLA'), ('ANGUILLA', 'ANGUILLA'), ('ANTARCTICA', 'ANTARCTICA'), ('ARGENTINA', 'ARGENTINA'), ('ARMENIA', 'ARMENIA'), ('AUSTRALIA', 'AUSTRALIA'), ('AUSTRIA', 'AUSTRIA'), ('AZERBAIJAN', 'AZERBAIJAN'), ('BAHAMAS', 'BAHAMAS'), ('BAHRAIN', 'BAHRAIN'), ('BANGLADESH', 'BANGLADESH'), ('BARBADOS', 'BARBADOS'), ('BELARUS', 'BELARUS'), ('BELGIUM', 'BELGIUM'), ('BELIZE', 'BELIZE'), ('BOLIVIA', 'BOLIVIA'), ('BRAZIL', 'BRAZIL'), ('BULGARIA', 'BULGARIA'), ('CAMEROON', 'CAMEROON'), ('CANADA', 'CANADA'), ('CHINA', 'CHINA'), ('COLOMBIA', 'COLOMBIA'), ('COMOROS', 'COMOROS'), ('CONGO', 'CONGO'), ('COSTA RICA', 'COSTA RICA'), ('CROATIA', 'CROATIA'), ('CUBA', 'CUBA'), ('CYPRUS', 'CYPRUS'), ('CZECH', 'CZECH REPUBLIC'), ('DENMARK', 'DENMARK'), ('DJIBOUTI', 'DJIBOUTI'), ('DOMINICAN', 'DOMINICAN REPUBLIC'), ('ECUADOR', 'ECUADOR'), ('EGYPT', 'EGYPT'), ('ERITREA', 'ERITREA'), ('ESTONIA', 'ESTONIA'), ('ETHIOPIA', 'ETHIOPIA'), ('FINLAND', 'FINLAND'), ('FRANCE', 'FRANCE'), ('GABON', 'GABON'), ('GAMBIA', 'GAMBIA'), ('GEORGIA', 'GEORGIA'), ('GERMANY', 'GERMANY'), ('GHANA', 'GHANA'), ('GREECE', 'GREECE'), ('GREENLAND', 'GREENLAND'), ('HUNGARY', 'HUNGARY'), ('ICELAND', 'ICELAND'), ('INDIA', 'INDIA'), ('INDONESIA', 'INDONESIA'), ('IRAN', 'IRAN'), ('IRAQ', 'IRAQ'), ('IRELAND', 'IRELAND'), ('ITALY', 'ITALY'), ('JAPAN', 'JAPAN'), ('JORDAN', 'JORDAN'), ('KAZAKHSTAN', 'KAZAKHSTAN'), ('KENYA', 'KENYA'), ('KIRIBATI', 'KIRIBATI'), ('North KOREA', "North KOREA, DEMOCRATIC PEOPLE'S REPUBLIC OF"), ('South KOREA', 'South KOREA, REPUBLIC OF'), ('KUWAIT', 'KUWAIT'), ('KYRGYZSTAN', 'KYRGYZSTAN'), ('LATVIA', 'LATVIA'), ('LEBANON', 'LEBANON'), ('LIBYAN', 'LIBYAN ARAB JAMAHIRIYA'), ('LIECHTENSTEIN', 'LIECHTENSTEIN'), ('LITHUANIA', 'LITHUANIA'), ('LUXEMBOURG', 'LUXEMBOURG'), ('MACAO', 'MACAO'), ('MACEDONIA', 'MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF'), ('MADAGASCAR', 'MADAGASCAR'), ('MALAWI', 'MALAWI'), ('MALAYSIA', 'MALAYSIA'), ('MALDIVES', 'MALDIVES'), ('MALI', 'MALI'), ('MALTA', 'MALTA'), ('MOROCCO', 'MOROCCO'), ('MOZAMBIQUE', 'MOZAMBIQUE'), ('NEPAL', 'NEPAL'), ('NETHERLANDS', 'NETHERLANDS'), ('NIGERIA', 'NIGERIA'), ('NORWAY', 'NORWAY'), ('OMAN', 'OMAN'), ('PAKISTAN', 'PAKISTAN'), ('PALAU', 'PALAU'), ('PALESTINIAN', 'PALESTINIAN'), ('PANAMA', 'PANAMA'), ('PARAGUAY', 'PARAGUAY'), ('PERU', 'PERU'), ('PHILIPPINES', 'PHILIPPINES'), ('PITCAIRN', 'PITCAIRN'), ('POLAND', 'POLAND'), ('PORTUGAL', 'PORTUGAL'), ('QATAR', 'QATAR'), ('ROMANIA', 'ROMANIA'), ('RUSSIAN', 'RUSSIAN FEDERATION'), ('RWANDA', 'RWANDA'), ('SAUDI ARABIA', 'SAUDI ARABIA'), ('SENEGAL', 'SENEGAL'), ('SINGAPORE', 'SINGAPORE'), ('SLOVAKIA', 'SLOVAKIA'), ('SLOVENIA', 'SLOVENIA'), ('SOMALIA', 'SOMALIA'), ('SOUTH AFRICA', 'SOUTH AFRICA'), ('SPAIN', 'SPAIN'), ('SUDAN', 'SUDAN'), ('SWEDEN', 'SWEDEN'), ('SWITZERLAND', 'SWITZERLAND'), ('SYRIAN', 'SYRIAN ARAB REPUBLIC'), ('TAIWAN', 'TAIWAN'), ('TAJIKISTAN', 'TAJIKISTAN'), ('TANZANIA', 'TANZANIA'), ('THAILAND', 'THAILAND'), ('TUNISIA', 'TUNISIA'), ('TURKEY', 'TURKEY'), ('TURKMENISTAN', 'TURKMENISTAN'), ('UGANDA', 'UGANDA'), ('UKRAINE', 'UKRAINE'), ('UNITED ARAB EMIRATES', 'UNITED ARAB EMIRATES'), ('UNITED KINGDOM', 'UNITED KINGDOM'), ('UNITED STATES', 'UNITED STATES'), ('URUGUAY', 'URUGUAY'), ('UZBEKISTAN', 'UZBEKISTAN'), ('YEMEN', 'YEMEN')], max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], max_length=50)),
                ('birthdate', models.DateField(null=True, verbose_name='Birth Date')),
                ('user_type', models.CharField(choices=[('0', 'Professor'), ('1', 'Student'), ('2', 'Patient')], default=('2', 'Patient'), max_length=256)),
                ('profile_img', models.ImageField(default='profile2.png', upload_to='profile_image_upload')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Accounts',
                'verbose_name_plural': 'Accounts',
            },
        ),
    ]
