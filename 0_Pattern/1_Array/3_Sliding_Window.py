#QUando a solução do problema subarray não se reperto por exepmplo

#while 
#R++
#while dentro 
#l+++


def sliding_window(self, s: str) -> int:
    left, right = 0, 0

    counter = {} 

    #inicia o contador
    counter[s[0]] = 1


    while right < len(s):
        r += 1
        #Expande a janel
        if count.get(s[righ]) : 
            count[s[right]] += 1
        else:
            count[s[right]] = 1
        while counter[s[right]] == 3:
            counter[s[left]] -= 1
            left += 1
    