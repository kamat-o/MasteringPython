def last2(str):
    last_two = str[-2:]
    cntr=0
    for i in range(len(str)-2):
        mword = str[i:i+2]
        if mword==last_two:
            cntr+=1
    print(cntr)

last2('hixxhi')