#coding: utf-8
integ = int(input())
flot = float(input())
intg_pos = int(input())
print(f"{integ:0=+10}")
print(f"{flot:#>10.2f}")
res_current = (f"{(intg_pos):0>16b}")
res_current = str(res_current)
result = str(res_current)
result = (result[::-1])
print('_'.join(result[i:i+4] for i in range(0, len(result), 4))[::-1])
