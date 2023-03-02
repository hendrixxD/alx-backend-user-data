#!/usr/bin/env python3
"""
personal data
"""

#import re
#from typing import List

#def filter_datum(fields: List[str], redaction: str, message: str,
#                 separator: str) -> str:
#    """ Replacing """
#    for f in fields:
#        message = re.sub(rf"{f}=(.*?)\{separator}",
#                         f'{f}={redaction}{separator}', message)
#    return message


import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
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
