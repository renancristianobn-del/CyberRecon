import argparse
import datetime
import json
import os
import socket
import time

from rich.console import Console
from rich.table import Table

from scanner.portscan import run_scan
from scanner.banner import grab_banner
from scanner.sslscan import get_ssl_info
from scanner.dnslookup import get_dns_records

console = Console()

COMMON_SERVICES = {
    21: "FTP",
    22: "SSH",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    5432: "PostgreSQL",
    6379: "Redis",
    8080: "HTTP-ALT"
}


def show_banner():

    console.print(
        """
[bold red]
████████╗ ██████╗ ██╗  ██╗██╗   ██╗ ██████╗  ██████╗
╚══██╔══╝██╔═══██╗██║ ██╔╝╚██╗ ██╔╝██╔═══██╗██╔═══██╗
   ██║   ██║   ██║█████╔╝  ╚████╔╝ ██║   ██║██║   ██║
   ██║   ██║   ██║██╔═██╗   ╚██╔╝  ██║   ██║██║   ██║
   ██║   ╚██████╔╝██║  ██╗   ██║   ╚██████╔╝╚██████╔╝
   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚═════╝

              CyberRecon v1.1
              Made by Tokyoo
[/bold red]
"""
    )


def main():

    start_time = time.time()

    show_banner()

    parser = argparse.ArgumentParser(
        description="CyberRecon"
    )

    parser.add_argument(
        "host",
        help="Host alvo"
    )

    parser.add_argument(
        "--ports",
        default="1-1024",
        help="Exemplo: 1-1024"
    )

    args = parser.parse_args()

    host = args.host

    try:

        ip = socket.gethostbyname(
            host
        )

        console.print(
            f"[green]IP:[/green] {ip}"
        )

    except Exception as e:

        console.print(
            f"[red]Erro DNS:[/red] {e}"
        )

        return

    start_port, end_port = map(
        int,
        args.ports.split("-")
    )

    console.print(
        f"\n[cyan]Iniciando reconhecimento em:[/cyan] {host}"
    )

    console.print(
        "\n[yellow]Escaneando portas...[/yellow]"
    )

    open_ports = run_scan(
        host,
        start_port,
        end_port
    )

    dns_info = get_dns_records(
        host
    )

    ssl_info = get_ssl_info(
        host
    )

    table = Table(
        title=f"Portas Abertas - {host}"
    )

    table.add_column(
        "Porta",
        style="green"
    )

    table.add_column(
        "Serviço",
        style="cyan"
    )

    table.add_column(
        "Banner",
        style="white"
    )

    ports_report = []

    for port in open_ports:

        banner = grab_banner(
            host,
            port
        )

        service = COMMON_SERVICES.get(
            port,
            "Unknown"
        )

        table.add_row(
            str(port),
            service,
            banner[:80] if banner else "-"
        )

        ports_report.append({
            "port": port,
            "service": service,
            "banner": banner
        })

    console.print(table)

    console.print(
        "\n[bold green]DNS Records[/bold green]"
    )

    console.print(
        dns_info
    )

    console.print(
        "\n[bold green]SSL/TLS[/bold green]"
    )

    console.print(
        ssl_info
    )

    elapsed = round(
        time.time() - start_time,
        2
    )

    os.makedirs(
        "reports",
        exist_ok=True
    )

    report = {
        "tool": "CyberRecon",
        "version": "1.1",
        "author": "Tokyoo",
        "host": host,
        "ip": ip,
        "scan_date": str(datetime.datetime.now()),
        "scan_duration_seconds": elapsed,
        "open_ports": open_ports,
        "dns": dns_info,
        "ssl": ssl_info,
        "ports": ports_report
    }

    report_file = (
        f"reports/{host}_report.json"
    )

    with open(
        report_file,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            report,
            f,
            indent=4,
            ensure_ascii=False
        )

    console.print(
        f"\n[yellow]Relatório salvo:[/yellow] {report_file}"
    )

    console.print(
        f"\n[green]Tempo total:[/green] {elapsed}s"
    )

    console.print(
        "\n[bold red]CyberRecon - Made by Tokyoo[/bold red]"
    )


if __name__ == "__main__":
    main()