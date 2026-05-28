from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='avaliacao',
            constraint=models.CheckConstraint(
                condition=models.Q(nota_geral__gte=1, nota_geral__lte=5),
                name='chk_nota_geral_1_5',
            ),
        ),
        migrations.AddConstraint(
            model_name='avaliacao',
            constraint=models.CheckConstraint(
                condition=models.Q(nota_atendimento__isnull=True) | models.Q(nota_atendimento__gte=1, nota_atendimento__lte=5),
                name='chk_nota_atendimento_1_5',
            ),
        ),
        migrations.AddConstraint(
            model_name='avaliacao',
            constraint=models.CheckConstraint(
                condition=models.Q(nota_prazo__isnull=True) | models.Q(nota_prazo__gte=1, nota_prazo__lte=5),
                name='chk_nota_prazo_1_5',
            ),
        ),
    ]
