a=[4,5,7,56,456,4,365,246]

greatest=a[0]

for i in a[1:]:
    if i>greatest:
        greatest=i
    
while greatest in a:
    a.remove(greatest)
print(a)
sec_greatest=a[0]
for j in a[1:]:
    if i>sec_greatest:
        sec_greatest=j

print(sec_greatest)


