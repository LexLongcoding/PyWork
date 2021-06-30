BEGIN TRANSACTION;
DROP TABLE IF EXISTS "django_migrations";
CREATE TABLE IF NOT EXISTS "django_migrations" (
	"id"	integer NOT NULL,
	"app"	varchar(255) NOT NULL,
	"name"	varchar(255) NOT NULL,
	"applied"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "auth_group_permissions";
CREATE TABLE IF NOT EXISTS "auth_group_permissions" (
	"id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED
);
DROP TABLE IF EXISTS "auth_user_groups";
CREATE TABLE IF NOT EXISTS "auth_user_groups" (
	"id"	integer NOT NULL,
	"user_id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
DROP TABLE IF EXISTS "auth_user_user_permissions";
CREATE TABLE IF NOT EXISTS "auth_user_user_permissions" (
	"id"	integer NOT NULL,
	"user_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED
);
DROP TABLE IF EXISTS "django_admin_log";
CREATE TABLE IF NOT EXISTS "django_admin_log" (
	"id"	integer NOT NULL,
	"action_time"	datetime NOT NULL,
	"object_id"	text,
	"object_repr"	varchar(200) NOT NULL,
	"change_message"	text NOT NULL,
	"content_type_id"	integer,
	"user_id"	integer NOT NULL,
	"action_flag"	smallint unsigned NOT NULL CHECK("action_flag" >= 0),
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
DROP TABLE IF EXISTS "django_content_type";
CREATE TABLE IF NOT EXISTS "django_content_type" (
	"id"	integer NOT NULL,
	"app_label"	varchar(100) NOT NULL,
	"model"	varchar(100) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "auth_permission";
CREATE TABLE IF NOT EXISTS "auth_permission" (
	"id"	integer NOT NULL,
	"content_type_id"	integer NOT NULL,
	"codename"	varchar(100) NOT NULL,
	"name"	varchar(255) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED
);
DROP TABLE IF EXISTS "auth_group";
CREATE TABLE IF NOT EXISTS "auth_group" (
	"id"	integer NOT NULL,
	"name"	varchar(150) NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "auth_user";
CREATE TABLE IF NOT EXISTS "auth_user" (
	"id"	integer NOT NULL,
	"password"	varchar(128) NOT NULL,
	"last_login"	datetime,
	"is_superuser"	bool NOT NULL,
	"username"	varchar(150) NOT NULL UNIQUE,
	"last_name"	varchar(150) NOT NULL,
	"email"	varchar(254) NOT NULL,
	"is_staff"	bool NOT NULL,
	"is_active"	bool NOT NULL,
	"date_joined"	datetime NOT NULL,
	"first_name"	varchar(150) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "home_user";
CREATE TABLE IF NOT EXISTS "home_user" (
	"id"	integer NOT NULL,
	"username"	varchar(20) NOT NULL,
	"email"	varchar(254) NOT NULL UNIQUE,
	"password"	varchar(255) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "home_kit";
CREATE TABLE IF NOT EXISTS "home_kit" (
	"id"	integer NOT NULL,
	"title"	varchar(255) NOT NULL,
	"created_at"	datetime NOT NULL,
	"kick"	varchar(255) NOT NULL,
	"snare"	varchar(255) NOT NULL,
	"HHcl"	varchar(255) NOT NULL,
	"HHop"	varchar(255) NOT NULL,
	"crash"	varchar(255) NOT NULL,
	"ride"	varchar(255) NOT NULL,
	"tom_h"	varchar(255) NOT NULL,
	"tom_m"	varchar(255) NOT NULL,
	"tom_l"	varchar(255) NOT NULL,
	"perc"	varchar(255) NOT NULL,
	"creator_id"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("creator_id") REFERENCES "home_user"("id") DEFERRABLE INITIALLY DEFERRED
);
DROP TABLE IF EXISTS "home_kit_favorited_by";
CREATE TABLE IF NOT EXISTS "home_kit_favorited_by" (
	"id"	integer NOT NULL,
	"kit_id"	integer NOT NULL,
	"user_id"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("kit_id") REFERENCES "home_kit"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "home_user"("id") DEFERRABLE INITIALLY DEFERRED
);
DROP TABLE IF EXISTS "django_session";
CREATE TABLE IF NOT EXISTS "django_session" (
	"session_key"	varchar(40) NOT NULL,
	"session_data"	text NOT NULL,
	"expire_date"	datetime NOT NULL,
	PRIMARY KEY("session_key")
);
INSERT INTO "django_migrations" VALUES (1,'contenttypes','0001_initial','2021-03-15 18:35:35.397274');
INSERT INTO "django_migrations" VALUES (2,'auth','0001_initial','2021-03-15 18:35:35.583112');
INSERT INTO "django_migrations" VALUES (3,'admin','0001_initial','2021-03-15 18:35:35.742258');
INSERT INTO "django_migrations" VALUES (4,'admin','0002_logentry_remove_auto_add','2021-03-15 18:35:35.911624');
INSERT INTO "django_migrations" VALUES (5,'admin','0003_logentry_add_action_flag_choices','2021-03-15 18:35:36.089603');
INSERT INTO "django_migrations" VALUES (6,'contenttypes','0002_remove_content_type_name','2021-03-15 18:35:36.231142');
INSERT INTO "django_migrations" VALUES (7,'auth','0002_alter_permission_name_max_length','2021-03-15 18:35:36.609487');
INSERT INTO "django_migrations" VALUES (8,'auth','0003_alter_user_email_max_length','2021-03-15 18:35:36.835536');
INSERT INTO "django_migrations" VALUES (9,'auth','0004_alter_user_username_opts','2021-03-15 18:35:37.016940');
INSERT INTO "django_migrations" VALUES (10,'auth','0005_alter_user_last_login_null','2021-03-15 18:35:37.205487');
INSERT INTO "django_migrations" VALUES (11,'auth','0006_require_contenttypes_0002','2021-03-15 18:35:37.300727');
INSERT INTO "django_migrations" VALUES (12,'auth','0007_alter_validators_add_error_messages','2021-03-15 18:35:37.468554');
INSERT INTO "django_migrations" VALUES (13,'auth','0008_alter_user_username_max_length','2021-03-15 18:35:37.618598');
INSERT INTO "django_migrations" VALUES (14,'auth','0009_alter_user_last_name_max_length','2021-03-15 18:35:37.773076');
INSERT INTO "django_migrations" VALUES (15,'auth','0010_alter_group_name_max_length','2021-03-15 18:35:37.987565');
INSERT INTO "django_migrations" VALUES (16,'auth','0011_update_proxy_permissions','2021-03-15 18:35:38.126055');
INSERT INTO "django_migrations" VALUES (17,'auth','0012_alter_user_first_name_max_length','2021-03-15 18:35:38.253388');
INSERT INTO "django_migrations" VALUES (18,'home','0001_initial','2021-03-15 18:35:38.439385');
INSERT INTO "django_migrations" VALUES (19,'sessions','0001_initial','2021-03-15 18:35:38.704844');
INSERT INTO "django_migrations" VALUES (20,'home','0002_auto_20210315_1438','2021-03-16 16:28:09.815967');
INSERT INTO "django_content_type" VALUES (1,'home','user');
INSERT INTO "django_content_type" VALUES (2,'home','kit');
INSERT INTO "django_content_type" VALUES (3,'admin','logentry');
INSERT INTO "django_content_type" VALUES (4,'auth','permission');
INSERT INTO "django_content_type" VALUES (5,'auth','group');
INSERT INTO "django_content_type" VALUES (6,'auth','user');
INSERT INTO "django_content_type" VALUES (7,'contenttypes','contenttype');
INSERT INTO "django_content_type" VALUES (8,'sessions','session');
INSERT INTO "auth_permission" VALUES (1,1,'add_user','Can add user');
INSERT INTO "auth_permission" VALUES (2,1,'change_user','Can change user');
INSERT INTO "auth_permission" VALUES (3,1,'delete_user','Can delete user');
INSERT INTO "auth_permission" VALUES (4,1,'view_user','Can view user');
INSERT INTO "auth_permission" VALUES (5,2,'add_kit','Can add kit');
INSERT INTO "auth_permission" VALUES (6,2,'change_kit','Can change kit');
INSERT INTO "auth_permission" VALUES (7,2,'delete_kit','Can delete kit');
INSERT INTO "auth_permission" VALUES (8,2,'view_kit','Can view kit');
INSERT INTO "auth_permission" VALUES (9,3,'add_logentry','Can add log entry');
INSERT INTO "auth_permission" VALUES (10,3,'change_logentry','Can change log entry');
INSERT INTO "auth_permission" VALUES (11,3,'delete_logentry','Can delete log entry');
INSERT INTO "auth_permission" VALUES (12,3,'view_logentry','Can view log entry');
INSERT INTO "auth_permission" VALUES (13,4,'add_permission','Can add permission');
INSERT INTO "auth_permission" VALUES (14,4,'change_permission','Can change permission');
INSERT INTO "auth_permission" VALUES (15,4,'delete_permission','Can delete permission');
INSERT INTO "auth_permission" VALUES (16,4,'view_permission','Can view permission');
INSERT INTO "auth_permission" VALUES (17,5,'add_group','Can add group');
INSERT INTO "auth_permission" VALUES (18,5,'change_group','Can change group');
INSERT INTO "auth_permission" VALUES (19,5,'delete_group','Can delete group');
INSERT INTO "auth_permission" VALUES (20,5,'view_group','Can view group');
INSERT INTO "auth_permission" VALUES (21,6,'add_user','Can add user');
INSERT INTO "auth_permission" VALUES (22,6,'change_user','Can change user');
INSERT INTO "auth_permission" VALUES (23,6,'delete_user','Can delete user');
INSERT INTO "auth_permission" VALUES (24,6,'view_user','Can view user');
INSERT INTO "auth_permission" VALUES (25,7,'add_contenttype','Can add content type');
INSERT INTO "auth_permission" VALUES (26,7,'change_contenttype','Can change content type');
INSERT INTO "auth_permission" VALUES (27,7,'delete_contenttype','Can delete content type');
INSERT INTO "auth_permission" VALUES (28,7,'view_contenttype','Can view content type');
INSERT INTO "auth_permission" VALUES (29,8,'add_session','Can add session');
INSERT INTO "auth_permission" VALUES (30,8,'change_session','Can change session');
INSERT INTO "auth_permission" VALUES (31,8,'delete_session','Can delete session');
INSERT INTO "auth_permission" VALUES (32,8,'view_session','Can view session');
INSERT INTO "home_user" VALUES (1,'Drumbro','drumbro@mail.com','$2b$12$CnrXXcHSv0jRT8ZwF.iBnOVmFinyfV6T9GXkyoHcE9/BTXwOyr1MG');
INSERT INTO "home_user" VALUES (2,'Lex123','lex@mail.com','$2b$12$/S7JfXeBhhII0UR2k/5IVe9i/C6VH97.2g1SGLbs1WG2a3ir2TSnu');
INSERT INTO "home_user" VALUES (3,'snoopy','snoopy@mail.com','$2b$12$LkQvedu4w7hFPgfg8PJJd.DvRTt6GGZT.DnibyCyljP09Z9WMVkHC');
INSERT INTO "home_kit" VALUES (8,'Cool Kit','2021-03-22 00:24:27.025906','{''name'': ''Kick_Hard'', ''link'': '' https://dl.dropboxusercontent.com/s/r5283t60zqvplis/Kick%20%2836%29.wav?dl=1''}','{''name'': ''Snare_Clean'', ''link'': ''https://dl.dropboxusercontent.com/s/qe7r9jmxxdf96zj/Snaredrum-02.wav?dl=1''}','{''name'': ''HHcl_Python'', ''link'': ''https://dl.dropboxusercontent.com/s/fodzatigqr55euo/Hat%20Closed.wav?dl=1''}','{''name'': ''HHop_Electro'', ''link'': ''https://dl.dropboxusercontent.com/s/r9bod2je6bhs10s/Hat%20Open.wav?dl=1''}','{''name'': ''Crash_808'', ''link'': ''https://dl.dropboxusercontent.com/s/td2054lys8qiywh/Crash-01.wav?dl=1''}','{''name'': ''Ride_909'', ''link'': ''https://dl.dropboxusercontent.com/s/s6tp9jy5v71z1up/Ride.wav?dl=1''}','{''name'': ''TomH_Zap'', ''link'': ''https://dl.dropboxusercontent.com/s/km4zvtix9ha8z24/Tom-09.wav?dl=1''}','{''name'': ''TomM_Yamaha'', ''link'': ''https://dl.dropboxusercontent.com/s/5rzionupibedj7z/TOMS_003.wav?dl=1''}','{''name'': ''TomL_808'', ''link'': ''https://dl.dropboxusercontent.com/s/4i2krdetdv3dify/Tom%20L.wav?dl=1''}','{''name'': ''Perc_Flick'', ''link'': ''https://dl.dropboxusercontent.com/s/xm3f3ki2m7me9gk/Flick01.wav?dl=1''}',3);
INSERT INTO "home_kit" VALUES (9,'Sweet Kit','2021-03-22 00:34:11.822471','{''name'': ''Kick_Smoothie'', ''link'': ''https://dl.dropboxusecontent.com/s/5h7urpvtlyjw0nu/Bassdrum-37.wav?dl=1''}','{''name'': ''Snare_Nice'', ''link'': ''https://dl.dropboxusercontent.com/s/fkmb1x7bue4o2m9/Snaredrum.wav?dl=1''}','{''name'': ''HHcl_Python'', ''link'': ''https://dl.dropboxusercontent.com/s/fodzatigqr55euo/Hat%20Closed.wav?dl=1''}','{''name'': ''HHop_Real'', ''link'': ''https://dl.dropboxusercontent.com/s/rkekcb4v1dbezb6/Real_HHop.WAV?dl=1''}','{''name'': ''Crash_Real'', ''link'': ''https://dl.dropboxusercontent.com/s/m0ebmc9r78zteks/Real.wav?dl=1''}','{''name'': ''Ride_Z'', ''link'': ''https://dl.dropboxusercontent.com/s/xz37o5has4lbx3b/DT_RD_zildjan.WAV?dl=1''}','{''name'': ''TomH_Sensei'', ''link'': '' https://dl.dropboxusercontent.com/s/n0nehc5n39cn38v/Sensei.wav?dl=1''}','{''name'': ''TomM_Yamaha'', ''link'': ''https://dl.dropboxusercontent.com/s/5rzionupibedj7z/TOMS_003.wav?dl=1''}','{''name'': ''TomL_Epic'', ''link'': ''https://dl.dropboxusercontent.com/s/nslpqnam6i2r6xh/Toml%20L-03.wav?dl=1''}','{''name'': ''Perc_Chime'', ''link'': ''https://dl.dropboxusercontent.com/s/6twaympvyf1f387/Chime.wav?dl=1''}',4);
INSERT INTO "home_kit" VALUES (12,'Late Night Kit','2021-03-22 06:04:52.849176','{''name'': ''Kick_Hard'', ''link'': '' https://dl.dropboxusercontent.com/s/r5283t60zqvplis/Kick%20%2836%29.wav?dl=1''}','{''name'': ''Snare_Fake'', ''link'': ''https://dl.dropboxusercontent.com/s/nwlem2u55u3ey8j/Snaredrum-17.wav?dl=1''}','{''name'': ''HHcl_Fire'', ''link'': ''https://dl.dropboxusercontent.com/s/f4yxwjk985uodtv/Hat%20Closed-01.wav?dl=1''}','{''name'': ''HHop_ninja'', ''link'': ''https://dl.dropboxusercontent.com/s/qvt3nmlcbe97p00/Ninja_HHop.WAV?dl=1''}','{''name'': ''Crash_Bold'', ''link'': ''https://dl.dropboxusercontent.com/s/pyom0bgpl8mught/Crash.wav?dl=1''}','{''name'': ''Ride_Django'', ''link'': ''https://dl.dropboxusercontent.com/s/2z1m8p2a5t64czb/Ride.wav?dl=1''}','{''name'': ''TomH_Boop'', ''link'': ''https://dl.dropboxusercontent.com/s/cm8obyt7m80oeza/Achitom1.wav?dl=1''}','{''name'': ''TomM_Mid'', ''link'': ''https://dl.dropboxusercontent.com/s/sq5fm7jqvdecfkp/MT0D7.WAV?dl=1''}','{''name'': ''TomL_808'', ''link'': ''https://dl.dropboxusercontent.com/s/4i2krdetdv3dify/Tom%20L.wav?dl=1''}','{''name'': ''Perc_Bit'', ''link'': ''https://dl.dropboxusercontent.com/s/pwmqqwkg2mpo6jt/STAY_SE_00014.wav?dl=1''}',3);
INSERT INTO "home_kit_favorited_by" VALUES (1,10,3);
INSERT INTO "home_kit_favorited_by" VALUES (2,11,3);
INSERT INTO "home_kit_favorited_by" VALUES (5,9,3);
INSERT INTO "home_kit_favorited_by" VALUES (6,12,3);
INSERT INTO "django_session" VALUES ('9uihfxicd2tow10b8i2k6iexo1drxygw','eyJ1c2VyX2lkIjozfQ:1lOEFf:SjC-oIdcRPklKU9nitxn9oElaETrg3_948jVXgyhuXo','2021-04-05 06:41:23.996420');
DROP INDEX IF EXISTS "auth_group_permissions_group_id_permission_id_0cd325b0_uniq";
CREATE UNIQUE INDEX IF NOT EXISTS "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" (
	"group_id",
	"permission_id"
);
DROP INDEX IF EXISTS "auth_group_permissions_group_id_b120cbf9";
CREATE INDEX IF NOT EXISTS "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" (
	"group_id"
);
DROP INDEX IF EXISTS "auth_group_permissions_permission_id_84c5c92e";
CREATE INDEX IF NOT EXISTS "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" (
	"permission_id"
);
DROP INDEX IF EXISTS "auth_user_groups_user_id_group_id_94350c0c_uniq";
CREATE UNIQUE INDEX IF NOT EXISTS "auth_user_groups_user_id_group_id_94350c0c_uniq" ON "auth_user_groups" (
	"user_id",
	"group_id"
);
DROP INDEX IF EXISTS "auth_user_groups_user_id_6a12ed8b";
CREATE INDEX IF NOT EXISTS "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" (
	"user_id"
);
DROP INDEX IF EXISTS "auth_user_groups_group_id_97559544";
CREATE INDEX IF NOT EXISTS "auth_user_groups_group_id_97559544" ON "auth_user_groups" (
	"group_id"
);
DROP INDEX IF EXISTS "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq";
CREATE UNIQUE INDEX IF NOT EXISTS "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" ON "auth_user_user_permissions" (
	"user_id",
	"permission_id"
);
DROP INDEX IF EXISTS "auth_user_user_permissions_user_id_a95ead1b";
CREATE INDEX IF NOT EXISTS "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" (
	"user_id"
);
DROP INDEX IF EXISTS "auth_user_user_permissions_permission_id_1fbb5f2c";
CREATE INDEX IF NOT EXISTS "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" (
	"permission_id"
);
DROP INDEX IF EXISTS "django_admin_log_content_type_id_c4bce8eb";
CREATE INDEX IF NOT EXISTS "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" (
	"content_type_id"
);
DROP INDEX IF EXISTS "django_admin_log_user_id_c564eba6";
CREATE INDEX IF NOT EXISTS "django_admin_log_user_id_c564eba6" ON "django_admin_log" (
	"user_id"
);
DROP INDEX IF EXISTS "django_content_type_app_label_model_76bd3d3b_uniq";
CREATE UNIQUE INDEX IF NOT EXISTS "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" (
	"app_label",
	"model"
);
DROP INDEX IF EXISTS "auth_permission_content_type_id_codename_01ab375a_uniq";
CREATE UNIQUE INDEX IF NOT EXISTS "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" (
	"content_type_id",
	"codename"
);
DROP INDEX IF EXISTS "auth_permission_content_type_id_2f476e4b";
CREATE INDEX IF NOT EXISTS "auth_permission_content_type_id_2f476e4b" ON "auth_permission" (
	"content_type_id"
);
DROP INDEX IF EXISTS "home_kit_creator_id_a24fa0be";
CREATE INDEX IF NOT EXISTS "home_kit_creator_id_a24fa0be" ON "home_kit" (
	"creator_id"
);
DROP INDEX IF EXISTS "home_kit_favorited_by_kit_id_user_id_ec371a32_uniq";
CREATE UNIQUE INDEX IF NOT EXISTS "home_kit_favorited_by_kit_id_user_id_ec371a32_uniq" ON "home_kit_favorited_by" (
	"kit_id",
	"user_id"
);
DROP INDEX IF EXISTS "home_kit_favorited_by_kit_id_b3aa86df";
CREATE INDEX IF NOT EXISTS "home_kit_favorited_by_kit_id_b3aa86df" ON "home_kit_favorited_by" (
	"kit_id"
);
DROP INDEX IF EXISTS "home_kit_favorited_by_user_id_103207f6";
CREATE INDEX IF NOT EXISTS "home_kit_favorited_by_user_id_103207f6" ON "home_kit_favorited_by" (
	"user_id"
);
DROP INDEX IF EXISTS "django_session_expire_date_a5c62663";
CREATE INDEX IF NOT EXISTS "django_session_expire_date_a5c62663" ON "django_session" (
	"expire_date"
);
COMMIT;
