from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doacoes', '0001_initial'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='doacao',
            index=models.Index(fields=['status', 'categoria'], name='idx_doacao_status_cat'),
        ),
        migrations.AddIndex(
            model_name='doacao',
            index=models.Index(fields=['doador', 'status'], name='idx_doacao_doador_status'),
        ),
    ]
