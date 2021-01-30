import re
from dynamic_constants import DynamicConstants


class HeaderDecode(object):
    @classmethod
    def _get_header_regex(cls, header_format: str):
        componants = re.findall(r"\(.[^)]*\)", header_format)

        expression = header_format

        for idx, match in enumerate(componants, 1):
            param = re.match(r"\((.[^)]*)\)", match).group(1)
            expression = expression.replace(match, "(?P<{param}>.[^|]*){close}".format(param=param, close="\\" if idx != len(componants) else ""))

        return expression

    def set_header_regex(self, header_format: str):
        DynamicConstants.HEADER_REGEX = self._get_header_regex(header_format)

        return DynamicConstants.HEADER_REGEX
