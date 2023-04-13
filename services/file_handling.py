BOOK_PATH = 'book/Bredberi_Marsianskie-hroniki.txt'
PAGE_SIZE = 750

book: dict[int, str] = {}

def _get_part_text(text: str, start: int, page_size: int) -> tuple[str, int]:
    general_symbols = '!?.'
    symbols = general_symbols + ',:;'
    t = text[start : start + page_size]
    if start + page_size < len(text):
        if text[start + page_size] in general_symbols:
            t = t.rstrip(general_symbols)
        for i, char in enumerate(reversed(t)):
            if char in symbols:
                t = t[:len(t) - i]
                break
                
    return t, len(t)

def prepare_book(path: str) -> None:
    with open(path) as file:
        text = file.read()

    counter = 1
    string_len_sum = 0

    while len(text) > string_len_sum:
       string, string_len = _get_part_text(text=text, start=string_len_sum, page_size=PAGE_SIZE)
       string_len_sum = string_len_sum + string_len + 1 
       book[counter] = string.lstrip()
       counter += 1

prepare_book(BOOK_PATH)

