import re
from ..dynamic_constants import DynamicConstants


class HeaderDecode(object):
    @staticmethod
    def _get_header_regex(header_format: str) -> str:
        """
            This method uses the header format provided by the user to generate a regex pattern. This pattern is then
            later used to extract the relevant metadata from the FASTA headers.

            :param header_format: The format of the header as provided by the user at the instantiation of the Hunana
            class.

            :type header_format: str

            :return: Returns a regex pattern for the FASTA headers to extract metadata.
        """

        components = re.findall(r"\(.[^)]*\)", header_format)

        expression = header_format

        for idx, match in enumerate(components, 1):
            param = re.match(r"\((.[^)]*)\)", match).group(1)
            expression = expression.replace(match, "(?P<{param}>.[^|]*){close}".format(
                param=param, close="\\" if idx != len(components) else ""))

        return expression

    @staticmethod
    def set_header_regex(header_format: str):
        """
            Sets the regex expression for the FASTA headers that is later used to extract the relevant metadata.
            The return value of this is only for error-handling and does not serve any other purpose.

            :param header_format: The format of the header as provided by the user at the instantiation of the Hunana
            class.

            :type header_format: str

            :return: The generated regex pattern for the FASTA headers.
        """

        DynamicConstants.HEADER_REGEX = HeaderDecode._get_header_regex(header_format)

        return DynamicConstants.HEADER_REGEX
