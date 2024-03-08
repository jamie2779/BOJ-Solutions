s=input()
l=len(s)
now =[False]*l
for i in range(l):
     target = []
     target_st=[]
     j=0
     #가능한 경우의 수 다 구함
     while j<l:
          if now[j]:
               j+=1
               continue
          t = now[:]
          t[j]=True
          target.append(t)
          st = ""
          for k in range(l):
               if t[k]:
                    st+= s[k]
          target_st.append(st)
          j+=1     

     #사전순으로 가장 작은 것 찾기     
     min_n=target[0]
     min_st=target_st[0]     
     for j in range(len(target)):
          if target_st[j]<min_st:
               min_st = target_st[j]
               min_n = target[j]
     print(min_st)
     now = min_n