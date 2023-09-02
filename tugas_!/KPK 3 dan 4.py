from itertools import count
kelipatan3 = 3
kelipatan4 = 4
kpk = 1

for i in count(0):
  if kpk % kelipatan3 == 0 and kpk % kelipatan4 ==0:
    break
  else:
    kpk += 1
print("KPK dari", kelipatan3, "dan", kelipatan4, "adalah", kpk)