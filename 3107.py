ip = input()
#하나의 그룹을 :: 로 변경한 경우
if ip.count(":") ==8:
    ip = ip.replace("::",":")
#두개 이상의 그룹을 ::로 변경한 경우
ip = ip.replace("::",(7-ip.count(":"))*":" + "::")
ip = ip.split(":")

#각 그룹내에서 0이 생략된 경우
for i in range(len(ip)):
    if len(ip[i]) < 4:
        ip[i] = (4-len(ip[i]))*'0'+ip[i]

print(":".join(ip))