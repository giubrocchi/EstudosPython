def ePrimo(k):
    if(k < 2):
        return False
    i = 2
    while(i <= k/2):
        if(k%i == 0):
            return False
        i += 1
    return True

def maior_primo(n):
    while(n >= 2):
        if(ePrimo(n)):
            return n
        n -= 1
    return 0
