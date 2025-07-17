from PIL import Image
import pytesseract
import logging

def extract_text_from_image_columns(image: Image.Image, page_num: int) -> str:
    width, height = image.size

    left_column_box = (0, 0, width // 2, height)
    right_column_box = (width // 2, 0, width, height)

    left_image = image.crop(left_column_box)
    right_image = image.crop(right_column_box)

    config = '--psm 4'
    lang = 'por+eng'

    logging.info(f'Extraindo texto da coluna esquerda da página {page_num}')
    left_text = pytesseract.image_to_string(left_image, lang=lang, config=config)

    logging.info(f'Extraindo texto da coluna direita da página {page_num}')
    right_text = pytesseract.image_to_string(right_image, lang=lang, config=config)

    return f"{left_text}\n{right_text}"
