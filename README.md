📄 Resumify – Resuma facilmente com IA

Resumify é um aplicativo simples e intuitivo que utiliza Inteligência Artificial (IA) para gerar resumos automáticos de arquivos PDF. Com uma interface amigável, você pode abrir documentos, gerar resumos rápidos e até salvá-los em PDF ou TXT.

🚀 Funcionalidades

✅ Resumir PDFs com IA usando o modelo facebook/bart-large-cnn da Hugging Face.
✅ Salvar o resumo em arquivos .txt ou .pdf.✅ Detecção de idioma: Apenas textos em português são resumidos.✅ Interface amigável: Criada com Tkinter, fácil de usar.✅ Resumir textos longos: Suporte a múltiplas páginas no PDF.✅ Processamento assíncrono: Interface não trava durante o processamento.

📥 Requisitos

Certifique-se de ter o Python 3.8+ instalado. Para instalar as bibliotecas necessárias, execute:

pip install transformers pdfplumber reportlab langdetect

▶️ Como executar o Resumify

Clone o repositório:

git clone https://github.com/seu-usuario/resumify.git
cd resumify

Execute o aplicativo:

python app.py

🧠 Como funciona?

Abrir PDF: Você seleciona um arquivo PDF.

Gerar Resumo: O app usa IA para processar e resumir o conteúdo.

Salvar o Resumo: Escolha salvar em .txt ou .pdf.

O modelo facebook/bart-large-cnn gera um resumo detalhado, com suporte a documentos longos.

🛠️ Estrutura do Projeto

resumify/
├── app.py          # Código principal do aplicativo
└── README.md      # Documentação do projeto

📌 Melhorias Futuras

📊 Suporte a outros idiomas.

🔍 Ajuste de parâmetros do resumo (tamanho variável).

🖼️ Melhorias na interface gráfica.

📜 Licença

Este projeto está licenciado sob a licença MIT. Sinta-se à vontade para usar e modificar!

💡 Contribuições são bem-vindas! Se você tem ideias para melhorar o Resumify, envie um Pull Request.
