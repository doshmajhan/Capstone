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
            return jsonify({
                'error': True,
                'status': 400,
                'error_type': 'invalid-configuration',
                'description': str(exception),
            })

        except TerraformError as exception:
            return jsonify({
                'error': True,
                'status': 500,
                'error_type': 'build-error',
                'description': str(exception),
            })

        except ValidationError:
            return jsonify({
                'error': True,
                'status': 400,
                'error_type': 'validation-error',
                'description': 'Invalid parameter type.',
            })

        except DoesNotExist:
            return jsonify({
                'error': True,
                'status': 400,
                'error_type': 'does-not-exist',
                'description': 'Role does not exist',
            })

        except NotUniqueError:
            return jsonify({
                'error': True,
                'status': 400,
                'error_type': 'not-unique',
                'description': 'Role already exists in the database',
            })
        except KeyError:
            return jsonify({
                'error': True,
                'status': 400,
                'error_type': 'missing-parameter',
                'description': 'Missing required parameter',
            })

    if isinstance(wrapper, Response):
        wrapper.status_code = wrapper.json.get('status', 500)

    return wrapper
