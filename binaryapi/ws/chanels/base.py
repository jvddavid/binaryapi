"""Module for base Binary base websocket chanel."""


class Base(object):
    """Class for base Binary websocket chanel."""

    # pylint: disable=too-few-public-methods

    def __init__(self, api):
        """
        :param api: The instance of :class:`BinaryAPI
            <iqoptionapi.api.BinaryAPI>`.
        """
        self.api = api

    def send_websocket_request(self, name, msg, passthrough=None, request_id=None):
        """Send request to Binary server websocket.

        :param passthrough: object
        :param str request_id:
        :param str name: The websocket chanel name.
        :param dict msg: The websocket chanel msg.

        :returns: The instance of :class:`requests.Response`.
        """
        return self.api.send_websocket_request(name, msg, passthrough=passthrough, request_id=request_id)
