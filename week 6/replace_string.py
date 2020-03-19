def replace(s, old, new):
    x = s.split(old) #deleting letters=old
    glue = new         #use new input as glue
    y = glue.join(x)    #put glue(=new) between the items in the list
    print(y)


replace("Mississippi", "i", "I")