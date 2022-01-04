'''
this function 
converts text to morse code
"^" - point
"^^^" - dash
"_" - pause between elements
"___" - pause between letters
"_______"pause between words
 '''

def encode_morze(poslanie):
    poslanie = str(poslanie)
    poslanie = poslanie.upper()
    morse_code = {
        "A" : ". -",
        "B" : "- . . .",
        "C" : "- . - .",
        "D" : "- . .",
        "E" : ".",
        "F" : ". . - .",
        "G" : "- - .",
        "H" : ". . . .",
        "I" : ". .",
        "J" : ". - - -",
        "K" : "- . -",
        "L" : ". - . .",
        "M" : "- -",
        "N" : "- .",
        "O" : "- - -",
        "P" : ". - - .",
        "Q" : "- - . -",
        "R" : ". - .",
        "S" : ". . .",
        "T" : "-",
        "U" : ". . -",
        "V" : ". . . -",
        "W" : ". - -",
        "X" : "- . . -",
        "Y" : "- . - -",
        "Z" : "- - . .",
        " " : "_",
        "1" : "",
        "2" : "",
        "3" : "",
        "4" : "",
        "5" : "",
        "6" : "",
        "7" : "",
        "8" : "",
        "9" : "",
        "0" : ""
       }
    poslanie_kod_morse=''
    for i in poslanie:
        poslanie_kod_morse=poslanie_kod_morse+(morse_code[i])
        poslanie_kod_morse=poslanie_kod_morse+"   "    
    z=poslanie_kod_morse
    z=z.replace(".", "^")
    z=z.replace("-", "^^^")
    z=z.replace(' ', '_')
    z=z[:-3]
    return z

print (encode_morze('hello'))
