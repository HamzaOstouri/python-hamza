class myString:
    def __init__(self,s):
        self.s = s
    def append(self,x):
        self.s = self.s + x
        return self.s

    def pop(self,i):
        s1 = self.s[0:i] # de 0 à i-1
        s2 = self.s[i+1:len(self.s)] # de i à [len(s)-1] c a d (n-1)
        return s1+s2
    def modifier(self,i):
        pass
        
# Tester la classe       
S = myString("Bara nayek")
print(S.pop(5)) # affiche 'hllo'
print(S.append(" greyhound ")) # affiche 'hello world !'
