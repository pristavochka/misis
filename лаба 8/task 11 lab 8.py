#Для хранения текста в сжатом виде найти часто повторяющиеся последовательности из двух букв и заменить их кодом. В качестве кода использовать символы, не встречающиеся в тексте. Составить также таблицу кодов.
import re
from collections import defaultdict
def compress_text(input_text):
    freq = defaultdict(int)
    for match in re.finditer(r'(?=(\w\w))', input_text):
        seq = match.group(1)
        freq[seq] += 1
    
    posled = {seq: count for seq, count in freq.items() if count > 1}
    
    codes = {}
    code= 0xE000
    
    for seq in posled:
        codes[seq] = chr(code)
        code += 1
    
    comp_text = input_text
    for seq, code in codes.items():
        comp_text = comp_text.replace(seq, code)
    
    return comp_text, codes

def decomp_text(comp_text, codes):
    reverse_codes = {v: k for k, v in codes.items()}
    
    decomp_text = comp_text
    for code, seq in reverse_codes.items():
        decomp_text = decomp_text.replace(code, seq)
    
    return decomp_text

if __name__ == "__main__":
    input_text = "тект который нужно будет компрессировать"
    
    comp_text, codes = compress_text(input_text)
    print("Сжатый текст:", comp_text)
    print("Таблица кодов:", codes)
    
    decomp_text = decomp_text(comp_text, codes)
    print("Декодированный текст:", decomp_text)
