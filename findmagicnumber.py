import sys
import timeit

def validateNumber(numberStr, breakEarly=False):
    result = 0
    for c in str(numberStr):
        result = result + int(c)
        if breakEarly:
            if result > 20:
                break
    if result == 20:
        return True
    else:
        return False

def getTestData(upperbound):
    result = []
    for i in xrange(upperbound):
        result.append(i)

    return result

def runTest():
    for num in getTestData(int(sys.argv[1])):
        validateNumber(num)

def runTest2():
    for num in getTestData(int(sys.argv[1])):
        validateNumber(num, True)

if __name__ == "__main__":
    print "keep running", timeit.timeit("runTest()", "from __main__ import runTest", number=1)
    print "break early", timeit.timeit("runTest2()", "from __main__ import runTest2", number=1)
