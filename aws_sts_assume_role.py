#!/usr/bin/env python3

import json
import os
import sys
from time import sleep

import select


def error(message):
    """
    Errors must create non-zero status codes and human-readable, ideally one-line, messages on stderr.
    """
    print(message, file=sys.stderr)
    sys.exit(1)


def validate(data):
    """
    Query data and result data must have keys who's values are strings.
    """
    if not isinstance(data, dict):
        error('Data must be a dictionary.')
    for value in data.values():
        if not isinstance(value, str):
            error('Values must be strings.')


def assume_role():
    if not select.select([sys.stdin, ], [], [], 0.0)[0]:
        error("No stdin data.")

    query = json.loads(sys.stdin.read())

    if not isinstance(query, dict):
        error("Data must be a dictionary.")

    validate(query)

    if "role_arn" not in query:
        error("Data parameter must define 'role_arn'.")

    if "wait" in query:
        sleep(int(query["wait"]))

    response = {}
    try:
        response_str = os.popen(
            "aws sts assume-role --role-arn {} --role-session-name TFSession --query \"Credentials.[AccessKeyId,SecretAccessKey,SessionToken]\" --output json".format(
                query["role_arn"]))
        response = json.load(response_str)
    except Exception as e:
        error(f"Error from AWS CLI: {e}")

    sys.stdout.write(json.dumps({
        "access_key": response[0],
        "secret_key": response[1],
        "token": response[2],
    }))


if __name__ == '__main__':
    assume_role()   