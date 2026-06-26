from database.connector import get_engine
from sqlalchemy import inspect


def get_schema():

    schema_text = ""
    engine = get_engine()

    inspector = inspect(engine)

    for table in inspector.get_table_names():
        schema_text+= f"\nTable: {table}\n"

        schema_text += "Columns:\n"

        for column in inspector.get_columns(table):
            schema_text+= (
                f"- {column['name']} "
                f"({column['type']})\n"
            )

        foreign_keys = inspector.get_foreign_keys(table)

        if foreign_keys:

            schema_text += "\nRelationships:\n"

            for fk in foreign_keys:

                schema_text += (
                    f"- {table}."
                    f"{fk['constrained_columns'][0]}"
                    f" ->"
                    f"{fk['referred_table']}."
                    f"{fk['referred_columns']}\n"
                )

        schema_text += "\n"

    return schema_text

