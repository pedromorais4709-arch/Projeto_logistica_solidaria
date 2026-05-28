from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doacoes', '0003_check_constraints'),
        ('pedidos', '0003_check_constraints'),
        ('avaliacoes', '0002_constraints'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            CREATE VIEW IF NOT EXISTS vw_resumo_doacoes AS
            SELECT
                u.id AS doador_id,
                u.username AS doador,
                COUNT(d.id) AS total_doacoes,
                SUM(CASE WHEN d.status = 'disponivel' THEN 1 ELSE 0 END) AS disponiveis,
                SUM(CASE WHEN d.status = 'entregue' THEN 1 ELSE 0 END) AS entregues,
                SUM(CASE WHEN d.status = 'cancelado' THEN 1 ELSE 0 END) AS canceladas
            FROM usuarios_usuario u
            LEFT JOIN doacoes_doacao d ON d.doador_id = u.id
            WHERE u.tipo = 'doador'
            GROUP BY u.id, u.username;
            """,
            reverse_sql="DROP VIEW IF EXISTS vw_resumo_doacoes;",
        ),
        migrations.RunSQL(
            sql="""
            CREATE VIEW IF NOT EXISTS vw_pedidos_completos AS
            SELECT
                p.id,
                p.codigo_rastreio,
                p.status,
                p.prioridade,
                p.data_criacao,
                p.data_entrega,
                b.username AS beneficiario,
                d.titulo AS doacao,
                d.quantidade AS qtd_disponivel,
                p.quantidade_solicitada,
                c.nome AS categoria,
                COALESCE(a.nota_geral, 0) AS nota_avaliacao
            FROM pedidos_pedido p
            JOIN usuarios_usuario b ON b.id = p.beneficiario_id
            JOIN doacoes_doacao d ON d.id = p.doacao_id
            JOIN doacoes_categoriadoacao c ON c.id = d.categoria_id
            LEFT JOIN avaliacoes_avaliacao a ON a.pedido_id = p.id;
            """,
            reverse_sql="DROP VIEW IF EXISTS vw_pedidos_completos;",
        ),
    ]
