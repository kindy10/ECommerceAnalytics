from sqlalchemy import create_engine, inspect, text


def test_database_has_transactions_table():
    engine = create_engine("sqlite:///:memory:")

    with engine.connect() as connection:
        connection.execute(
            text(
                """
                CREATE TABLE transactions (
                    id INTEGER PRIMARY KEY,
                    invoice_no VARCHAR NOT NULL
                )
                """
            )
        )

    assert "transactions" in inspect(engine).get_table_names()