import logging
import os


class SystemNotificationHandler(logging.Handler):
    def emit(self, record):
        """
        Emit a record.

        Pickles the record and writes it to the socket in binary format.
        If there is an error with the socket, silently drop the packet.
        If there was a problem with the socket, re-establishes the
        socket.
        """
        try:
            msg = self.format(record)
            os.system("pkill notify-osd")
            os.system('notify-send "Log" "{}"'.format(msg))
        except Exception:
            self.handleError(record)
