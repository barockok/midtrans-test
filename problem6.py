string1 = input()
string2 = input()

def anagram(s1, s2):
    all = list(s1+s2)
    a = list(set(s2) - set(s1))
    b = list(set(s1) - set(s2))
    c = list(a+b)

    # removing different char
    result = list(set(all)-set(c))

    return c

agr = anagram(string1, string2)
ooutput = str(len((agr))) + " # " + "removing " + str(agr)

print(ooutput)