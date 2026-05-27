from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        
        migrations.AddIndex(
            model_name='pedido',
            index=models.Index(fields=['codigo_rastreio'], name='idx_pedido_rastreio'),
        ),
        
        migrations.AddIndex(
            model_name='pedido',
            index=models.Index(fields=['status', 'data_criacao'], name='idx_pedido_status_data'),
        ),
    ]
