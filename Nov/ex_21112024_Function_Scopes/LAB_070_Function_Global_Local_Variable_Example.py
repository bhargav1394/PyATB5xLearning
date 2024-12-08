# local variables have more preference as compare to public variables.`

public_toilet = "PB"

def home():
    private_toilet="PT"
    print(public_toilet,"\n",private_toilet)

home()
def stranger():
    print(public_toilet)
    #print(private_toilet)

stranger()