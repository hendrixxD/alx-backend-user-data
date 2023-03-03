#!/usr/bin/env python3
"""
personal data
"""

import re
import os
from typing import List
import logging
import mysql.connector


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'creditcard')

def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """
    Replaces specified fields in a log message with a redaction string.

    Args:
        fields (List[str]): List of fields to redact.
        redaction (str): String to replace fields with.
        message (str): Log message to be redacted.
        separator (str): Separator used in the log message.

    Returns:
        str: Redacted log message.
    """
    for field in fields:
        pattern = r'(?<=' + field + '=)[^' + separator + ']*'
        message = re.sub(pattern, redaction, message)
    return message

class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Init
        """
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """ """"
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def get_logger() -> logging.Logger:
    """ Implementing a logger.
    """

    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    return logger

# PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')

def get_db() -> mysql.connector.connection.MySQLConnection::
    """
    Return a connector to the holberton database
    """
    username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    database = os.getenv('PERSONAL_DATA_DB_NAME')

    cnx = mysql.connector.connect(user=username, password=password,
                                host=host, database=database)
    return cnx

def main() -> None:
    """
    Retrieve all rows from the users table, obfuscate sensitive information,
    and display the filtered data in the log output
    """
    cnx = get_db()
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        row_data = dict(zip(cursor.column_names, row))
        filtered_data = ['{}={}'.format(k, '***' if k in PII_FIELDS else v)
                        for k, v in row_data.items()]
        log_message = '; '.join(filtered_data)
        print('[HOLBERTON] user_data INFO 2019-11-19 18:37:59,596: {}'.format(log_message))
        print('Filtered fields:\n{}'.format('\n'.join(PII_FIELDS)))

if __name__ == '__main__':
    main()
