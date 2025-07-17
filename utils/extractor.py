import fitz
import logging
from PIL import Image
import io
from utils.ocr import extract_text_from_image_columns

def extract_text_from_pdf(pdf_path: str) -> str:
    logging.info(f'Carregando PDF: {pdf_path}')
    doc = fitz.open(pdf_path)
    all_text = []

    for page_num, page in enumerate(doc, start=1):
        logging.info(f'Processando página {page_num}/{len(doc)}')
        pix = page.get_pixmap(dpi=300)
        img_data = pix.tobytes("png")
        image = Image.open(io.BytesIO(img_data))

        page_text = extract_text_from_image_columns(image, page_num)
        all_text.append(page_text)

    logging.info('Extração de texto de todas as páginas completada.')
    return "\n".join(all_text)
