import Pmf
import operator

def Mode(hist):
    return max(hist.Items(), key=lambda x: x[1])[0]

def AllModes(hist):
    return sorted(hist.Items(), key=operator.itemgetter(1), reverse=True)

if __name__ == '__main__':
    hist = Pmf.MakeHistFromList([1,2,2,3,5]) #made up values
    print "Mode of hist is: ", Mode(hist)
    print "Value-frequency pairs (in desc. order): ", AllModes(hist)