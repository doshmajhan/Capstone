"""
This module handles exceptions encountered by the application.
"""
from functools import wraps
from flask import jsonify, Response
from mongoengine.errors import DoesNotExist, NotUniqueError, ValidationError
from terraform import TerraformError

class InvalidConfiguration(Exception):
    """
    Raised when the given configuration is invalid.
    """
    pass

class BadRequest(Exception):
    """
    Raised when the data inside of a request was not readable.
    """
    pass

def handle_exceptions(func):
    """
    This function can be used as a decorator to wrap functions.
    Wrapped functions will be surrounded in a try / except block that
    includes necessary error handling, including logging and
    returning error responses.
    """
    @wraps(func)
    def wrapper(*args, **kwargs): #pylint: disable=too-many-return-statements,too-many-branches
        """
        This uses the func tools library to wrap a function.
        """
        try:
            retval = func(*args, **kwargs)
            return retval

        except InvalidConfiguration as exception:
            resp = jsonify({
                'error': True,
                'status': 400,
                'error_type': 'invalid-configuration',
                'description': str(exception),
            })
            resp.status_code = 400
            return resp

        except TerraformError as exception:
            resp = jsonify({
                'error': True,
                'status': 500,
                'error_type': 'build-error',
                'description': str(exception),
            })
            resp.status_code = 500
            return resp

        except ValidationError:
            resp = jsonify({
                'error': True,
                'status': 400,
                'error_type': 'validation-error',
                'description': 'Invalid parameter type.',
            })
            resp.status_code = 400
            return resp

        except DoesNotExist:
            resp = jsonify({
                'error': True,
                'status': 400,
                'error_type': 'does-not-exist',
                'description': 'Role does not exist',
            })
            resp.status_code = 400
            return resp

        except NotUniqueError:
            resp = jsonify({
                'error': True,
                'status': 400,
                'error_type': 'not-unique',
                'description': 'Role already exists in the database',
            })
            resp.status_code = 400
            return resp
        except OSError as e:
            resp = jsonify({
                'error': True,
                'status': 400,
                'error_type': 'invalid-role',
                'description': 'One or more specified roles were not found.'
            })
            print(e.filename)
            resp.status_code = 400
            return resp
        except KeyError:
            resp = jsonify({
                'error': True,
                'status': 400,
                'error_type': 'missing-parameter',
                'description': 'Missing required parameter',
            })
            resp.status_code = 400
            return resp

    return wrapper
