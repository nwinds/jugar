# iff serialNum are the same family then is related, v.v
class Cert(object):

    def __init__(self, subject, issuer, serialNum):
        self.subject = subject
        self.issuer = issuer
        self.serialNum = serialNum

    def selfSigned(self):
        return self.subject and self.subject == self.issuer

    def __repr__(self):
        return '(%s, %s, 0x%08x)' % (self.subject, self.issuer, self.serialNum)


# issuer cert: iCert, subject cert: sCert
def check_issuer(iCert, sCert):
    return iCert.subject == sCert.issuer and iCert.serialNum == (sCert.serialNum >> 4)


def find_issuer(stack, issuer):
    for item in stack:
        if item.subject == issuer:
            return item
    return None  # cound't find one issuer


child = Cert('Charlie', 'Bob', 0x111)
parent = Cert('Bob', 'Frank', 0x11)
parent1 = Cert('Bob', 'Frank', 0x22)
grandpa = Cert('Frank', 'Frank', 0x1)
garanpa1 = Cert('Frank', 'Frank', 0x2)

storedStack = [child, parent, parent1, grandpa]  # FIFO, 0 is the TOP
chainStack = []  # should not be okay

# set certs to be verified
cert = child
currCert = cert
# chainStack.append(currCert)
# search from bottom to top(logic)
while True:
    chainStack.append(currCert)
    # quit at first matches
    currCert = find_issuer(storedStack, currCert.issuer)
    if currCert.selfSigned():
        chainStack.append(currCert)
        break


# def constructStack()
# print chainStack
print(chainStack)


# verify
#cnt = len(chainStack)
currCert = chainStack[-1]
subjCert = None
while len(chainStack) > 0:
    if currCert.selfSigned():
        break
    subjCert = chainStack[-1]
    if not check_issuer(currCert, subjCert):
        print('Varification failed')


print('Varification over')
