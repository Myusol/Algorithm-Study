sc={'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0,
    'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0}
t,th=0,0
for i in range(20):
    _,h,s=input().split()
    # if s=='P':
    #     continue
    # else:
    #     # t+=float(h)*sc.get(s)
    #     t+=float(h)*sc[s]
    #     th+=float(h)
    if s!='P':
        t+=float(h)*sc[s]
        th+=float(h)
print(t/th)