import itertools

def getPossibleResults(a, b):
    out = {}
    out[a+b]="{}+{}".format(a,b)
    out[a-b]="{}-{}".format(a,b)
    out[b-a]="{}-{}".format(b,a)
    out[b*a]="{}*{}".format(a,b)
    if a == b:
        if a != 0:
            out[1]="{}/{}".format(a,b)
    else:
        if a != 0:
            if b % a ==0:
                out[b/a]="{}/{}".format(b,a)
        if b != 0:
            if a % b ==0:
                out[a/b]="{}/{}".format(a,b)
    return out

def debug(a):
    import traceback;
    print "  " * len(traceback.extract_stack()), a

def solve(numbers, target):
    # solve([1,3,5,2], 13)
    # one possible return:
    # ["3*5=15", "15-2=13"]
    if target in numbers:
        return [str(target)]
#    debug("Solve: {}".format(numbers))
    for a, b in itertools.combinations(numbers, 2):
#        debug("{}, {}".format(a,b))
        new_numbers = list(numbers)
        new_numbers.pop(new_numbers.index(a))
        new_numbers.pop(new_numbers.index(b))

        for res, expl in getPossibleResults(a, b).items():
            r = solve(new_numbers + [res], target)
            if r:
                return [expl + "=%s" % res] + r
    return []

def run(nums):
    for x in xrange(1,1000):
        print x,
        ans = solve(nums, x)
        if not ans:
            print "Nothing found"
            return 
        print ans

if __name__=="__main__":
    import sys
    run(map(int, sys.argv[1:]))
