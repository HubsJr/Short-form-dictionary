print("we currently have 11 short forms available in our dictionary:")
OMG=("OMG")
GR8=("GR8")
LOL=("LOL")
NP=("NP")
IDK=("IDK")
ATM=("ATM")
IMO=("IMO")
JIC=("JIC")
A3=("A3")
VN=("VN")
SIC=("SIC")
RIP=("RIP")
PUFF=("PUFF")
OMGFF=("this is FullForm of OMG:\nOH MY GOD")
GR8FF=("this is the FullForm of GR8:\nGREAT")
LOLFF=("this is the FullForm of LOL:\nLAUGH OUT LOUD")
NPFF=("this is the FullForm of NP:\nNO PROBLEM")
IDKFF=("this is the FullForm of IDK:\nI DON'T KNOW")
ATMFF=("this is the FullForm of ATM:\nAT THE MOMENT")
IMOFF=("this is the FullForm of IMO:\nIN MY OPINION")
JICFF=("this is the FullForm of JIC:\nJUST IN CASE")
A3FF=("this is the FullForm of A3:\nANYWHERE,ANYTIME,ANY PLACE")
VNFF=("this is the FullForm of VN:\nVERY NICE")
SICFF=("this is FullForm of SIC:\nTHUS,SO,AS SUCH OR IN SUCH MANNER")
PUFFGG=("this is FullForm of PUFF:\nPEOPLE UNITED FOR FUN AND FRIENDSHIP")
RIPFF=("this is FullForm of RIP:\nREST IN PEACE")
ENTER=str(input("Enter a short form:"))
ENTERR=ENTER.upper()
if ENTERR==OMG:
    print(OMGFF)
elif ENTERR==GR8:
    print(GR8FF)
elif ENTERR==LOL:
    print(LOLFF)
elif ENTERR==NP:
    print(NPFF)
elif ENTERR==IDK:
    print(IDKFF)
elif ENTERR==ATM:
    print(ATMFF)
elif ENTERR==IMO:
    print(IMOFF)
elif ENTERR==JIC:
    print(JICFF)
elif ENTERR==A3:
    print(A3FF)
elif ENTERR==VN:
    print(VNFF)
elif ENTERR==SIC:
    print(SICFF)
elif ENTERR==RIP:
    print(RIPFF)
elif ENTERR==PUFF:
    print(PUFFGG)
else:
    print("Sorry we don't have that Short form in our dictionary yet, but we will soon add it")