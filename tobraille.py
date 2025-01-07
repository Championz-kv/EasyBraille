tobraille = { "a" : "⠁", 
"b" : "⠃", 
"c" : "⠉", 
"d" : "⠙", 
"e" : "⠑", 
"f" : "⠋", 
"g" : "⠛", 
"h" : "⠓", 
"i" : "⠊", 
"j" : "⠚", 
"k" : "⠅", 
"l" : "⠇", 
"m" : "⠍", 
"n" : "⠝", 
"o" : "⠕", 
"p" : "⠏", 
"q" : "⠟", 
"r" : "⠗", 
"s" : "⠎", 
"t" : "⠞", 
"u" : "⠥", 
"v" : "⠧", 
"w" : "⠺", 
"x" : "⠭", 
"y" : "⠽", 
"z" : "⠵", 
"1" : "⠁", 
"2" : "⠃", 
"3" : "⠉", 
"4" : "⠙", 
"5" : "⠑", 
"6" : "⠋", 
"7" : "⠛", 
"8" : "⠓", 
"9" : "⠊", 
"0" : "⠚", 
"," : "⠂", 
";" : "⠆", 
":" : "⠒", 
"?" : "⠦", 
"!" : "⠖", 
"'" : "⠄", 
"\"" : "⠦", 
"(" : "⠶", 
")" : "⠶", 
"-" : "⠤", 
"/" : "⠸⠌", 
"\\" : "⠸⠡", 
"&" : "⠯", 
"#" : "⠸⠹",
"." : "⠲",
"|" : "⠸⠳",
"+" : "⠐⠖",
"=" : "⠐⠶",
" " : " ",
"" : "",
"with" : "⠾", 
"and" : "⠯", 
"for" : "⠿", 
"the" : "⠮", 
"ing" : "⠬", 
"of" : "⠷", 
"ch" : "⠡", 
"gh" : "⠣", 
"sh" : "⠩", 
"st" : "⠌", 
"th" : "⠹", 
"wh" : "⠱", 
"ed" : "⠫", 
"er" : "⠻", 
"ou" : "⠳", 
"ow" : "⠪", 
"in" : "⠔" }

def to_braille(txt):
    skip = 0
    brailletxt = ""
    num = False
    caps = False
    for i in range(0,len(txt)):
        if skip > 0 :
            skip -= 1
            continue
        elif txt[i:i+1] == "\n" :
            brailletxt += "\n"
            num = False

        if txt[i].isupper() == True:
            if caps == False:
                if len(txt)-1 == i or txt[i+1].isupper() == False:
                    brailletxt += "⠠"
                else:
                    brailletxt += "⠠⠠"
                    caps = True
        else:
            if caps == True:
                caps = False
                brailletxt += "⠠⠄"

        if txt[i:i+4].lower() in ["with"] :
            if num == True :
                num = False
            skip = 3
            brailletxt += tobraille[txt[i:i+4].lower()]
        elif txt[i:i+3].lower() in ["and","for","the","ing"] :
            if num == True :
                num = False
            skip = 2
            brailletxt += tobraille[txt[i:i+3].lower()]
        elif txt[i:i+2].lower() in ["of", "ch", "gh", "sh", "st", "th", "wh", "ed", "er", "ou", "ow", "in"] :
            if num == True :
                num = False
            skip = 1
            brailletxt += tobraille[txt[i:i+2].lower()]
        elif txt[i] in ["1","2","3","4","5","6","7","8","9","0"] :
            if num == False:
                brailletxt += "⠼"
                num = True
            brailletxt += tobraille[txt[i]]
        elif txt[i] in ["."] :
            brailletxt += tobraille[txt[i]]
        else:
            if txt[i] in " ,-;:?!'\\\"()#&/" :
                num = False
            else:
                if num == True :
                    num = False
                    brailletxt += "⠰"
            brailletxt += tobraille[txt[i].lower()]
    if caps == True:
        brailletxt += "⠠⠄"
    return brailletxt

while True:
    text = input("\ntext : ")
    print(to_braille(text))