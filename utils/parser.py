import re
import logging

def parse_questions_from_text_advanced(text: str) -> list:
    logging.info('Iniciando a análise avançada para extrair questões...')
    questions = []
    split_text = re.split(r'(?=\n\s*(?:Questão\s+)?\d{1,2}\s*[-–.]\s*)', text)

    for question_block in split_text:
        question_block = question_block.strip()
        if not question_block or not re.match(r'^(?:Questão\s+)?\d{1,2}', question_block):
            continue

        logging.info(f"Processando bloco de questão: {question_block[:80]}...")

        try:
            alternatives_matches = list(re.finditer(r'^\s*([a-d])\)\s*', question_block, re.MULTILINE))
            if not alternatives_matches:
                logging.warning("Nenhuma alternativa encontrada.")
                continue

            question_number = int(re.match(r'^(?:Questão\s+)?(\d{1,2})', question_block).group(1))

            first_alt_start = alternatives_matches[0].start()
            header = question_block[:first_alt_start].strip()

            texto_apoio = ""
            enunciado = ""

            support_match = re.search(r'["“]([\s\S]+?)["”]', header)
            if support_match:
                texto_apoio = support_match.group(1).strip()
                enunciado = header.replace(support_match.group(0), '').strip()
            else:
                enunciado = header

            enunciado = re.sub(r'^(?:Questão\s+)?\d{1,2}\s*[-–.]\s*', '', enunciado).strip()

            alternatives = {}
            for j, match in enumerate(alternatives_matches):
                key = match.group(1)
                start = match.end()
                end = alternatives_matches[j + 1].start() if j + 1 < len(alternatives_matches) else len(question_block)
                alt_text = re.sub(r'\s+', ' ', question_block[start:end]).strip()
                alternatives[key] = alt_text

            questions.append({
                "numero_questao": question_number,
                "enunciado": enunciado,
                "texto_apoio": texto_apoio,
                "alternativas": alternatives
            })
            logging.info(f"Questão {question_number} extraída com sucesso.")

        except Exception as e:
            logging.error(f"Erro ao processar questão: {e}")

    logging.info(f"Total de {len(questions)} questões extraídas.")
    return questions
