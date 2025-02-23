import tkinter as tk
from tkinter import filedialog, messagebox
import pdfplumber
from transformers import pipeline
from langdetect import detect
import threading

# Carrega o modelo de sumarização apenas uma vez para melhorar o desempenho
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Função para extrair texto do PDF usando pdfplumber
def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:  # Verifica se há texto na página
                text += page_text + " "

    if not text.strip():  # Se o texto extraído for vazio, retorna uma mensagem de erro
        raise ValueError("O PDF não contém texto legível.")

    return text.strip()

# Função para gerar um resumo usando IA (modelo de resumo abstrativo)
def summarize_text(text, min_words=200, max_words=500):
    max_input_length = 1024  # Limite do modelo BART

    try:
        lang = detect(text)
        if lang != 'pt':
            return "O texto precisa estar em português para ser resumido."
    except:
        return "Não foi possível detectar o idioma."

    if len(text.split()) < 50:  # Verifica se o texto tem pelo menos 50 palavras
        return "O texto é muito curto para gerar um resumo significativo."

    if len(text) > max_input_length:
        text = text[:max_input_length]  # Corta o texto no limite

    summary = summarizer(text, max_length=300, min_length=50, do_sample=False)  
    summarized_text = summary[0]['summary_text']

    words = summarized_text.split()
    if len(words) > max_words:
        summarized_text = " ".join(words[:max_words])

    return summarized_text

from tkinter import filedialog, messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import textwrap

def save_summary(summary):
    save_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Arquivo de Texto", "*.txt"), ("Arquivo PDF", "*.pdf")]
    )

    if save_path:
        try:
            # Salvar como TXT
            if save_path.endswith(".txt"):
                with open(save_path, "w", encoding="utf-8") as file:
                    file.write("Resumo Gerado com IA:\n\n")
                    file.write(summary)

            # Salvar como PDF
            elif save_path.endswith(".pdf"):
                pdf = canvas.Canvas(save_path, pagesize=letter)

                # Configurações de layout
                title = "Resumo Gerado com IA"
                pdf.setFont("Helvetica-Bold", 14)  # Fonte maior para o título
                pdf.drawString(72, 750, title)

                pdf.setFont("Helvetica", 10)  # Fonte menor para o corpo do texto

                # Ajusta a posição inicial para o conteúdo
                y = 730
                max_width = 100  # Número máximo de caracteres por linha (ajustável)
                line_height = 14

                # Quebrar o texto em múltiplas linhas
                lines = summary.splitlines()  # Mantém as quebras de parágrafo
                for line in lines:
                    wrapped_lines = textwrap.wrap(line, max_width)

                    for wrapped_line in wrapped_lines:
                        pdf.drawString(72, y, wrapped_line)
                        y -= line_height

                        # Adiciona nova página se necessário
                        if y < 50:
                            pdf.showPage()
                            pdf.setFont("Helvetica-Bold", 14)
                            pdf.drawString(72, 750, "Continuação do Resumo:")
                            pdf.setFont("Helvetica", 10)
                            y = 730

                pdf.save()

            messagebox.showinfo("Sucesso", f"Resumo salvo com sucesso em: {save_path}")

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar o arquivo: {e}")

# Função para abrir e processar o PDF
def open_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        def process():
            try:
                progress_label.config(text="Processando...")
                document_text = extract_text_from_pdf(file_path)
                summary = summarize_text(document_text)
                response_label.config(text=f"Resumo:\n{summary}")

                # Botão para salvar o resumo
                save_button = tk.Button(root, text="Salvar Resumo", command=lambda: save_summary(summary), bg="#3498DB", fg="white", font=("Helvetica", 12))
                save_button.pack(pady=10)

            except ValueError as ve:
                messagebox.showerror("Erro", str(ve))
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao processar o PDF: {str(e)}")
            finally:
                progress_label.config(text="")

        threading.Thread(target=process).start()

# Interface gráfica
root = tk.Tk()
root.title("Resumidor de PDFs com IA")
root.geometry("700x600")
root.configure(bg="#2C3E50")

header = tk.Label(root, text="Resumidor de PDFs com IA", font=("Helvetica", 20, "bold"), bg="#34495E", fg="white", pady=20)
header.pack(fill="x")

button = tk.Button(root, text="Abrir PDF e Gerar Resumo", command=open_pdf, font=("Helvetica", 14), bg="#1ABC9C", fg="white", padx=20, pady=10, relief="flat")
button.pack(pady=20)

progress_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#2C3E50", fg="white")
progress_label.pack(pady=10)

response_frame = tk.Frame(root, bg="#2C3E50")
response_frame.pack(padx=20, pady=20, fill="both", expand=True)

response_label = tk.Label(response_frame, text="", wraplength=650, justify="left", font=("Helvetica", 12), bg="#ECF0F1", fg="#2C3E50", padx=10, pady=10, relief="sunken")
response_label.pack(fill="both", expand=True)

footer = tk.Label(root, text="Desenvolvido com IA - BART Model", font=("Helvetica", 10), bg="#34495E", fg="white", pady=10)
footer.pack(fill="x", side="bottom")

root.mainloop()










