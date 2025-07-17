# 🧠 ExamOCR

Este projeto tem como objetivo **extrair e estruturar automaticamente questões de provas em PDF**, especialmente documentos com **layout em duas colunas**, utilizando **OCR (Reconhecimento Óptico de Caracteres)**.

---


## 🚀 Funcionalidades

- 📄 Leitura de PDFs com layout de duas colunas.
- 🤖 OCR usando Tesseract (suporte a português e inglês).
- 🧠 Extração estruturada de questões, enunciado, texto de apoio e alternativas.
- 💾 Exportação das questões em formato JSON.

---
## 🔗 Links

Google Colab: https://colab.research.google.com/drive/12Rce8t_LEC8ugomN61puebgi9kVy-Wd-?usp=sharing

Frontend: https://github.com/Leopinheiro132/QuestionBank

Sistema MetaConquista: https://metaconquista.vercel.app/

## 📂 Estrutura do Projeto

```
pdf-question-parser/
├── main.py                     # Script principal de execução
├── config.py                   # Caminhos e configurações globais
├── requirements.txt            # Dependências do projeto
├── README.md                   # Documentação do projeto
├── output/                     # Arquivos de saída (JSON)
│   └── questoes_eear_corrigido.json  # Resultado da extração da prova
└── utils/
    ├── extractor.py            # Função para extrair texto do PDF
    ├── ocr.py                  # Função de OCR das colunas
    └── parser.py               # Função para analisar e estruturar as questões
```

> A pasta `output/` contém o **arquivo JSON com o resultado final da extração das questões da prova**, estruturado com:
> - Número da questão
> - Enunciado
> - Texto de apoio (se houver)
> - Alternativas

---

## 🧪 Pré-requisitos

Certifique-se de ter o **Tesseract OCR** instalado:

```bash
sudo apt update
sudo apt install tesseract-ocr
```

---

## 📦 Instalação das dependências

```bash
pip install -r requirements.txt
```

---

## ⚙️ Como usar

1. Coloque seu arquivo PDF no caminho configurado em `config.py` (`PDF_PATH`).
2. Execute o script principal:

```bash
python main.py
```

3. O arquivo `questoes_eear_corrigido.json` será salvo na pasta `output/`.

---

## 📄 Exemplo de Saída

```json
{
  "numero_questao": 1,
  "enunciado": "Qual é a função principal do oxigênio na respiração celular?",
  "texto_apoio": "“O oxigênio é fundamental para o processo de obtenção de energia nas células...”",
  "alternativas": {
    "a": "Fornecer glicose.",
    "b": "Atuar na digestão.",
    "c": "Aceitar elétrons na cadeia respiratória.",
    "d": "Formar o ATP diretamente."
  }
}
```

---

## 🧠 Tecnologias usadas

- [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/en/latest/)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [pytesseract](https://pypi.org/project/pytesseract/)
- [Pillow (PIL)](https://pillow.readthedocs.io/)

---

## 📌 Observações

- O OCR pode apresentar erros em PDFs de baixa qualidade.
- Arquivos com formatação incomum podem exigir ajustes na `regex` do parser.
- O layout do PDF precisa seguir uma lógica de colunas para melhor extração.

---

## 📜 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se livre para abrir *issues*, propor *pull requests* ou sugerir melhorias.

---
