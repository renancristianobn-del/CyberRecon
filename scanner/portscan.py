import socket
from concurrent.futures import ThreadPoolExecutor, as_completed


def scan_port(host, port):

    try:
        with socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        ) as sock:

            sock.settimeout(3)

            result = sock.connect_ex(
                (host, port)
            )

            if result == 0:
                return port

    except Exception:
        pass

    return None


def run_scan(host, start_port, end_port):

    open_ports = []

    workers = 50

    with ThreadPoolExecutor(
        max_workers=workers
    ) as executor:

        futures = {
            executor.submit(
                scan_port,
                host,
                port
            ): port
            for port in range(
                start_port,
                end_port + 1
            )
        }

        for future in as_completed(futures):

            result = future.result()

            if result:
                open_ports.append(result)

    return sorted(open_ports)