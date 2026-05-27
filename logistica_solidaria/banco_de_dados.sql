BEGIN TRANSACTION;
CREATE TABLE "auth_group" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(150) NOT NULL UNIQUE);
CREATE TABLE "auth_group_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE "auth_permission" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "codename" varchar(100) NOT NULL, "name" varchar(255) NOT NULL);
INSERT INTO "auth_permission" VALUES(1,1,'add_logentry','Can add log entry');
INSERT INTO "auth_permission" VALUES(2,1,'change_logentry','Can change log entry');
INSERT INTO "auth_permission" VALUES(3,1,'delete_logentry','Can delete log entry');
INSERT INTO "auth_permission" VALUES(4,1,'view_logentry','Can view log entry');
INSERT INTO "auth_permission" VALUES(5,3,'add_permission','Can add permission');
INSERT INTO "auth_permission" VALUES(6,3,'change_permission','Can change permission');
INSERT INTO "auth_permission" VALUES(7,3,'delete_permission','Can delete permission');
INSERT INTO "auth_permission" VALUES(8,3,'view_permission','Can view permission');
INSERT INTO "auth_permission" VALUES(9,2,'add_group','Can add group');
INSERT INTO "auth_permission" VALUES(10,2,'change_group','Can change group');
INSERT INTO "auth_permission" VALUES(11,2,'delete_group','Can delete group');
INSERT INTO "auth_permission" VALUES(12,2,'view_group','Can view group');
INSERT INTO "auth_permission" VALUES(13,4,'add_contenttype','Can add content type');
INSERT INTO "auth_permission" VALUES(14,4,'change_contenttype','Can change content type');
INSERT INTO "auth_permission" VALUES(15,4,'delete_contenttype','Can delete content type');
INSERT INTO "auth_permission" VALUES(16,4,'view_contenttype','Can view content type');
INSERT INTO "auth_permission" VALUES(17,5,'add_session','Can add session');
INSERT INTO "auth_permission" VALUES(18,5,'change_session','Can change session');
INSERT INTO "auth_permission" VALUES(19,5,'delete_session','Can delete session');
INSERT INTO "auth_permission" VALUES(20,5,'view_session','Can view session');
INSERT INTO "auth_permission" VALUES(21,6,'add_usuario','Can add Usuário');
INSERT INTO "auth_permission" VALUES(22,6,'change_usuario','Can change Usuário');
INSERT INTO "auth_permission" VALUES(23,6,'delete_usuario','Can delete Usuário');
INSERT INTO "auth_permission" VALUES(24,6,'view_usuario','Can view Usuário');
INSERT INTO "auth_permission" VALUES(25,8,'add_doacao','Can add Doação');
INSERT INTO "auth_permission" VALUES(26,8,'change_doacao','Can change Doação');
INSERT INTO "auth_permission" VALUES(27,8,'delete_doacao','Can delete Doação');
INSERT INTO "auth_permission" VALUES(28,8,'view_doacao','Can view Doação');
INSERT INTO "auth_permission" VALUES(29,7,'add_categoriadoacao','Can add Categoria');
INSERT INTO "auth_permission" VALUES(30,7,'change_categoriadoacao','Can change Categoria');
INSERT INTO "auth_permission" VALUES(31,7,'delete_categoriadoacao','Can delete Categoria');
INSERT INTO "auth_permission" VALUES(32,7,'view_categoriadoacao','Can view Categoria');
INSERT INTO "auth_permission" VALUES(33,9,'add_pedido','Can add Pedido');
INSERT INTO "auth_permission" VALUES(34,9,'change_pedido','Can change Pedido');
INSERT INTO "auth_permission" VALUES(35,9,'delete_pedido','Can delete Pedido');
INSERT INTO "auth_permission" VALUES(36,9,'view_pedido','Can view Pedido');
INSERT INTO "auth_permission" VALUES(37,10,'add_eventorastreamento','Can add Evento de Rastreamento');
INSERT INTO "auth_permission" VALUES(38,10,'change_eventorastreamento','Can change Evento de Rastreamento');
INSERT INTO "auth_permission" VALUES(39,10,'delete_eventorastreamento','Can delete Evento de Rastreamento');
INSERT INTO "auth_permission" VALUES(40,10,'view_eventorastreamento','Can view Evento de Rastreamento');
INSERT INTO "auth_permission" VALUES(41,11,'add_avaliacao','Can add Avaliação');
INSERT INTO "auth_permission" VALUES(42,11,'change_avaliacao','Can change Avaliação');
INSERT INTO "auth_permission" VALUES(43,11,'delete_avaliacao','Can delete Avaliação');
INSERT INTO "auth_permission" VALUES(44,11,'view_avaliacao','Can view Avaliação');
INSERT INTO "auth_permission" VALUES(45,12,'add_notificacao','Can add Notificação');
INSERT INTO "auth_permission" VALUES(46,12,'change_notificacao','Can change Notificação');
INSERT INTO "auth_permission" VALUES(47,12,'delete_notificacao','Can delete Notificação');
INSERT INTO "auth_permission" VALUES(48,12,'view_notificacao','Can view Notificação');
CREATE TABLE "avaliacoes_avaliacao" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "nota_geral" smallint unsigned NOT NULL CHECK ("nota_geral" >= 0), "nota_atendimento" smallint unsigned NULL CHECK ("nota_atendimento" >= 0), "nota_prazo" smallint unsigned NULL CHECK ("nota_prazo" >= 0), "comentario" text NOT NULL, "recomendaria" bool NULL, "data_avaliacao" datetime NOT NULL, "avaliador_id" bigint NOT NULL REFERENCES "usuarios_usuario" ("id") DEFERRABLE INITIALLY DEFERRED, "pedido_id" bigint NOT NULL UNIQUE REFERENCES "pedidos_pedido" ("id") DEFERRABLE INITIALLY DEFERRED, CONSTRAINT "chk_nota_geral_1_5" CHECK (("nota_geral" >= 1 AND "nota_geral" <= 5)), CONSTRAINT "chk_nota_atendimento_1_5" CHECK (("nota_atendimento" IS NULL OR ("nota_atendimento" >= 1 AND "nota_atendimento" <= 5))), CONSTRAINT "chk_nota_prazo_1_5" CHECK (("nota_prazo" IS NULL OR ("nota_prazo" >= 1 AND "nota_prazo" <= 5))));
INSERT INTO "avaliacoes_avaliacao" VALUES(1,5,5,5,'',1,'2026-05-27 17:16:22.595467',4,1);
CREATE TABLE "django_admin_log" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "action_flag" smallint unsigned NOT NULL CHECK ("action_flag" >= 0), "change_message" text NOT NULL, "content_type_id" integer NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" bigint NOT NULL REFERENCES "usuarios_usuario" ("id") DEFERRABLE INITIALLY DEFERRED, "action_time" datetime NOT NULL);
INSERT INTO "django_admin_log" VALUES(1,'2','emy_moon (Doador)',1,'[{"added": {}}]',6,1,'2026-05-26 01:08:02.455613');
CREATE TABLE "django_content_type" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL);
INSERT INTO "django_content_type" VALUES(1,'admin','logentry');
INSERT INTO "django_content_type" VALUES(2,'auth','group');
INSERT INTO "django_content_type" VALUES(3,'auth','permission');
INSERT INTO "django_content_type" VALUES(4,'contenttypes','contenttype');
INSERT INTO "django_content_type" VALUES(5,'sessions','session');
INSERT INTO "django_content_type" VALUES(6,'usuarios','usuario');
INSERT INTO "django_content_type" VALUES(7,'doacoes','categoriadoacao');
INSERT INTO "django_content_type" VALUES(8,'doacoes','doacao');
INSERT INTO "django_content_type" VALUES(9,'pedidos','pedido');
INSERT INTO "django_content_type" VALUES(10,'rastreamento','eventorastreamento');
INSERT INTO "django_content_type" VALUES(11,'avaliacoes','avaliacao');
INSERT INTO "django_content_type" VALUES(12,'notificacoes','notificacao');
CREATE TABLE "django_migrations" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" datetime NOT NULL);
INSERT INTO "django_migrations" VALUES(1,'contenttypes','0001_initial','2026-05-22 23:40:39.611239');
INSERT INTO "django_migrations" VALUES(2,'contenttypes','0002_remove_content_type_name','2026-05-22 23:40:39.624608');
INSERT INTO "django_migrations" VALUES(3,'auth','0001_initial','2026-05-22 23:40:39.642703');
INSERT INTO "django_migrations" VALUES(4,'auth','0002_alter_permission_name_max_length','2026-05-22 23:40:39.658763');
INSERT INTO "django_migrations" VALUES(5,'auth','0003_alter_user_email_max_length','2026-05-22 23:40:39.668454');
INSERT INTO "django_migrations" VALUES(6,'auth','0004_alter_user_username_opts','2026-05-22 23:40:39.677252');
INSERT INTO "django_migrations" VALUES(7,'auth','0005_alter_user_last_login_null','2026-05-22 23:40:39.686066');
INSERT INTO "django_migrations" VALUES(8,'auth','0006_require_contenttypes_0002','2026-05-22 23:40:39.689321');
INSERT INTO "django_migrations" VALUES(9,'auth','0007_alter_validators_add_error_messages','2026-05-22 23:40:39.696863');
INSERT INTO "django_migrations" VALUES(10,'auth','0008_alter_user_username_max_length','2026-05-22 23:40:39.707001');
INSERT INTO "django_migrations" VALUES(11,'auth','0009_alter_user_last_name_max_length','2026-05-22 23:40:39.717753');
INSERT INTO "django_migrations" VALUES(12,'auth','0010_alter_group_name_max_length','2026-05-22 23:40:39.730776');
INSERT INTO "django_migrations" VALUES(13,'auth','0011_update_proxy_permissions','2026-05-22 23:40:39.746590');
INSERT INTO "django_migrations" VALUES(14,'auth','0012_alter_user_first_name_max_length','2026-05-22 23:40:39.755525');
INSERT INTO "django_migrations" VALUES(15,'usuarios','0001_initial','2026-05-22 23:40:39.769650');
INSERT INTO "django_migrations" VALUES(16,'admin','0001_initial','2026-05-22 23:40:39.786021');
INSERT INTO "django_migrations" VALUES(17,'admin','0002_logentry_remove_auto_add','2026-05-22 23:40:39.802240');
INSERT INTO "django_migrations" VALUES(18,'admin','0003_logentry_add_action_flag_choices','2026-05-22 23:40:39.812227');
INSERT INTO "django_migrations" VALUES(19,'sessions','0001_initial','2026-05-22 23:40:39.821667');
INSERT INTO "django_migrations" VALUES(20,'doacoes','0001_initial','2026-05-22 23:52:18.715455');
INSERT INTO "django_migrations" VALUES(21,'pedidos','0001_initial','2026-05-22 23:53:55.754228');
INSERT INTO "django_migrations" VALUES(22,'rastreamento','0001_initial','2026-05-26 00:31:25.622620');
INSERT INTO "django_migrations" VALUES(23,'avaliacoes','0001_initial','2026-05-26 00:31:56.303641');
INSERT INTO "django_migrations" VALUES(24,'notificacoes','0001_initial','2026-05-26 00:32:25.863913');
INSERT INTO "django_migrations" VALUES(25,'usuarios','0002_usuario_cnpj_usuario_pagina_descricao_and_more','2026-05-26 23:36:41.940796');
INSERT INTO "django_migrations" VALUES(26,'pedidos','0002_pedido_voluntario','2026-05-27 18:37:05.848681');
INSERT INTO "django_migrations" VALUES(27,'avaliacoes','0002_constraints','2026-05-27 23:24:36.548858');
INSERT INTO "django_migrations" VALUES(28,'doacoes','0002_constraints','2026-05-27 23:24:36.577618');
INSERT INTO "django_migrations" VALUES(29,'doacoes','0003_check_constraints','2026-05-27 23:24:36.654561');
INSERT INTO "django_migrations" VALUES(30,'pedidos','0002_constraints','2026-05-27 23:24:36.677774');
INSERT INTO "django_migrations" VALUES(31,'pedidos','0003_check_constraints','2026-05-27 23:24:36.726133');
INSERT INTO "django_migrations" VALUES(32,'pedidos','0004_merge_0002_pedido_voluntario_0003_check_constraints','2026-05-27 23:24:36.729825');
INSERT INTO "django_migrations" VALUES(33,'rastreamento','0002_trigger','2026-05-27 23:24:36.746616');
INSERT INTO "django_migrations" VALUES(34,'relatorios','0001_views_sql','2026-05-27 23:24:36.764253');
CREATE TABLE "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" datetime NOT NULL);
CREATE TABLE "doacoes_categoriadoacao" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "nome" varchar(100) NOT NULL, "descricao" text NOT NULL, "ativo" bool NOT NULL);
INSERT INTO "doacoes_categoriadoacao" VALUES(1,'Alimentos','',1);
INSERT INTO "doacoes_categoriadoacao" VALUES(2,'Roupas','',1);
INSERT INTO "doacoes_categoriadoacao" VALUES(3,'Móveis','',1);
INSERT INTO "doacoes_categoriadoacao" VALUES(4,'Brinquedos','',1);
INSERT INTO "doacoes_categoriadoacao" VALUES(5,'Material Escolar','',1);
INSERT INTO "doacoes_categoriadoacao" VALUES(6,'Higiene e Limpeza','',1);
INSERT INTO "doacoes_categoriadoacao" VALUES(7,'Eletrônicos','',1);
INSERT INTO "doacoes_categoriadoacao" VALUES(8,'Medicamentos','',1);
CREATE TABLE "doacoes_doacao" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "titulo" varchar(200) NOT NULL, "descricao" text NOT NULL, "quantidade" integer unsigned NOT NULL CHECK ("quantidade" >= 0), "condicao" varchar(20) NOT NULL, "status" varchar(20) NOT NULL, "imagem" varchar(100) NULL, "data_criacao" datetime NOT NULL, "data_atualizacao" datetime NOT NULL, "categoria_id" bigint NOT NULL REFERENCES "doacoes_categoriadoacao" ("id") DEFERRABLE INITIALLY DEFERRED, "doador_id" bigint NOT NULL REFERENCES "usuarios_usuario" ("id") DEFERRABLE INITIALLY DEFERRED, CONSTRAINT "chk_doacao_quantidade_positiva" CHECK ("quantidade" >= 1), CONSTRAINT "chk_doacao_status_valido" CHECK ("status" IN ('disponivel', 'reservado', 'entregue', 'cancelado')), CONSTRAINT "chk_doacao_condicao_valida" CHECK ("condicao" IN ('novo', 'semi_novo', 'usado_bom', 'usado_regular')));
INSERT INTO "doacoes_doacao" VALUES(1,'roupas frio','roupas brrrr',15,'novo','entregue','','2026-05-26 23:51:42.206700','2026-05-26 23:51:42.206735',2,1);
CREATE TABLE "notificacoes_notificacao" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "tipo" varchar(30) NOT NULL, "titulo" varchar(200) NOT NULL, "mensagem" text NOT NULL, "lida" bool NOT NULL, "data_leitura" datetime NULL, "link" varchar(500) NOT NULL, "data_criacao" datetime NOT NULL, "destinatario_id" bigint NOT NULL REFERENCES "usuarios_usuario" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "notificacoes_notificacao" VALUES(1,'pedido_criado','Novo pedido recebido!','Guilherme de souza solicitou sua doação "roupas frio".',0,NULL,'/pedidos/1/','2026-05-26 23:59:06.275295',1);
INSERT INTO "notificacoes_notificacao" VALUES(2,'pedido_aprovado','Seu pedido foi aprovado! 🎉','O pedido #1 (roupas frio) foi aprovado.',0,NULL,'/pedidos/1/','2026-05-27 17:14:46.839476',4);
INSERT INTO "notificacoes_notificacao" VALUES(3,'pedido_aprovado','Seu pedido foi aprovado! 🎉','O pedido #1 (roupas frio) foi aprovado.',0,NULL,'/pedidos/1/','2026-05-27 17:14:50.184977',4);
INSERT INTO "notificacoes_notificacao" VALUES(4,'pedido_em_separacao','Atualização do pedido #1','Seu pedido está sendo separado.',0,NULL,'/rastreamento/LSAD3F799F/','2026-05-27 17:14:58.725552',4);
INSERT INTO "notificacoes_notificacao" VALUES(5,'pedido_em_transito','Atualização do pedido #1','Seu pedido saiu para entrega! 🚚',0,NULL,'/rastreamento/LSAD3F799F/','2026-05-27 17:15:07.600460',4);
INSERT INTO "notificacoes_notificacao" VALUES(6,'pedido_entregue','Atualização do pedido #1','Sua entrega foi realizada! Que tal avaliar? ⭐',0,NULL,'/rastreamento/LSAD3F799F/','2026-05-27 17:15:15.699402',4);
INSERT INTO "notificacoes_notificacao" VALUES(7,'avaliacao_recebida','Você recebeu uma avaliação!','Sua doação "roupas frio" foi avaliada com 5/5 estrelas.',0,NULL,'/avaliacoes/','2026-05-27 17:16:22.601813',1);
CREATE TABLE "pedidos_pedido" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "quantidade_solicitada" integer unsigned NOT NULL CHECK ("quantidade_solicitada" >= 0), "status" varchar(20) NOT NULL, "prioridade" varchar(10) NOT NULL, "justificativa" text NOT NULL, "observacoes" text NOT NULL, "codigo_rastreio" varchar(50) NOT NULL UNIQUE, "data_criacao" datetime NOT NULL, "data_atualizacao" datetime NOT NULL, "data_entrega" datetime NULL, "beneficiario_id" bigint NOT NULL REFERENCES "usuarios_usuario" ("id") DEFERRABLE INITIALLY DEFERRED, "doacao_id" bigint NOT NULL REFERENCES "doacoes_doacao" ("id") DEFERRABLE INITIALLY DEFERRED, "voluntario_id" bigint NULL REFERENCES "usuarios_usuario" ("id") DEFERRABLE INITIALLY DEFERRED, CONSTRAINT "chk_pedido_quantidade_positiva" CHECK ("quantidade_solicitada" >= 1), CONSTRAINT "chk_pedido_status_valido" CHECK ("status" IN ('pendente', 'aprovado', 'em_separacao', 'em_transito', 'entregue', 'cancelado')), CONSTRAINT "chk_pedido_prioridade_valida" CHECK ("prioridade" IN ('baixa', 'normal', 'alta', 'urgente')));
INSERT INTO "pedidos_pedido" VALUES(1,1,'entregue','normal','bih boh bohh','dadadadad','LSAD3F799F','2026-05-26 23:59:06.268627','2026-05-27 17:15:15.695232','2026-05-27 17:15:15.693497',4,1,NULL);
CREATE TABLE "rastreamento_eventorastreamento" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "tipo" varchar(20) NOT NULL, "descricao" text NOT NULL, "localizacao" varchar(200) NOT NULL, "automatico" bool NOT NULL, "data_evento" datetime NOT NULL, "pedido_id" bigint NOT NULL REFERENCES "pedidos_pedido" ("id") DEFERRABLE INITIALLY DEFERRED, "registrado_por_id" bigint NULL REFERENCES "usuarios_usuario" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "rastreamento_eventorastreamento" VALUES(1,'criado','Pedido criado pelo beneficiário.','',1,'2026-05-26 23:59:06.271848',1,4);
INSERT INTO "rastreamento_eventorastreamento" VALUES(2,'aprovado','Status atualizado para Aprovado.','',0,'2026-05-27 17:14:46.830442',1,1);
INSERT INTO "rastreamento_eventorastreamento" VALUES(3,'aprovado','Status atualizado para Aprovado.','',0,'2026-05-27 17:14:50.181946',1,1);
INSERT INTO "rastreamento_eventorastreamento" VALUES(4,'em_separacao','Status atualizado para Em separação.','',0,'2026-05-27 17:14:58.717389',1,1);
INSERT INTO "rastreamento_eventorastreamento" VALUES(5,'em_transito','Status atualizado para Em trânsito.','',0,'2026-05-27 17:15:07.593815',1,1);
INSERT INTO "rastreamento_eventorastreamento" VALUES(6,'entregue','Status atualizado para Entregue.','',0,'2026-05-27 17:15:15.697120',1,1);
CREATE TABLE "usuarios_usuario" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "first_name" varchar(150) NOT NULL, "last_name" varchar(150) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL, "tipo" varchar(20) NOT NULL, "telefone" varchar(20) NOT NULL, "cpf" varchar(14) NULL UNIQUE, "cidade" varchar(100) NOT NULL, "estado" varchar(2) NOT NULL, "foto" varchar(100) NULL, "bio" text NOT NULL, "data_cadastro" datetime NOT NULL, "cnpj" varchar(18) NULL UNIQUE, "pagina_descricao" text NOT NULL, "pagina_historia" text NOT NULL, "pagina_missao" text NOT NULL, "pagina_publicada" bool NOT NULL, "pagina_titulo" varchar(200) NOT NULL, "placa_veiculo" varchar(10) NOT NULL, "razao_social" varchar(200) NOT NULL, "tipo_veiculo" varchar(50) NOT NULL);
INSERT INTO "usuarios_usuario" VALUES(1,'pbkdf2_sha256$1200000$BO0WC24O47wUipavXMJOgu$Dd5fm8raqxL1YH41E8szw/FOVVdJjZ96Lj5dL/mzml0=','2026-05-27 17:34:56.978733',1,'emy','','','moonlightlana97@gmail.com',1,1,'2026-05-26 00:36:03.740392','doador','',NULL,'','','','','2026-05-26 00:36:03.896235',NULL,'','','',0,'','','','');
INSERT INTO "usuarios_usuario" VALUES(2,'pbkdf2_sha256$1200000$b4mHdfRHbqjDB8cMYUL9zi$noBgMrjhW4WN7pcNp9VWuIxLJbtp5epN2STlK/Emui0=',NULL,0,'emy_moon','','','',0,1,'2026-05-26 01:08:02.301550','doador','',NULL,'','','','','2026-05-26 01:08:02.454807',NULL,'','','',0,'','','','');
INSERT INTO "usuarios_usuario" VALUES(3,'pbkdf2_sha256$1200000$GacEsAF1gEXrX2sQUdI62J$NWVUACHLfjczyXFvKbVKNb8TRQHc4IWuEhbvHFL2ngI=','2026-05-26 17:46:59.687868',0,'mariobetuti78@gmail.com','Mario ','Betuti','mariobetuti78@gmail.com',0,1,'2026-05-26 17:46:59.541822','voluntario','8299999999','1414844848','Maceio','AL','','','2026-05-26 17:46:59.680471',NULL,'','','',0,'','','','');
INSERT INTO "usuarios_usuario" VALUES(4,'pbkdf2_sha256$1200000$jmlmAq8rYDJjeqRWyKZjeh$FyFMSp7OdGdCwq/L+SEYhLlG2RP4kRgadEeo8uapf8I=','2026-05-27 17:35:51.502026',0,'guilhermesouza98@gmail.com','Guilherme de souza','','guilhermesouza98@gmail.com',0,1,'2026-05-26 23:43:03.002977','ong','82 999999999',NULL,'Maceio','AL','','','2026-05-26 23:43:03.275321','141144645454545454454','blah blah blah','blah blah blah','blah blah blah',1,'Lar São Domingos:','','Lar São Domingos','');
INSERT INTO "usuarios_usuario" VALUES(5,'pbkdf2_sha256$1200000$uApek5marwCPGTbjp6BfTG$sB5048LeG9jkDkI9LfFKomTgxIPmNj1y6OJimeCX3aU=','2026-05-27 18:39:06.527075',0,'julio7890@gmail.com','julio','techos','julio7890@gmail.com',0,1,'2026-05-27 18:39:06.368511','voluntario','82 898898989','454545454','Maceio','AL','','','2026-05-27 18:39:06.519039',NULL,'','','',0,'','JHG-*8905','','caminhao');
CREATE TABLE "usuarios_usuario_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "usuario_id" bigint NOT NULL REFERENCES "usuarios_usuario" ("id") DEFERRABLE INITIALLY DEFERRED, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE "usuarios_usuario_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "usuario_id" bigint NOT NULL REFERENCES "usuarios_usuario" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE UNIQUE INDEX "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" ("app_label", "model");
CREATE UNIQUE INDEX "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" ("group_id", "permission_id");
CREATE INDEX "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" ("group_id");
CREATE INDEX "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" ("permission_id");
CREATE UNIQUE INDEX "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" ("content_type_id", "codename");
CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "auth_permission" ("content_type_id");
CREATE UNIQUE INDEX "usuarios_usuario_groups_usuario_id_group_id_4ed5b09e_uniq" ON "usuarios_usuario_groups" ("usuario_id", "group_id");
CREATE INDEX "usuarios_usuario_groups_usuario_id_7a34077f" ON "usuarios_usuario_groups" ("usuario_id");
CREATE INDEX "usuarios_usuario_groups_group_id_e77f6dcf" ON "usuarios_usuario_groups" ("group_id");
CREATE UNIQUE INDEX "usuarios_usuario_user_permissions_usuario_id_permission_id_217cadcd_uniq" ON "usuarios_usuario_user_permissions" ("usuario_id", "permission_id");
CREATE INDEX "usuarios_usuario_user_permissions_usuario_id_60aeea80" ON "usuarios_usuario_user_permissions" ("usuario_id");
CREATE INDEX "usuarios_usuario_user_permissions_permission_id_4e5c0f2f" ON "usuarios_usuario_user_permissions" ("permission_id");
CREATE INDEX "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" ("content_type_id");
CREATE INDEX "django_admin_log_user_id_c564eba6" ON "django_admin_log" ("user_id");
CREATE INDEX "django_session_expire_date_a5c62663" ON "django_session" ("expire_date");
CREATE INDEX "rastreamento_eventorastreamento_pedido_id_61d9fb50" ON "rastreamento_eventorastreamento" ("pedido_id");
CREATE INDEX "rastreamento_eventorastreamento_registrado_por_id_6bcf3f93" ON "rastreamento_eventorastreamento" ("registrado_por_id");
CREATE INDEX "notificacoes_notificacao_destinatario_id_0cc3ca16" ON "notificacoes_notificacao" ("destinatario_id");
CREATE INDEX "avaliacoes_avaliacao_avaliador_id_fa942c21" ON "avaliacoes_avaliacao" ("avaliador_id");
CREATE INDEX "doacoes_doacao_categoria_id_30ba3036" ON "doacoes_doacao" ("categoria_id");
CREATE INDEX "doacoes_doacao_doador_id_c4b60bed" ON "doacoes_doacao" ("doador_id");
CREATE INDEX "idx_doacao_status_cat" ON "doacoes_doacao" ("status", "categoria_id");
CREATE INDEX "idx_doacao_doador_status" ON "doacoes_doacao" ("doador_id", "status");
CREATE INDEX "pedidos_pedido_beneficiario_id_555928e2" ON "pedidos_pedido" ("beneficiario_id");
CREATE INDEX "pedidos_pedido_doacao_id_1de9903c" ON "pedidos_pedido" ("doacao_id");
CREATE INDEX "pedidos_pedido_voluntario_id_6d9b645d" ON "pedidos_pedido" ("voluntario_id");
CREATE INDEX "idx_pedido_rastreio" ON "pedidos_pedido" ("codigo_rastreio");
CREATE INDEX "idx_pedido_status_data" ON "pedidos_pedido" ("status", "data_criacao");
CREATE TRIGGER trg_evento_entregue
            AFTER INSERT ON rastreamento_eventorastreamento
            WHEN NEW.tipo = 'entregue'
            BEGIN
                UPDATE pedidos_pedido
                SET status = 'entregue',
                    data_entrega = datetime('now')
                WHERE id = NEW.pedido_id
                  AND status != 'entregue';
            END;
CREATE TRIGGER trg_evento_cancelado
            AFTER INSERT ON rastreamento_eventorastreamento
            WHEN NEW.tipo = 'cancelado'
            BEGIN
                UPDATE pedidos_pedido
                SET status = 'cancelado'
                WHERE id = NEW.pedido_id
                  AND status NOT IN ('entregue', 'cancelado');
            END;
CREATE VIEW vw_resumo_doacoes AS
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
CREATE VIEW vw_pedidos_completos AS
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
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('django_migrations',34);
INSERT INTO "sqlite_sequence" VALUES('django_content_type',12);
INSERT INTO "sqlite_sequence" VALUES('auth_permission',48);
INSERT INTO "sqlite_sequence" VALUES('auth_group',0);
INSERT INTO "sqlite_sequence" VALUES('django_admin_log',1);
INSERT INTO "sqlite_sequence" VALUES('usuarios_usuario',5);
INSERT INTO "sqlite_sequence" VALUES('doacoes_categoriadoacao',8);
INSERT INTO "sqlite_sequence" VALUES('rastreamento_eventorastreamento',6);
INSERT INTO "sqlite_sequence" VALUES('notificacoes_notificacao',7);
INSERT INTO "sqlite_sequence" VALUES('avaliacoes_avaliacao',1);
INSERT INTO "sqlite_sequence" VALUES('doacoes_doacao',1);
INSERT INTO "sqlite_sequence" VALUES('pedidos_pedido',1);
COMMIT;
