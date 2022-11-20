import string
import collections

alphabet = { 1: "а", 2: "б", 3: "в", 4: "г", 5: "д", 6:"е", 7:"ё", 8:"ж",
9:"з", 10:"и", 11:"й", 12:"к", 13:"л", 14:"м", 15:"н", 16:"о", 17:"п", 
18:"р", 19:"с", 20:"т", 21:"у", 22:"ф", 23:"х", 24:"ц", 25:"ч", 26:"ш",
27:"щ", 28:"ъ", 29:"ы", 30:"ь", 31:"э", 32:"ю", 33:"я" }
alphabet_r = { x:y for y, x in alphabet.items()}

most_frequent_letters =  ["о", "е", "a", "и" ]

def decrypt_cipher(key):
    print(str(key))
    for char in ciphertext:
        if char in alphabet_r.keys():
            c_pos = int(alphabet_r[char])
            m_pos = c_pos + key
            if m_pos > 33:
                m_pos = m_pos - 33
            print(alphabet[m_pos], end='')
        else:
            print(char, end='')
        
    print('\n')
     

def get_keys(ld):
    for item in ld:
        frequent_ch = item[0]
        common_ch = item[1]
        item = alphabet_r[common_ch] -  alphabet_r[frequent_ch]
        if item < 0:
            item = 33 + item
        if item != 0:
            yield item

def create_lookup_table(lst_one, lst_two):
    lst_res = []
    for el_one in lst_one:
        for el_two in lst_two:
            lst_res.append(*zip(el_one, el_two))
    return list(set(lst_res)) 

def main():
    global ciphertext
    with open("ciphertext.txt", "r") as file:
         ciphertext = file.readline()

    ciphertext = ciphertext.lower()
# Здесь я пытался использовать частотность букв в русском языке
    nl = len(most_frequent_letters)
    most_common_letters = [ x for (x, y) in collections.Counter(ciphertext.replace(" ", "")).most_common(nl)]
    print(most_frequent_letters)
    print(most_common_letters)
    lookup_table = create_lookup_table(most_frequent_letters, most_common_letters)
    print(lookup_table)
    key_lists = [key for key in get_keys(lookup_table)]
    for key in key_lists:
          decrypt_cipher(key)

if __name__ == "__main__":
    main()
