import socket


def grab_banner(host, port):

    try:

        with socket.socket() as s:

            s.settimeout(3)

            s.connect(
                (host, port)
            )

            if port in [80, 443]:

                s.send(
                    b"HEAD / HTTP/1.0\r\n\r\n"
                )

            response = (
                s.recv(1024)
                .decode(
                    "utf-8",
                    errors="ignore"
                )
            )

            response = (
                response
                .splitlines()[0]
                .strip()
            )

            return response

    except Exception:
        return "-"