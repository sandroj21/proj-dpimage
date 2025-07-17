from utils.extractor import extract_text_from_pdf
from utils.parser import parse_questions_from_text_advanced
from config import PDF_PATH, OUTPUT_FILENAME
import json
import logging
from google.colab import files

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    texto_completo = extract_text_from_pdf(PDF_PATH)
    questoes_json = parse_questions_from_text_advanced(texto_completo)

    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as f:
        json.dump(questoes_json, f, ensure_ascii=False, indent=4)

    logging.info(f"Arquivo JSON '{OUTPUT_FILENAME}' criado com sucesso.")
    files.download(OUTPUT_FILENAME)

if __name__ == "__main__":
    main()
