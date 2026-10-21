import ssl
import socket


def get_ssl_info(host):

    try:

        context = ssl.create_default_context()

        with socket.create_connection(
            (host, 443),
            timeout=5
        ) as sock:

            with context.wrap_socket(
                sock,
                server_hostname=host
            ) as ssock:

                cert = ssock.getpeercert()

                return {
                    "tls_version": ssock.version(),
                    "subject": cert.get(
                        "subject"
                    ),
                    "issuer": cert.get(
                        "issuer"
                    )
                }

    except Exception as e:

        return {
            "error": str(e)
        }