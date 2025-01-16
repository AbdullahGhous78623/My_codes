algebraic_expression="(x+y)+(z+q)"
WE=""

for i in algebraic_expression:
    if i!="(" and i!=")":
        WE+=i
print(WE)
