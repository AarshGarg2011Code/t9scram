from loadkeys import loadkeys, loadkeypad

sampletext = "Lorem Ipsum Dolor Sit Amet"
samplescrambled = "56736 47786 36567 748 2638"
sampledkey = "33321S31421S13333S431S1121"

chars = """1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"""
chars_upper = """1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"""

keys = loadkeys()
keypad = loadkeypad()

def scramble(text: str = sampletext):
    dkey = []
    scrambled = []
    for i in text:
        if i not in chars:
            dkey.append("S")
            scrambled.append(str(i))
            continue
        else:
            if i in chars_upper:
                snum = keys[i][0]
                dnum = keys[i][1]
                scrambled.append(str(snum))
                dkey.append(str(dnum))
                continue
            else:
                j = i.upper()
                snum = keys[j][0]
                dnum = keys[j][1]
                scrambled.append(str(snum))
                dkey.append(str(dnum))
                continue
    dkey = ''.join(dkey)
    scrambled = ''.join(scrambled)
    return scrambled, dkey

def unscramble(scrambled: str = samplescrambled, dkey: str = sampledkey):
    unscrambled = []
    stlen = len(scrambled)
    dklen = len(dkey)
    if stlen != dklen: raise ValueError("Error: Length of Scrambled Text does not match length of Descramble Key")
    for i in range(stlen):
        stchar = scrambled[i]
        dkchar = dkey[i]
        if dkchar == "S":
            unscrambled.append(stchar)
            continue
        utchar = keypad[stchar][int(dkchar)]
        unscrambled.append(utchar)
    unscrambled = ''.join(unscrambled)
    return unscrambled

