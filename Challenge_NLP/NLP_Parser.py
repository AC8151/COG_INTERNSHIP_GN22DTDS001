## NLP PARSER ##

import sys # for r/w to system
import re # regex for pattern matching

## reading file from cmd
def file_reader():
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        contents = f.read()
    return contents    

## finding currencies (only $,£,₹)      
def currency_parser(file):
    cur = re.findall(r"([$£₹][0-9]+\.?[0-9]*)", file)
    if cur == []: return '\nNo Currency'
    return '\nCurrencies: '+str(cur)

## finding dates dd/mm/yyyy or yy and mm/dd/yyyy or yy
def date_parser(file):
    date = re.findall(r"(\d{2}/\d{2}/\d{2,4})", file)
    #print(re.findall('(0[1-9]|[12][0-9]|3[01]|1[1-2]/0[1-9]|[12][0-9]|3[01]|1[1-2]/\d{4}|d{2})', file))
    if date == []: return '\nNo Dates'
    return '\nDates: '+str(date)

## finding ardinalities and orders
def cardi_ord_parser(file):
    car = re.findall(r"(\d+(?:st|[nr]d|th))", file)
    ordi = re.findall(r"/first|second|tw(?:elfth|entieth)|th(?:irt(?:eenth|ieth)|ird)|fi(?:ft(?:eenth|ieth)|h)|(?:four|six|seven)(?:teenth|th|tieth)|eight(?:eenth|h|ieth)|nin(?:e(?:teenth|tieth)|th)|tenth|eleventh|fortieth|hundreth|thousandth/i", file)
    combi = car+ordi
    if combi == []: return '\nNo cardinality/order'
    return '\nCardinalities/Orders: '+str(combi)

## finding 4 letter words starting with vowels
def vowel_parser(file):
    vow = re.findall(r"\b[aeiouAEIOU][a-zA-Z]{3}\b", file)
    if vow == []: return '\nNo 4 letter words beginning with vowels'
    return '\n4 letter words begins with vowels: '+str(vow)


if __name__=='__main__':
    file = file_reader()
    print('\n\n---NLP PARSER---\nBy - Aditi Chatterjee') ## title
    print('\n\nTHE FILE:\n{}\n\nPARSING RESULTS:'.format(file)) ## displaying file contents
    
    ## performing requisite parsing
    print(currency_parser(file))
    print(date_parser(file))
    print(cardi_ord_parser(file))
    print(vowel_parser(file))
          
