frombraille = {"⠁" : "a", 
"⠃" : "b", 
"⠉" : "c", 
"⠙" : "d", 
"⠑" : "e", 
"⠋" : "f", 
"⠛" : "g", 
"⠓" : "h", 
"⠊" : "i", 
"⠚" : "j", 
"⠅" : "k", 
"⠇" : "l", 
"⠍" : "m", 
"⠝" : "n", 
"⠕" : "o", 
"⠏" : "p", 
"⠟" : "q", 
"⠗" : "r", 
"⠎" : "s", 
"⠞" : "t", 
"⠥" : "u", 
"⠧" : "v", 
"⠺" : "w", 
"⠭" : "x", 
"⠽" : "y", 
"⠵" : "z",
"⠾" : "with", 
"⠯" : "and", 
"⠿" : "for", 
"⠮" : "the", 
"⠬" : "ing", 
"⠷" : "of", 
"⠡" : "ch", 
"⠣" : "gh", 
"⠩" : "sh", 
"⠌" : "st", 
"⠹" : "th", 
"⠱" : "wh", 
"⠫" : "ed", 
"⠻" : "er", 
"⠳" : "ou", 
"⠪" : "ow", 
"⠔" : "in", 
"⠂" : ",", 
"⠆" : ";", 
"⠒" : ":", 
"⠖" : "!", 
"⠄" : "'", 
"⠤" : "-",
"⠀" : " ",
" " : " " }

frombraillenum = {"⠁" : "1", 
"⠃" : "2", 
"⠉" : "3", 
"⠙" : "4", 
"⠑" : "5", 
"⠋" : "6", 
"⠛" : "7", 
"⠓" : "8", 
"⠊" : "9", 
"⠚" : "0"}

def from_braille(txt) :
    skip = 0
    caps = False
    finaltxt = ""
    capslock = False
    quote = False
    num = False
    bracket = False
    maths = False
    symbol = False
    for i in range(0,len(txt)):
        if skip > 0 :
            skip -= 1
            continue
        elif txt[i] == "\n" :
            finaltxt += "\n"
            num = False
        elif maths == True:
            if txt[i] == "⠖":#######
                finaltxt += "+"
            elif txt[i] == "":
                finaltxt += "="
            else :
                finaltxt += "□"
            maths = False
        elif txt[i:i+2] == "⠠⠄" :
            skip = 1
            capslock = False
        elif txt[i] == "⠠":
            if txt[i:i+2] == "⠠⠠" :
                capslock = True
                skip = 1
            else :
                caps = True
                continue
        elif txt[i] == "⠼" :
            num = True
        elif txt[i] == "⠰" :
            num = False
        elif txt[i] in " ⠤⠄⠆⠒⠖" :
            num = False
            finaltxt += frombraille[txt[i]]
        elif txt[i] == "⠶" :
            if bracket == False:
                finaltxt += "("
                bracket = True
            else:
                finaltxt += ")"
                bracket = False
        elif txt[i] == "⠦" :
            if quote == True:
                finaltxt += "\""
                quote = False
            else :
                if i+1 == len(txt) :
                    if txt[i+1] in frombraille and frombraille[txt[i+1]] == " " :
                        finaltxt += "?"
                else :
                    finaltxt += "\""
                    quote = True 
        elif txt[i] == "⠐" :
            maths = True
        elif txt[i] == "⠸" :
            symbol = True
        #symbol
        else:
            if num == True :
                if txt[i] in frombraillenum :
                    finaltxt += frombraillenum[txt[i]]
                elif txt[i] in frombraille :
                    num = False
                    if caps == True or capslock == True:
                        finaltxt += frombraille[txt[i]].upper()
                    else : 
                        finaltxt += frombraille[txt[i]]
                else :
                    finaltxt += "□"
            else:
                if txt[i] in frombraille :
                    if caps == True or capslock == True:
                        finaltxt += frombraille[txt[i]].upper()
                    else : 
                        finaltxt += frombraille[txt[i]]
                else :
                    finaltxt += "□"
        caps = False
    return(finaltxt)



while True:
    text = input("\nbraille : ")
    print(from_braille(text))