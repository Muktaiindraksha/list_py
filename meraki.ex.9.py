kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
sumc=0
sumd=0
suml=0
for i in kitna_paisa_hai:
    if(i>=10000000):
        sumc+=1
    elif(i>=100000):
        suml+=1
    else:
        sumd+=1
print(sumc,"Crorepati")
print(suml,"Lakhpati")
print(sumd,"Dilwale")

