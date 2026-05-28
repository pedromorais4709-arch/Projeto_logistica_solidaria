from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0002_constraints'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='pedido',
            constraint=models.CheckConstraint(
                condition=models.Q(quantidade_solicitada__gte=1),
                name='chk_pedido_quantidade_positiva',
            ),
        ),
        migrations.AddConstraint(
            model_name='pedido',
            constraint=models.CheckConstraint(
                condition=models.Q(status__in=[
                    'pendente', 'aprovado', 'em_separacao',
                    'em_transito', 'entregue', 'cancelado'
                ]),
                name='chk_pedido_status_valido',
            ),
        ),
        migrations.AddConstraint(
            model_name='pedido',
            constraint=models.CheckConstraint(
                condition=models.Q(prioridade__in=['baixa', 'normal', 'alta', 'urgente']),
                name='chk_pedido_prioridade_valida',
            ),
        ),
    ]
