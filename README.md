# 📊 Dashboard de Análise de Dados do Instagram

Este projeto apresenta um dashboard interativo, construído com [Streamlit](https://streamlit.io), para visualização e análise de dados coletados de contas públicas do Instagram em diferentes países. A atualização dos dados é realizada quinzenalmente com base em scripts de coleta e análise localmente executados.

## 🔍 Funcionalidades

- **Análise de bios** das contas monitoradas
- **Nuvens de palavras** por país
- **Análise de sentimentos** das postagens
- **Top posts** por curtidas (geral e por país)
- **Visualização de bigramas e trigramas**

## 📁 Estrutura do Projeto

seu_projeto_streamlit/
├── dashboard/ # App principal do Streamlit
│ └── app.py
├── outputs/ # Dados e imagens gerados pelos scripts de análise
├── requirements.txt # Bibliotecas necessárias para rodar o app
└── README.md # Este arquivo

bash
Copiar
Editar

## 🚀 Como Executar Localmente

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Execute o app:

bash
Copiar
Editar
streamlit run dashboard/app.py
🌐 Acesse Online
O dashboard também está disponível publicamente em:

https://seu-usuario.streamlit.app

📦 Atualização dos Dados
A cada 15 dias, os scripts de análise são executados localmente e os arquivos gerados são atualizados na pasta outputs/. O Streamlit lê diretamente dessa pasta, permitindo que as visualizações estejam sempre sincronizadas com os dados mais recentes.

🛠️ Tecnologias Utilizadas
Python

Streamlit

Pandas

Matplotlib

Pillow

spaCy (nos scripts de análise)

📄 Licença
Este projeto está licenciado sob a Creative Commons.

📬 Em caso de dúvidas ou sugestões, sinta-se à vontade para abrir uma issue ou entrar em contato!
