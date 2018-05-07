import socket


def is_connected():
    """
    Quick check of internet connection.
    Return True if connected, return False if not connected.
    """
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False
