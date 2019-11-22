Un = (1,2,4,8)
Eq = ""
C = 0
iterra = 0
Sum = 0

def setSum(v) :
    global Sum
    Sum = v

def getSum() :
    return Sum

def setitt(v) :
    global iterra
    iterra = v

def getitt() :
    return iterra

def setC(v) :
    global C
    C = v

def setValue(v) :
    global Eq
    Eq = v

def getValue() :
    return Eq

def setFormula(q0=0, M=0) :
    if getValue() == "" :
        s = Eq+"Un = {} x {}^n".format(q0,M)
    else:
        s = Eq+" + {} x {}^n".format(q0, M)
    return s

quotions = []
def setquots(sequence) :
    quotions.clear()
    for i in range(1, len(sequence)):
        quotions.append(sequence[i] - sequence[i - 1])
def safetytest() :
    for i in range(0,len(quotions)) :
        if quotions[i] == 0 : return False
    return True

def testFor(sequence, ac=1,ac2=0) :
    print("Testing For Seq ", sequence)
    setquots(sequence)
    if testValidity(sequence) :
        print("Contant Sequence ! No Formula")
        return False
    if safetytest() :
        valid, M = testAdmision(sequence)
        if valid and M != 0 :
            print("Mult detected -> ", M)
            if testType(sequence,M) :
                print("Formula structure : ", Eq)
                print("Sum Of Sequence :   ", getSum())
                return True
            else:
                setSum(sume(sequence))
                w=2
                seq2 = []
                for i in range(1,len(sequence)) :
                    key = (sequence[i]-M*sequence[i-1])
                    seq2.append(key)
                if testValidity(seq2) :
                    print("General Type Un+1 = {} x Un + {}".format(M, key))
                else: print("General Type Unknown")
                print("key q0 = ", quotions[0])
                if ac == 1 :
                    ac2 = 0
                    print("PROTOCOL TSTM USED")
                    if protocolTSTM(sequence, quotions[0]) :
                        setValue(setFormula(quotions[0], M))
                        St = getValue() + " + {}".format(C)
                        setValue(St)
                        print("Formula structure : ", Eq)
                        print("Sum Of Sequence :   ", getSum())
                        return True
                if ac2 == 1 :
                    ac2 = 1
                    ac = 0
                    print("PROTOCOL TST USED")
                    while w < 10 :
                        if protocolTST(sequence, w) and ac2 == 1 :
                            setValue(setFormula(getitt(),M))
                            St = getValue()+" + {}".format(C)
                            setValue(St)
                            print("Formula structure : ", Eq)
                            print("Sum Of Sequence :   ", getSum())
                            return True
                        w += 1
        else :
            print("Can't detect Mult")
            print("Testing protocole TST")
            return protocolTST(sequence)

def protocolTSTM(sequence, start) :
    if start > 0 :
        subseq = []
        setquots(sequence)
        if safetytest() :
            valid, M = testAdmision(sequence)
            if valid and M!=0 :
                print("Admission OK")
                for i in range(0, len(sequence)):
                    key = sequence[i] - start * (M**i)
                    subseq.append(key)
                if testValidity(subseq) :
                    setC(key)
                    print("Valide")
                    return True
                else: return protocolTST(sequence, start-1)
    return False

def protocolTST(sequence, start=2) :
    if start < 10 :
        subseq = []
        for i in range(0, len(sequence)) :
            key = sequence[i]-start**i
            subseq.append(key)
        setquots(subseq)
        if testValidity(subseq):
            setC(key)
            print("Valide")
            return True
        if safetytest() :
            setitt(getitt() + 1)
            valid, M = testAdmision(subseq)
            if valid and M !=0 :
                print("Admission OK")
                setValue(setFormula(getitt(),start))
                setitt(0)
            return testFor(subseq,0,1)
    return False

def testValidity(sequence) :
    for i in range(1,len(sequence)) :
        if sequence[i] != sequence[i-1] :
            return False
    return True

def testType(sequence,M=0,type=1) :
    if type==1 :
        for i in range(1, len(sequence)) :
            if M!=1 :
                return testType(sequence,M, 2)
            else:
                print("Arithmetic type Un+1 = Un + r")
                print("Sum of elements Formula Sn = (n-p+1)( Un + Up ) / 2")
                setValue("Un = {} + n x {}".format(sequence[0], sequence[1]-sequence[0]))
                setSum(len(sequence)*((sequence[len(sequence)-1]+sequence[0])/2))
                return True
    if type==2 :
        for i in range(1, len(sequence)):
            if sequence[i] != M * sequence[i-1] :
                return False
            else:
                print("Geometric type Un+1 = M x Un")
                print("Sum of elements Formula Sn = Up x (1-q^(n-p+1))/(1-q)")
                setValue("Un = {} x {}^n".format(sequence[0], M))
                setSum(sequence[0]*((1-M**len(sequence))/(1-M)))
                return True


def testAdmision(sequence) :
    for i in range(2, len(quotions)) :
        if quotions[i-1]/quotions[i-2] == quotions[i]/quotions[i-1] :
            M = quotions[1]/quotions[0]
            return True, M
    return False, 0

def sume(sequence) :
    S=0
    for i in range(0, len(sequence)) :
        S += sequence[i]
    return S

def generate(U0, M, CT, n=10) :
    seq = []
    seq.append(U0)
    print("GENERATED ",n," TERMS")
    print("U 0 = ", U0)
    for i in range(1, n) :
        U0 = M*U0 + CT
        seq.append(U0)
        print("U",i,"= ", U0)
    return seq

if __name__ == '__main__':
    testFor(Un)

