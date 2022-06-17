import pytest
from pytest_mock import MockerFixture

from aerich.ddl.mysql import MysqlDDL
from aerich.ddl.postgres import PostgresDDL
from aerich.ddl.sqlite import SqliteDDL
from aerich.exceptions import NotSupportError
from aerich.migrate import Migrate
from aerich.utils import get_models_describe

old_models_describe = {
    "models.Category": {
        "name": "models.Category",
        "app": "models",
        "table": "category",
        "abstract": False,
        "description": None,
        "docstring": None,
        "unique_together": [],
        "indexes": [],
        "pk_field": {
            "name": "id",
            "field_type": "IntField",
            "db_column": "id",
            "python_type": "int",
            "generated": True,
            "nullable": False,
            "unique": True,
            "indexed": True,
            "default": None,
            "description": None,
            "docstring": None,
            "constraints": {"ge": 1, "le": 2147483647},
            "db_field_types": {"": "INT"},
        },
        "data_fields": [
            {
                "name": "slug",
                "field_type": "CharField",
                "db_column": "slug",
                "python_type": "str",
                "generated": False,
                "nullable": False,
                "unique": False,
                "indexed": False,
                "default": None,
                "description": None,
                "docstring": None,
                "constraints": {"max_length": 200},
                "db_field_types": {"": "VARCHAR(200)"},
            },
            {
                "name": "name",
                "field_type": "CharField",
                "db_column": "name",
                "python_type": "str",
                "generated": False,
                "nullable": False,
                "unique": False,
                "indexed": False,
                "default": None,
                "description": None,
                "docstring": None,
                "constraints": {"max_length": 200},
                "db_field_types": {"": "VARCHAR(200)"},
            },
            {
                "name": "created_at",
                "field_type": "DatetimeField",
                "db_column": "created_at",
                "python_type": "datetime.datetime",
                "generated": False,
                "nullable": False,
                "unique": False,
                "indexed": False,
                "default": None,
                "description": None,
                "docstring": None,
                "constraints": {"readOnly": True},
                "db_field_types": {
                    "": "TIMESTAMP",
                    "mysql": "DATETIME(6)",
                    "postgres": "TIMESTAMPTZ",
                },
                "auto_now_add": True,
                "auto_now": False,
            },
            {
                "name": "user_id",
                "field_type": "IntField",
                "db_column": "user_id",
                "python_type": "int",
                "generated": False,
                "nullable": False,
                "unique": False,
                "indexed": False,
                "default": None,
                "description": "User",
                "docstring": None,
                "constraints": {"ge": 1, "le": 2147483647},
                "db_field_types": {"": "INT"},
            },
        ],
        "fk_fields": [
            {
                "name": "user",
                "field_type": "ForeignKeyFieldInstance",
                "python_type": "models.User",
                "generated": False,
                "nullable": False,
                "unique": False,
                "indexed": False,
                "default": None,
                "description": "User",
                "docstring": None,
                "constraints": {},
                "raw_field": "user_id",
                "on_delete": "CASCADE",
            }
        ],
        "backward_fk_fields": [],
        "o2o_fields": [],
        "backward_o2o_fields": [],
        "m2m_fields": [
            {
                "name": "products",
                "field_type": "ManyToManyFieldInstance",
                "python_type": "models.Product",
                "generated": False,
                "nullable": False,
                "unique": False,
                "indexed": False,
                "default": None,
                "description": None,
                "docstring": None,
                "constraints": {},
                "model_name": "models.Product",
                "related_name": "categories",
                "forward_key": "product_id",
                "backward_key": "category_id",
                "through": "product_category",
                "on_delete": "CASCADE",
                "_generated": True,
            }
        ],
    },
    "models.Config": {
        "name": "models.Config",
        "app": "models",
        "table": "configs",
        "abstract": False,
        "description": None,
        "docstring": None,
        "unique_together": [],
        "indexes": [],
        "pk_field": {
            "name": "id",
            "field_type": "IntField",
            "db_column": "id",
            "python_type": "int",
            "generated": True,
            "nullable": False,
            "unique": True,
            "indexed": True,
            "default": None,
            "description": None,
            "docstring": None,
            "constraints": {"ge": 1, "le": 2147483647},
            "db_field_types": {"": "INT"},
        },
        "data_fields": [
            {
                "name": "label",
                "field_type": "CharField",
                "db_column": "label",
                "python_type": "str",
                "generated": False,
                "nullable": False,
                "unique": False,
                "indexed": False,
                "default": None,
                "description": None,
                "docstring": None,
                "constraints": {"max_length": 200},
                "db_field_types": {"": "VARCHAR(200)"},
            },
            {
                "name": "key",
                "field_type": "CharField",
                "db_column": "key",
                "python_type": "str",
                "generated": False,
                "nullable": False,
                "unique": False,
                "indexed": False,
                "default": None,
                "description": None,
                "docstring": None,
                "constraints": {"max_length": 20},
                "db_field_types": {"": "VARCHAR(20)"},
            },
            {
                "name": "value",
                "field_type": "JSONField",
                "db_column": "value",
                "python_type": "Union[dict, list]",
                "generated": False,
                "nullable": False,
                "unique": False,
                "indexed": False,
                "default": None,
                "description": None,
                "docstring": None,
                "constraints": {},
                "db_field_types": {"": "TEXT", "postgres": "JSONB"},
            },
            {
                "name": "status",
                "field_type": "IntEnumFieldInstance",
                "db_column": "status",
                "python_type": "int",
                "generated": False,
                "nullable": False,
                "unique": False,
                "indexed": False,
                "default": 1,
                "description": "on: 1\noff: 0",
                "docstring": None,
                "constraints": {"ge": -32768, "le": 32767},
                "db_field_types": {"": "SMALLINT"},
            },
        ],
        "fk_fields": [],
        "backward_fk_fields": [],
        "o2o_fields": [],
        "backward_o2o_fields": [],
        "m2m_fields": [],
    },
    "models.Email": {
        "name": "models.Email",
        "app": "models",
        "table": "email",
        "abstract": False,
        "description": None,
        "docstring": None,
        "unique_together": [],
        "indexes": [],
        "pk_field": {
            "name": "id",
            "field_type": "IntField",
            "db_column": "id",
            "python_type": "int",
            "generated": True,
            "nullable": False,
            "unique": True,
            "indexed": True,
            "default": None,
            "description": None,
            "docstring": None,
            "constraints": {"ge": 1, "le": 2147483647},
            "db_field_types": {"": "INT"},
        },
        "data_fields": [
            {
                "name": "email",
                "field_type": "CharField",
                "db_column": "email",
                "python_type": "str",
                "generated": False,
                "nullable": False,
                "unique": False,
                "indexed": False,
                "default": None,
                "description": None,
                "docstring": None,
                "constraints": {"max_length": 200},
                "db_field_types": {"": "VARCHAR(200)"},
            },
            {
                "name": "is_primary",
                "field_type": "BooleanField",
                "db_column": "is_primary",
                "python_type": "bool",
                "generated": False,
                "nullable": False,
                "unique": False,
                "indexed": False,
                "default": False,
                "description": None,
                "docstring": None,
                "constraints": {},
                "db_field_types": {"": "BOOL", "sqlite": "INT"},
            },
            {
                "name": "user_id",
                "field_type": "IntField",
                "db_column": "user_id",
                "python_type": "int",
                "generated": False,
                "nullable": False,
                "unique": False,
                "indexed": False,
                "default": None,
                "description": None,
                "docstring": None,
                "constraints": {"ge": 1, "le": 2147483647},
                "db_field_types": {"": "INT"},
            },
        ],
        "fk_fields": [
            {
                "name": "user",
                "field_type": "ForeignKeyFieldInstance",
                "python_type": "models.User",
                "generated": False,
                "nullable": False,
                "unique": False,
                "indexed": False,
                "default": None,
                "description": None,
                "docstring": None,
                "constraints": {},
                "raw_field": "user_id",
                "on_delete": "CASCADE",
            }
        ],
        "backward_fk_fields": [],
        "o2o_fields": [],
        "backward_o2o_fields": [],
        "m2m_fields": [],
    },
    "models.Product": {
        "name": "models.Product",
        "app": "models",
        "table": "product",
        "abstract": False,
        "description": None,
        "docstring": None,
        "unique_together": [],
        "indexes": [],
        "pk_field": {
            "name": "id",
            "field_type": "IntField",
            "db_column": "id",
            "python_type": "int",
            "generated": True,
            "nullable": False,
            "unique": True,
            "indexed": True,
            "default": None,
            "description": None,
            "docstring": None,
            "constraints": {"ge": 1, "le": 2147483647},
            "db_field_types": {"": "INT"},
        },
        "data_fields": [
            {
                "name": "name",
                "field_type": "CharField",
                "db_column": "name",
                "python_type": "str",
                "generated": False,
                "nullable": False,
                "unique": False,
                "indexed": False,
                "default": None,
                "description": None,
                "docstring": None,
                "constraints": {"max_length": 50},
                "db_field_types": {"": "VARCHAR(50)"},
            },
            {
                "name": "view_num",
                "field_type": "IntField",
                "db_column": "view_num",
                "python_type": "int",
                "generated": False,
                "nullable": False,
                "unique": False,
                "indexed": False,
                "default": None,
                "description": "View Num",
                "docstring": None,
                "constraints": {"ge": -2147483648, "le": 2147483647},
                "db_field_types": {"": "INT"},
            },
            {
                "name": "sort",
                "field_type": "IntField",
                "db_column": "sort",
                "python_type": "int",
                "generated": False,
                "nullable": False,
                "unique": False,
                "indexed": False,
                "default": None,
                "description": None,
                "docstring": None,
                "constraints": {"ge": -2147483648, "le": 2147483647},
                "db_field_types": {"": "INT"},
            },
            {
                "name": "is_reviewed",
                "field_type": "BooleanField",
                "db_column": "is_reviewed",
                "python_type": "bool",
                "generated": False,
                "nullable": False,
                "unique": False,
                "indexed": False,
                "default": None,
                "description": "Is Reviewed",
                "docstring": None,
                "constraints": {},
                "db_field_types": {"": "BOOL", "sqlite": "INT"},
            },
            {
                "name": "type",
                "field_type": "IntEnumFieldInstance",
                "db_column": "type_db_alias",
                "python_type": "int",
                "generated": False,
                "nullable": False,
                "unique": False,
                "indexed": False,
                "default": None,
                "description": "Product Type",
                "docstring": None,
                "constraints": {"ge": -32768, "le": 32767},
                "db_field_types": {"": "SMALLINT"},
            },
            {
                "name": "image",
                "field_type": "CharField",
                "db_column": "image",
                "python_type": "str",
                "generated": False,
                "nullable": False,
                "unique": False,
                "indexed": False,
                "default": None,
                "description": None,
                "docstring": None,
                "constraints": {"max_length": 200},
                "db_field_types": {"": "VARCHAR(200)"},
            },
            {
                "name": "body",
                "field_type": "TextField",
                "db_column": "body",
                "python_type": "str",
                "generated": False,
                "nullable": False,
                "unique": False,
                "indexed": False,
                "default": None,
                "description": None,
                "docstring": None,
                "constraints": {},
                "db_field_types": {"": "TEXT", "mysql": "LONGTEXT"},
            },
            {
                "name": "created_at",
                "field_type": "DatetimeField",
                "db_column": "created_at",
                "python_type": "datetime.datetime",
                "generated": False,
                "nullable": False,
                "unique": False,
                "indexed": False,
                "default": None,
                "description": None,
                "docstring": None,
                "constraints": {"readOnly": True},
                "db_field_types": {
                    "": "TIMESTAMP",
                    "mysql": "DATETIME(6)",
                    "postgres": "TIMESTAMPTZ",
                },
                "auto_now_add": True,
                "auto_now": False,
            },
        ],
        "fk_fields": [],
        "backward_fk_fields": [],
        "o2o_fields": [],
        "backward_o2o_fields": [],
        "m2m_fields": [
            {
                "name": "categories",
                "field_type": "ManyToManyFieldInstance",
                "python_type": "models.Category",
                "generated": False,
                "nullable": False,
                "unique": False,
                "indexed": False,
                "default": None,
                "description": None,
                "docstring": None,
                "constraints": {},
                "model_name": "models.Category",
                "related_name": "products",
                "forward_key": "category_id",
                "backward_key": "product_id",
                "through": "product_category",
                "on_delete": "CASCADE",
                "_generated": False,
            }
        ],
    },
    "models.User": {
        "name": "models.User",
        "app": "models",
        "table": "user",
        "abstract": False,
        "description": None,
        "docstring": None,
        "unique_together": [],
        "indexes": [],
        "pk_field": {
            "name": "id",
            "field_type": "IntField",
            "db_column": "id",
            "python_type": "int",
            "generated": True,
            "nullable": False,
            "unique": True,
            "indexed": True,
            "default": None,
            "description": None,
            "docstring": None,
            "constraints": {"ge": 1, "le": 2147483647},
            "db_field_types": {"": "INT"},
        },
        "data_fields": [
            {
                "name": "username",
                "field_type": "CharField",
                "db_column": "username",
                "python_type": "str",
                "generated": False,
                "nullable": False,
                "unique": False,
                "indexed": False,
                "default": None,
                "description": None,
                "docstring": None,
                "constraints": {"max_length": 20},
                "db_field_types": {"": "VARCHAR(20)"},
            },
            {
                "name": "password",
                "field_type": "CharField",
                "db_column": "password",
                "python_type": "str",
                "generated": False,
                "nullable": False,
                "unique": False,
                "indexed": False,
                "default": None,
                "description": None,
                "docstring": None,
                "constraints": {"max_length": 200},
                "db_field_types": {"": "VARCHAR(200)"},
            },
            {
                "name": "last_login",
                "field_type": "DatetimeField",
                "db_column": "last_login",
                "python_type": "datetime.datetime",
                "generated": False,
                "nullable": False,
                "unique": False,
                "indexed": False,
                "default": "<function None.now>",
                "description": "Last Login",
                "docstring": None,
                "constraints": {},
                "db_field_types": {
                    "": "TIMESTAMP",
                    "mysql": "DATETIME(6)",
                    "postgres": "TIMESTAMPTZ",
                },
                "auto_now_add": False,
                "auto_now": False,
            },
            {
                "name": "is_active",
                "field_type": "BooleanField",
                "db_column": "is_active",
                "python_type": "bool",
                "generated": False,
                "nullable": False,
                "unique": False,
                "indexed": False,
                "default": True,
                "description": "Is Active",
                "docstring": None,
                "constraints": {},
                "db_field_types": {"": "BOOL", "sqlite": "INT"},
            },
            {
                "name": "is_superuser",
                "field_type": "BooleanField",
                "db_column": "is_superuser",
                "python_type": "bool",
                "generated": False,
                "nullable": False,
                "unique": False,
                "indexed": False,
                "default": False,
                "description": "Is SuperUser",
                "docstring": None,
                "constraints": {},
                "db_field_types": {"": "BOOL", "sqlite": "INT"},
            },
            {
                "name": "avatar",
                "field_type": "CharField",
                "db_column": "avatar",
                "python_type": "str",
                "generated": False,
                "nullable": False,
                "unique": False,
                "indexed": False,
                "default": "",
                "description": None,
                "docstring": None,
                "constraints": {"max_length": 200},
                "db_field_types": {"": "VARCHAR(200)"},
            },
            {
                "name": "intro",
                "field_type": "TextField",
                "db_column": "intro",
                "python_type": "str",
                "generated": False,
                "nullable": False,
                "unique": False,
                "indexed": False,
                "default": "",
                "description": None,
                "docstring": None,
                "constraints": {},
                "db_field_types": {"": "TEXT", "mysql": "LONGTEXT"},
            },
        ],
        "fk_fields": [],
        "backward_fk_fields": [
            {
                "name": "categorys",
                "field_type": "BackwardFKRelation",
                "python_type": "models.Category",
                "generated": False,
                "nullable": False,
                "unique": False,
                "indexed": False,
                "default": None,
                "description": "User",
                "docstring": None,
                "constraints": {},
            },
            {
                "name": "emails",
                "field_type": "BackwardFKRelation",
                "python_type": "models.Email",
                "generated": False,
                "nullable": False,
                "unique": False,
                "indexed": False,
                "default": None,
                "description": None,
                "docstring": None,
                "constraints": {},
            },
        ],
        "o2o_fields": [],
        "backward_o2o_fields": [],
        "m2m_fields": [],
    },
    "models.Aerich": {
        "name": "models.Aerich",
        "app": "models",
        "table": "aerich",
        "abstract": False,
        "description": None,
        "docstring": None,
        "unique_together": [],
        "indexes": [],
        "pk_field": {
            "name": "id",
            "field_type": "IntField",
            "db_column": "id",
            "python_type": "int",
            "generated": True,
            "nullable": False,
            "unique": True,
            "indexed": True,
            "default": None,
            "description": None,
            "docstring": None,
            "constraints": {"ge": 1, "le": 2147483647},
            "db_field_types": {"": "INT"},
        },
        "data_fields": [
            {
                "name": "version",
                "field_type": "CharField",
                "db_column": "version",
                "python_type": "str",
                "generated": False,
                "nullable": False,
                "unique": False,
                "indexed": False,
                "default": None,
                "description": None,
                "docstring": None,
                "constraints": {"max_length": 255},
                "db_field_types": {"": "VARCHAR(255)"},
            },
            {
                "name": "app",
                "field_type": "CharField",
                "db_column": "app",
                "python_type": "str",
                "generated": False,
                "nullable": False,
                "unique": False,
                "indexed": False,
                "default": None,
                "description": None,
                "docstring": None,
                "constraints": {"max_length": 20},
                "db_field_types": {"": "VARCHAR(20)"},
            },
            {
                "name": "content",
                "field_type": "JSONField",
                "db_column": "content",
                "python_type": "Union[dict, list]",
                "generated": False,
                "nullable": False,
                "unique": False,
                "indexed": False,
                "default": None,
                "description": None,
                "docstring": None,
                "constraints": {},
                "db_field_types": {"": "TEXT", "postgres": "JSONB"},
            },
        ],
        "fk_fields": [],
        "backward_fk_fields": [],
        "o2o_fields": [],
        "backward_o2o_fields": [],
        "m2m_fields": [],
    },
}


def test_migrate(mocker: MockerFixture):
    """
    models.py diff with old_models.py
    - change email pk: id -> email_id
    - add field: Email.address
    - add fk: Config.user
    - drop fk: Email.user
    - drop field: User.avatar
    - add index: Email.email
    - add many to many: Email.users
    - remove unique: User.username
    - change column: length User.password
    - add unique_together: (name,type) of Product
    - alter default: Config.status
    - rename column: Product.image -> Product.pic
    """
    mocker.patch("click.prompt", side_effect=(True,))

    models_describe = get_models_describe("models")
    Migrate.app = "models"
    if isinstance(Migrate.ddl, SqliteDDL):
        with pytest.raises(NotSupportError):
            Migrate.diff_models(old_models_describe, models_describe)
            Migrate.diff_models(models_describe, old_models_describe, False)
    else:
        Migrate.diff_models(old_models_describe, models_describe)
        Migrate.diff_models(models_describe, old_models_describe, False)
    Migrate._merge_operators()
    if isinstance(Migrate.ddl, MysqlDDL):
        assert sorted(Migrate.upgrade_operators) == sorted(
            [
                "ALTER TABLE `category` MODIFY COLUMN `name` VARCHAR(200)",
                "ALTER TABLE `category` MODIFY COLUMN `slug` VARCHAR(100) NOT NULL",
                "ALTER TABLE `config` ADD `user_id` INT NOT NULL  COMMENT 'User'",
                "ALTER TABLE `config` ADD CONSTRAINT `fk_config_user_17daa970` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE",
                "ALTER TABLE `config` ALTER COLUMN `status` DROP DEFAULT",
                "ALTER TABLE `email` ADD `address` VARCHAR(200) NOT NULL",
                "ALTER TABLE `email` DROP COLUMN `user_id`",
                "ALTER TABLE `configs` RENAME TO `config`",
                "ALTER TABLE `product` RENAME COLUMN `image` TO `pic`",
                "ALTER TABLE `email` RENAME COLUMN `id` TO `email_id`",
                "ALTER TABLE `product` ADD INDEX `idx_product_name_869427` (`name`, `type_db_alias`)",
                "ALTER TABLE `email` ADD INDEX `idx_email_email_4a1a33` (`email`)",
                "ALTER TABLE `product` ADD UNIQUE INDEX `uid_product_name_869427` (`name`, `type_db_alias`)",
                "ALTER TABLE `product` ALTER COLUMN `view_num` SET DEFAULT 0",
                "ALTER TABLE `user` DROP COLUMN `avatar`",
                "ALTER TABLE `user` MODIFY COLUMN `password` VARCHAR(100) NOT NULL",
                "CREATE TABLE IF NOT EXISTS `newmodel` (\n    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,\n    `name` VARCHAR(50) NOT NULL\n) CHARACTER SET utf8mb4;",
                "ALTER TABLE `user` ADD UNIQUE INDEX `uid_user_usernam_9987ab` (`username`)",
                "CREATE TABLE `email_user` (`email_id` INT NOT NULL REFERENCES `email` (`email_id`) ON DELETE CASCADE,`user_id` INT NOT NULL REFERENCES `user` (`id`) ON DELETE CASCADE) CHARACTER SET utf8mb4",
            ]
        )

        assert sorted(Migrate.downgrade_operators) == sorted(
            [
                "ALTER TABLE `category` MODIFY COLUMN `name` VARCHAR(200) NOT NULL",
                "ALTER TABLE `category` MODIFY COLUMN `slug` VARCHAR(200) NOT NULL",
                "ALTER TABLE `config` DROP COLUMN `user_id`",
                "ALTER TABLE `config` DROP FOREIGN KEY `fk_config_user_17daa970`",
                "ALTER TABLE `config` ALTER COLUMN `status` SET DEFAULT 1",
                "ALTER TABLE `email` ADD `user_id` INT NOT NULL",
                "ALTER TABLE `email` DROP COLUMN `address`",
                "ALTER TABLE `config` RENAME TO `configs`",
                "ALTER TABLE `product` RENAME COLUMN `pic` TO `image`",
                "ALTER TABLE `email` RENAME COLUMN `email_id` TO `id`",
                "ALTER TABLE `product` DROP INDEX `idx_product_name_869427`",
                "ALTER TABLE `email` DROP INDEX `idx_email_email_4a1a33`",
                "ALTER TABLE `product` DROP INDEX `uid_product_name_869427`",
                "ALTER TABLE `product` ALTER COLUMN `view_num` DROP DEFAULT",
                "ALTER TABLE `user` ADD `avatar` VARCHAR(200) NOT NULL  DEFAULT ''",
                "ALTER TABLE `user` DROP INDEX `idx_user_usernam_9987ab`",
                "ALTER TABLE `user` MODIFY COLUMN `password` VARCHAR(200) NOT NULL",
                "DROP TABLE IF EXISTS `email_user`",
                "DROP TABLE IF EXISTS `newmodel`",
            ]
        )

    elif isinstance(Migrate.ddl, PostgresDDL):
        expected_upgrade_operators = set([
            'ALTER TABLE "category" ALTER COLUMN "name" DROP NOT NULL',
            'ALTER TABLE "category" ALTER COLUMN "slug" TYPE VARCHAR(100) USING "slug"::VARCHAR(100)',
            'ALTER TABLE "category" ALTER COLUMN "created_at" TYPE TIMESTAMPTZ USING "created_at"::TIMESTAMPTZ',
            'ALTER TABLE "config" ADD "user_id" INT NOT NULL',
            'ALTER TABLE "config" ADD CONSTRAINT "fk_config_user_17daa970" FOREIGN KEY ("user_id") REFERENCES "user" ("id") ON DELETE CASCADE',
            'ALTER TABLE "config" ALTER COLUMN "status" DROP DEFAULT',
            'ALTER TABLE "config" ALTER COLUMN "value" TYPE JSONB USING "value"::JSONB',
            'ALTER TABLE "configs" RENAME TO "config"',
            'ALTER TABLE "email" ADD "address" VARCHAR(200) NOT NULL',
            'ALTER TABLE "email" DROP COLUMN "user_id"',
            'ALTER TABLE "email" RENAME COLUMN "id" TO "email_id"',
            'ALTER TABLE "email" ALTER COLUMN "is_primary" TYPE BOOL USING "is_primary"::BOOL',
            'ALTER TABLE "product" ALTER COLUMN "view_num" SET DEFAULT 0',
            'ALTER TABLE "product" RENAME COLUMN "image" TO "pic"',
            'ALTER TABLE "product" ALTER COLUMN "is_reviewed" TYPE BOOL USING "is_reviewed"::BOOL',
            'ALTER TABLE "product" ALTER COLUMN "body" TYPE TEXT USING "body"::TEXT',
            'ALTER TABLE "product" ALTER COLUMN "created_at" TYPE TIMESTAMPTZ USING "created_at"::TIMESTAMPTZ',
            'ALTER TABLE "user" ALTER COLUMN "password" TYPE VARCHAR(100) USING "password"::VARCHAR(100)',
            'ALTER TABLE "user" DROP COLUMN "avatar"',
            'ALTER TABLE "user" ALTER COLUMN "is_superuser" TYPE BOOL USING "is_superuser"::BOOL',
            'ALTER TABLE "user" ALTER COLUMN "last_login" TYPE TIMESTAMPTZ USING "last_login"::TIMESTAMPTZ',
            'ALTER TABLE "user" ALTER COLUMN "intro" TYPE TEXT USING "intro"::TEXT',
            'ALTER TABLE "user" ALTER COLUMN "is_active" TYPE BOOL USING "is_active"::BOOL',
            'CREATE INDEX "idx_product_name_869427" ON "product" ("name", "type_db_alias")',
            'CREATE INDEX "idx_email_email_4a1a33" ON "email" ("email")',
            'CREATE TABLE "email_user" ("email_id" INT NOT NULL REFERENCES "email" ("email_id") ON DELETE CASCADE,"user_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE)',
            'CREATE TABLE IF NOT EXISTS "newmodel" (\n    "id" SERIAL NOT NULL PRIMARY KEY,\n    "name" VARCHAR(50) NOT NULL\n);\nCOMMENT ON COLUMN "config"."user_id" IS \'User\';',
            'CREATE UNIQUE INDEX "uid_product_name_869427" ON "product" ("name", "type_db_alias")',
            'CREATE UNIQUE INDEX "uid_user_usernam_9987ab" ON "user" ("username")',

        ])
        expected_downgrade_operators = set([
            'ALTER TABLE "category" ALTER COLUMN "name" SET NOT NULL',
            'ALTER TABLE "category" ALTER COLUMN "slug" TYPE VARCHAR(200) USING "slug"::VARCHAR(200)',
            'ALTER TABLE "category" ALTER COLUMN "created_at" TYPE TIMESTAMPTZ USING "created_at"::TIMESTAMPTZ',
            'ALTER TABLE "config" ALTER COLUMN "status" SET DEFAULT 1',
            'ALTER TABLE "config" DROP COLUMN "user_id"',
            'ALTER TABLE "config" DROP CONSTRAINT "fk_config_user_17daa970"',
            'ALTER TABLE "config" RENAME TO "configs"',
            'ALTER TABLE "config" ALTER COLUMN "value" TYPE JSONB USING "value"::JSONB',
            'ALTER TABLE "email" ADD "user_id" INT NOT NULL',
            'ALTER TABLE "email" DROP COLUMN "address"',
            'ALTER TABLE "email" RENAME COLUMN "email_id" TO "id"',
            'ALTER TABLE "email" ALTER COLUMN "is_primary" TYPE BOOL USING "is_primary"::BOOL',
            'ALTER TABLE "product" ALTER COLUMN "view_num" DROP DEFAULT',
            'ALTER TABLE "product" RENAME COLUMN "pic" TO "image"',
            'ALTER TABLE "user" ADD "avatar" VARCHAR(200) NOT NULL  DEFAULT \'\'',
            'ALTER TABLE "user" ALTER COLUMN "password" TYPE VARCHAR(200) USING "password"::VARCHAR(200)',
            'ALTER TABLE "user" ALTER COLUMN "last_login" TYPE TIMESTAMPTZ USING "last_login"::TIMESTAMPTZ',
            'ALTER TABLE "user" ALTER COLUMN "is_superuser" TYPE BOOL USING "is_superuser"::BOOL',
            'ALTER TABLE "user" ALTER COLUMN "is_active" TYPE BOOL USING "is_active"::BOOL',
            'ALTER TABLE "user" ALTER COLUMN "intro" TYPE TEXT USING "intro"::TEXT',
            'ALTER TABLE "product" ALTER COLUMN "created_at" TYPE TIMESTAMPTZ USING "created_at"::TIMESTAMPTZ',
            'ALTER TABLE "product" ALTER COLUMN "is_reviewed" TYPE BOOL USING "is_reviewed"::BOOL',
            'ALTER TABLE "product" ALTER COLUMN "body" TYPE TEXT USING "body"::TEXT',
            'DROP INDEX "idx_product_name_869427"',
            'DROP INDEX "idx_email_email_4a1a33"',
            'DROP INDEX "idx_user_usernam_9987ab"',
            'DROP INDEX "uid_product_name_869427"',
            'DROP TABLE IF EXISTS "email_user"',
            'DROP TABLE IF EXISTS "newmodel"',
        ])
        assert not set(Migrate.upgrade_operators).symmetric_difference(expected_upgrade_operators)
        assert not set(Migrate.downgrade_operators).symmetric_difference(expected_downgrade_operators)

    elif isinstance(Migrate.ddl, SqliteDDL):
        assert Migrate.upgrade_operators == []
        assert Migrate.downgrade_operators == []


def test_sort_all_version_files(mocker):
    mocker.patch(
        "os.listdir",
        return_value=[
            "1_datetime_update.sql",
            "11_datetime_update.sql",
            "10_datetime_update.sql",
            "2_datetime_update.sql",
        ],
    )

    Migrate.migrate_location = "."

    assert Migrate.get_all_version_files() == [
        "1_datetime_update.sql",
        "2_datetime_update.sql",
        "10_datetime_update.sql",
        "11_datetime_update.sql",
    ]
