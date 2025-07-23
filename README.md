# 🧠 ExamOCR - Extração Automática de Questões de Provas em PDF

# 1. Introdução
O objetivo deste trabalho foi automatizar a extração de questões de provas em formato PDF para alimentar o sistema MetaConquista, que é um sistema de aprendizado baseado em questões de simulados de concurso. O ExamOCR foi desenvolvido para realizar essa tarefa de forma eficiente, utilizando OCR para converter texto de provas digitalizadas em um formato estruturado JSON que pode ser integrado diretamente ao banco de dados do MetaConquista.

---

# 2. Desenvolvimento / Técnicas Utilizadas

🚀 O projeto foi desenvolvido utilizando as seguintes abordagens e tecnologias:


- 📄 Leitura de PDFs com Layout em Duas Colunas: Suporta documentos com múltiplas colunas, utilizando técnicas de processamento de imagem para separar as colunas antes de aplicar o OCR.

- 🤖 OCR usando Tesseract: Implementa o Tesseract OCR para converter texto de imagens em conteúdo legível, com suporte para português e inglês.

- 🧠 Extração Estruturada de Questões: Extrai e estrutura as questões, enunciado, texto de apoio e alternativas de maneira automatizada e precisa.

- 💾 Exportação em Formato JSON: A saída é um arquivo JSON contendo as questões extraídas, que pode ser facilmente manipulado e analisado.

- Processamento de PDFs: Usamos a biblioteca PyMuPDF para extrair as imagens de cada página do PDF, considerando o layout de duas colunas.


## 2.1 MetaConquista

<img width="1918" height="953" alt="metaconquista" src="https://github.com/user-attachments/assets/78d3f27d-61d4-4f64-b371-9e2685bc51c7" />


## 🔗 Links
Sistema MetaConquista: 
```
https://metaconquista.vercel.app/
```

Google Colab:
```
https://colab.research.google.com/drive/12Rce8t_LEC8ugomN61puebgi9kVy-Wd-?usp=sharing
```

Github do Frontend: 
```
https://github.com/Leopinheiro132/QuestionBank
```

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

Obs: O código-fonte se encontra de forma fatorada no Github. Contudo, a sua execução está no Google Colab.

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

## 📄 Exemplo de Saída JSON

```json
{
  "pagina": 6,
  "coluna": "esquerda",
  "numero": 1,
  "enunciado": "Qual é a função principal do oxigênio na respiração celular?",
  "alternativas": {
    "a": "Fornecer glicose.",
    "b": "Atuar na digestão.",
    "c": "Aceitar elétrons na cadeia respiratória.",
    "d": "Formar o ATP diretamente."
  }
}
```

---

# 3. Resultados

Após passar o PDF da prova pelo PyMuPDF e convertê-lo em imagem, utilizamos o Pillow para processar as imagens, dividindo-as em duas partes: barra da esquerda e barra da direita. Em seguida, ambas as partes foram analisadas com o Tesseract para extração das perguntas, alternativas, etc., gerando o seguinte resultado:

Parte do json real de output:
```json
    {
        "pagina": 10,
        "coluna": "direita",
        "numero": 54,
        "enunciado": "Seja f(x) = ax + b uma fungao polinomial do 1° grau, decrescente, tal que f(3) = 5. Assim, é possivel que",
        "alternativas": {
            "a": "3,2",
            "b": "3,6",
            "c": "4,2",
            "d": "4,6"
        }
    },
    {
        "pagina": 10,
        "coluna": "direita",
        "numero": 57,
        "enunciado": "Seja o triangulo ABC, retangulo em B, tal que o ponto E esta em sua hipotenusa e o ponto D, no cateto AB, conforme a figura. Assim, o valor de b’ + 4c’ é",
        "alternativas": {
            "a": "4",
            "b": "8",
            "c": "12",
            "d": "16"
        }
    }

```
esse Json é enviado para o back-end da plataforma onde é armazenado no banco de dados para futuras consultas pela plataforma.

---

## 🧠 Tecnologias usadas
 Visão Computacional
- [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/en/latest/)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [pytesseract](https://pypi.org/project/pytesseract/)
- [Pillow (PIL)](https://pillow.readthedocs.io/)

 Plataforma (front e back-end)
- [next.js](https://nextjs.org/)
- [postgreSQL](https://www.postgresql.org/)

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
