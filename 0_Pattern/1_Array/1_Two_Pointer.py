#dois ponteiros para preencher o array, e usar para inverter string, ou inverter palavras
#através de encontrar um espaço

#reverString

class Solution:
    def reverseWords_manual(s):
        res = ''
        left, rigth = 0,0

        while right < len(s):
            #Verifica se Right é um espaço em branco 
            if s[right] != ' ':
                right += 1
            else:
                #Inverte a palavra
                res = s[left:right+1] [::-1]

                #Nova palavra
                left = right + 1
            right += 1
        res = s[left:right] + ' ' + res
        return res