"""
This module handles exceptions encountered by the application.
"""
from functools import wraps
from mongoengine.errors import DoesNotExist, NotUniqueError, ValidationError

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
            return {
                'error': True,
                'error_type': 'invalid-configuration',
                'description': str(exception),
            }

        except ValidationError:
            return {
                'error': True,
                'error_type': 'validation-error',
                'description': 'Invalid parameter type.',
            }

        except DoesNotExist:
            return {
                'error': True,
                'error_type': 'does-not-exist',
                'description': 'Role does not exist',
            }

        except NotUniqueError:
            return {
                'error': True,
                'error_type': 'not-unique',
                'description': 'Role already exists in the database',
            }
        except KeyError:
            return {
                'error': True,
                'error_type': 'missing-parameter',
                'description': 'Missing required parameter',
            }

    return wrapper
