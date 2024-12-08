# local variables have more preference as compare to public variables.`

public_toilet = "PB"

def home():
    private_toilet="PT"
    #print(public_toilet)
    print(private_toilet)
    public_toilet = "LPB"
    print(public_toilet)

home()