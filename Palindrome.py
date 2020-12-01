def solution(S): 
    temp_s='' 
    S=S.lower() 
    liste=list(S) 
    print(liste) 
    for i in range(len(liste)): 
        if liste[i]=='?': 
            liste[i]=liste[-i-1] 
        temp_s+=liste[i] 
    print(temp_s) 
    if temp_s==temp_s[::-1]: 
        return(temp_s) 
    else: 
        return('NO')
print(solution('?ab??a'))
