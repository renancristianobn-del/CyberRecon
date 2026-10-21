import socket
import dns.resolver


def get_dns_records(domain):

    records = {
        "A": [],
        "MX": [],
        "NS": []
    }

    try:
        records["A"] = socket.gethostbyname_ex(
            domain
        )[2]
    except Exception:
        pass

    try:
        mx_records = dns.resolver.resolve(
            domain,
            "MX"
        )

        records["MX"] = [
            str(r.exchange)
            for r in mx_records
        ]
    except Exception:
        pass

    try:
        ns_records = dns.resolver.resolve(
            domain,
            "NS"
        )

        records["NS"] = [
            str(r)
            for r in ns_records
        ]
    except Exception:
        pass

    return records
