import pdfplumber

def extract_text_from_pdf(pdf_path, output_file=None):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            if output_file:
                with open(output_file, 'w', encoding='utf-8') as f:
                    for page_num, page in enumerate(pdf.pages, 1):
                        text = page.extract_text()
                        f.write(f"страница {page_num}:\n")
                        if text:
                            f.write(text + "\n")
                        else:
                            f.write("(Текст не обнаружен или страница пустая)\n")
                        f.write("=" * 60 + "\n\n")
                print(f"Текст сохранен в файл: {output_file}")
            else:
                all_text = ''
                for page_num, page in enumerate(pdf.pages, 1):
                    text = page.extract_text()
                    # print(f"страница {page_num}:")
                    all_text += str(page_num)
                    if text:
                        # print(text)
                        all_text += str(text)
                    else:
                        print("(Текст не обнаружен или страница пустая)")
                    # print("=" * 60)

    except FileNotFoundError:
        print(f"Файл {pdf_path} не найден")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    return all_text

# extract_text_from_pdf("data/Неверные 18+/NV_1_v9_fin_.pdf")  # вывод в консоль
# extract_text_from_pdf("data/Неверные 18+/NV_1_v9_fin_.pdf", "output.txt")  # сохранение в файл