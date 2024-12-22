txt = input()
target = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"
for ch in txt:
    print(target[(ord(ch) - ord('가'))//588],end="")