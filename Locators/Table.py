def bookname(Bname, coln):
    i=0
    if coln== "Author":
        i=2
    elif coln== "Subject":
        i=3
    elif coln== "Price":
        i= 4
    return "//tr[td[text()='"+Bname+"']]//td["+str(i)+"]"