# SniffCross 🔎

Uma ferramenta CLI leve e rápida para reconhecimento de dados corporativos e extração do Quadro de Sócios e Administradores (QSA).

#### *Esse projeto faz parte das iniciativas de código aberto do **Projeto Sniff**.*

## 🚀 Funcionalidades

* **Busca direta via CNPJ:** Aceita formatos com ou sem pontuação.
* **Extração de QSA:** Identifica sócios, administradores e suas qualificações.
* **Visualização Limpa:** Saída formatada em tabelas e painéis diretamente no terminal para fácil leitura.
* **Integração:** Consome dados públicos e gratuitos da Brasil API.

## ⚙️ Instalação

Certifique-se de ter o Python 3 instalado. Clone o repositório e instale as dependências:

git clone https://github.com/JuniorRedWolf/sniff-cross.git
cd sniff-cross
pip install -r requirements.txt

## 🛠️ Como Usar

Execute o script passando o CNPJ alvo com o argumento -c ou --cnpj:

python sniff_cross.py -c 00000000000000

*(O script limpará automaticamente pontos e traços, se houver).*

## ⚠️ Aviso Legal

O SniffCross utiliza exclusivamente APIs públicas que retornam dados abertos. Esta ferramenta foi criada para fins educacionais e para auxiliar profissionais de cibersegurança e investigadores digitais em análises legítimas. Utilize com responsabilidade.

---
*Desenvolvido pela equipe Wolf Security / Projeto Sniff.*