from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rastreamento', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            CREATE TRIGGER IF NOT EXISTS trg_evento_entregue
            AFTER INSERT ON rastreamento_eventorastreamento
            WHEN NEW.tipo = 'entregue'
            BEGIN
                UPDATE pedidos_pedido
                SET status = 'entregue',
                    data_entrega = datetime('now')
                WHERE id = NEW.pedido_id
                  AND status != 'entregue';
            END;
            """,
            reverse_sql="DROP TRIGGER IF EXISTS trg_evento_entregue;",
        ),
        migrations.RunSQL(
            sql="""
            CREATE TRIGGER IF NOT EXISTS trg_evento_cancelado
            AFTER INSERT ON rastreamento_eventorastreamento
            WHEN NEW.tipo = 'cancelado'
            BEGIN
                UPDATE pedidos_pedido
                SET status = 'cancelado'
                WHERE id = NEW.pedido_id
                  AND status NOT IN ('entregue', 'cancelado');
            END;
            """,
            reverse_sql="DROP TRIGGER IF EXISTS trg_evento_cancelado;",
        ),
    ]
