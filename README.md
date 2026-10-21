
CyberRecon

Ferramenta de Reconhecimento e Enumeração de Rede desenvolvida em Python.

CyberRecon foi criado para auxiliar na identificação de portas abertas, serviços expostos, informações DNS e configurações SSL/TLS de um host.

⚠️ Use apenas em sistemas próprios ou mediante autorização explícita.

Autor
Desenvolvido por Tokyoo

GitHub:

https://github.com/renancristianobn-del
Recursos
✅ Scan de Portas TCP

✅ Detecção de Serviços

✅ Banner Grabbing

✅ Enumeração DNS

✅ Inspeção SSL/TLS

✅ Exportação de Relatórios JSON

✅ Terminal Colorido com Rich

✅ Multithreading

Estrutura do Projeto
cyberrecon/
│
├── main.py
├── scanner/
│   ├── portscan.py
│   ├── banner.py
│   ├── sslscan.py
│   └── dnslookup.py
│
├── reports/
│
├── requirements.txt
├── README.md
└── LICENSE
Requisitos
Python 3.10 ou superior

Verifique sua versão:

python --version
ou

python3 --version
Instalação
Clone o repositório:

git clone https://github.com/renancristianobn-del/cyberrecon.git
Entre na pasta:

cd cyberrecon
Instale as dependências:

pip install -r requirements.txt
Como Executar
Sintaxe básica:

python main.py dominio.com
Exemplo:

python main.py google.com
Escanear um Intervalo de Portas
Escanear portas de 1 até 5000:

python main.py google.com --ports 1-5000
Escanear apenas as portas mais comuns:

python main.py google.com --ports 1-1024
Exemplo de Saída
Iniciando scan em google.com

┏━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┓
┃ Porta  ┃ Banner              ┃
┡━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━┩
│ 80     │ nginx              │
│ 443    │ HTTP/1.1 200 OK    │
└────────┴────────────────────┘

DNS:
{
  'A': ['142.250.x.x']
}

SSL/TLS:
{
  'tls_version': 'TLSv1.3'
}

Relatório salvo:
reports/google_report.json
Relatórios
Todos os relatórios serão armazenados automaticamente na pasta:

reports/
Exemplo:

reports/google_report.json
reports/github_report.json
Formato do Relatório
{
  "host": "github.com",
  "ports": [
    {
      "port": 443,
      "banner": "HTTP/1.1 200 OK"
    }
  ]
}
Dependências
O projeto utiliza:

rich
dnspython
requests
Instalação manual:

pip install rich dnspython requests
Roadmap
Recursos planejados para futuras versões:

Exportação CSV
Exportação HTML
WHOIS Lookup
GeoIP Lookup
Integração com Nmap
Docker Support
API REST
Painel Web Flask
GitHub Actions
Licença
MIT License

Disclaimer
Este software foi desenvolvido para fins educacionais e auditorias autorizadas.

O autor não se responsabiliza por qualquer uso indevido da ferramenta.

Assinatura
████████╗ ██████╗ ██╗  ██╗██╗   ██╗ ██████╗
╚══██╔══╝██╔═══██╗██║ ██╔╝╚██╗ ██╔╝██╔═══██╗
   ██║   ██║   ██║█████╔╝  ╚████╔╝ ██║   ██║
   ██║   ██║   ██║██╔═██╗   ╚██╔╝  ██║   ██║
   ██║   ╚██████╔╝██║  ██╗   ██║   ╚██████╔╝
   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝

      CyberRecon - Made by Tokyoo