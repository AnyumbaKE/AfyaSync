import base64
from datetime import datetime, timedelta
from io import BytesIO
from flask import (
    app,
    current_app,
    jsonify,
    render_template,
    request,
    send_file,
    Response,
)
import requests

def input_to_timestamp(input, input_format):
    """
    Converts a string input representing a date and time to a Unix timestamp.
    Time function takes a String input and a format and converts it into a
    Unix timestamp
    """
    try:
        # Attempt to parse the input string into a datetime object
        datetime_obj = datetime.strptime(input, input_format)
        # convert the datetime object to a Unix timestamp (integer)
        timestamp = int(datetime_obj.timestamp())
        return timestamp # return the unix timestamp
    except ValueError:
        # if the input string is not in the correct format, return none
        return None

def timestamp_to_str(timestamp, end_format):
    """
    Convert a Unix timestamp to a formatted date and time string
    """
    dt_obj = datetime.fromtimestamp(
        timestamp
    ) # convert the timestamp to a datetime object
    formatted_str = dt_obj.strftime(
        end_format
    ) # format the datetime object into string
    return formatted_str # return the formatted date and time string