import re
from ..dynamic_constants import DynamicConstants


class HeaderDecode(object):
    @staticmethod
    def _get_header_regex(header_format: str):
        componants = re.findall(r"\(.[^)]*\)", header_format)

        expression = header_format

        for idx, match in enumerate(componants, 1):
            param = re.match(r"\((.[^)]*)\)", match).group(1)
            expression = expression.replace(match, "(?P<{param}>.[^|]*){close}".format(param=param, close="\\" if idx != len(componants) else ""))

        return expression

    @staticmethod
    def set_header_regex(header_format: str):
        DynamicConstants.HEADER_REGEX = HeaderDecode._get_header_regex(header_format)

        return DynamicConstants.HEADER_REGEX
