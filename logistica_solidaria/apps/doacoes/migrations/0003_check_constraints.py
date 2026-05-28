from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doacoes', '0002_constraints'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='doacao',
            constraint=models.CheckConstraint(
                condition=models.Q(quantidade__gte=1),
                name='chk_doacao_quantidade_positiva',
            ),
        ),
        migrations.AddConstraint(
            model_name='doacao',
            constraint=models.CheckConstraint(
                condition=models.Q(status__in=['disponivel', 'reservado', 'entregue', 'cancelado']),
                name='chk_doacao_status_valido',
            ),
        ),
        migrations.AddConstraint(
            model_name='doacao',
            constraint=models.CheckConstraint(
                condition=models.Q(condicao__in=['novo', 'semi_novo', 'usado_bom', 'usado_regular']),
                name='chk_doacao_condicao_valida',
            ),
        ),
    ]
