# EM python, string s são imutaveis e consegue validar

def two_pointers(s: str) -> int:
    res = ''
    l, r = 0, 0

    while r< l:
        if s[r] == ' ':
            r += 1
        else:
            res += s[l:r+1][::-1]
            r+=1
            l = r
        
        #para inverter a ultima palavra
        res += ''
        res += s[l:r+2][::-1]
        #para cortar o primeiro espaço em branco
        return res[1:]