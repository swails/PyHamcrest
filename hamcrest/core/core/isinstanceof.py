from hamcrest.core.base_matcher import BaseMatcher

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"

import types

class IsInstanceOf(BaseMatcher):

    def __init__(self, expected_type):
        if not self._valid_type(expected_type):
            raise TypeError('IsInstanceOf requires type')
        self.expected_type = expected_type

    def _matches(self, item):
        return isinstance(item, self.expected_type)

    def _valid_type(self, expected_type):
        if isinstance(expected_type, type):
            return True

        if type(expected_type) == types.ClassType:
            return True

        return False

    def describe_to(self, description):
        description.append_text('an instance of ')              \
                    .append_text(self.expected_type.__name__)


def instance_of(atype):
    """Matches if object is an instance of, or inherits from, a given type.

    :param atype: The type to compare against as the expected type.

    This matcher checks whether the evaluated object is an instance of
    ``atype`` or an instance of any class that inherits from ``atype``.

    Example::

        instance_of(str)

    """
    return IsInstanceOf(atype)
