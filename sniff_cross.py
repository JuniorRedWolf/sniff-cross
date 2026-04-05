import argparse
import requests
import sys
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def get_cnpj_data(cnpj):
    """Busca dados do CNPJ."""
    cnpj_clean = ''.join(filter(str.isdigit, cnpj))
    
    with console.status(f"[bold cyan]Buscando informações para o CNPJ {cnpj_clean}...[/bold cyan]"):
        url = f"https://brasilapi.com.br/api/cnpj/v1/{cnpj_clean}"
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 404:
                console.print("[bold red]Erro:[/bold red] CNPJ não encontrado.")
                return None
            else:
                console.print(f"[bold red]Erro na API:[/bold red] Status {response.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            console.print(f"[bold red]Erro de conexão:[/bold red] {e}")
            return None

def display_data(data):
    """Formata e exibe os dados extraídos no terminal."""
    if not data:
        return

    razao_social = data.get("razao_social", "Não informado")
    nome_fantasia = data.get("nome_fantasia", "Não informado") or "Não informado"
    cnpj = data.get("cnpj", "Não informado")
    status = data.get("descricao_situacao_cadastral", "Não informado")
    uf = data.get("uf", "N/A")
    municipio = data.get("municipio", "N/A")

    # Painel principal com os dados da empresa
    info_empresa = (
        f"[bold]Nome Fantasia:[/bold] {nome_fantasia}\n"
        f"[bold]CNPJ:[/bold] {cnpj}\n"
        f"[bold]Status:[/bold] {status}\n"
        f"[bold]Localidade:[/bold] {municipio} - {uf}"
    )
    
    console.print(Panel(info_empresa, title=f"[bold green]{razao_social}[/bold green]", expand=False))

    # Painel com o Quadro Societário
    socios = data.get("qsa", [])
    if socios:
        table = Table(title="Quadro de Sócios e Administradores (QSA)", show_header=True, header_style="bold blue")
        table.add_column("Nome", style="cyan")
        table.add_column("Qualificação", style="magenta")
        table.add_column("Faixa Etária", style="yellow")

        for socio in socios:
            nome = socio.get("nome_socio", "N/A")
            qualificacao = socio.get("descricao_qualificacao_socio", "N/A")
            idade = socio.get("faixa_etaria", "N/A")
            table.add_row(nome, qualificacao, idade)

        console.print(table)
    else:
        console.print("[yellow]Nenhum sócio registrado no quadro societário (QSA).[/yellow]")

def main():
    parser = argparse.ArgumentParser(
        description="SniffCross - Ferramenta CLI para reconhecimento de dados e QSA corporativo."
    )
    parser.add_argument(
        "-c", "--cnpj", 
        required=True, 
        help="O CNPJ alvo para investigação (com ou sem pontuação)."
    )
    
    args = parser.parse_args()

    dados_empresa = get_cnpj_data(args.cnpj)
    display_data(dados_empresa)

if __name__ == "__main__":
    main()