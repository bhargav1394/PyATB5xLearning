def test(a,b):
    print("positional Args:",a,b)

test(10,20)
#Non-extra Keyword args
def test1(*args):
    print("Non-extra keywords:",args)
test1(30,40,50,60)

test1()

#Default argument
def test3(a=20,b=30):
    print("Default argument:",a,b)

test3()
test3(50,60)

#extra keyword arguments
def test4(**kwargs):
    print("kwargs",kwargs)
test4(a=2,b=3,c=True)

test4()
#Keyword only args

def test5(a,b=30):
    print("keyword only args",a,b)
test5(a=20,b=50)

#mix Argument
def test6(a,b,*args,c=20,d=30,**kwargs):
    print("Positional", a,b)
    print("Non-extra",args)
    print("Default",c,d)
    print("extra keyword",kwargs)

test6(10,20,30,40,50,60,c=50,p=True,q="Demo")