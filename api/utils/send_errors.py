from flask import make_response


def send_internal_error(error):
    print(" * Internal server error = {}".format(error))
    return make_response(
        "Internal error. Please contact with service",
        500
    )


def send_invalid_error(error):
    print(" * Invalid request = {}".format(error))
    return make_response(
        "Invalid request = {}".format(error),
        300
    )
