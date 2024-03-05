import sqlite3

import config


def execute(sql: str, params: tuple = ()) -> sqlite3.Cursor:
    return _get_cursor().execute(sql, params)


def executemany(sql: str, params: list[tuple]) -> sqlite3.Cursor:
    return _get_cursor().executemany(sql, params)


def fetchall(sql: str) -> list:
    return execute(sql).fetchall()


def commit() -> None:
    _get_connection().commit()


def close_conection() -> None:
    _get_connection().close


def _get_connection() -> sqlite3.Connection:
    if not getattr(_get_connection, "con", None):
        con = sqlite3.connect(config.SQLITE_DB_FILE)
        _get_connection.con = con

    return _get_connection.con


def _get_cursor() -> sqlite3.Cursor:
    return _get_connection().cursor()
