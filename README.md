# 🧠 PDF Question Parser (ExamOCR)

Este projeto tem como objetivo **extrair e estruturar automaticamente questões de provas em PDF**, especialmente documentos com **layout em duas colunas**, utilizando **OCR (Reconhecimento Óptico de Caracteres)**.

---

## 🚀 Funcionalidades

- 📄 Leitura de PDFs com layout de duas colunas.
- 🤖 OCR usando Tesseract (suporte a português e inglês).
- 🧠 Extração estruturada de questões, enunciado, texto de apoio e alternativas.
- 💾 Exportação das questões em formato JSON.

---

## 📂 Estrutura do Projeto

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

A pasta output/ contém o arquivo JSON com o resultado final da extração das questões da prova, estruturado com número da questão, enunciado, texto de apoio (se houver) e alternativas.
