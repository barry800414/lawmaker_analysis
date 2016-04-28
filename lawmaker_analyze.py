
import json, sys

NOT_REGIONAL = '全國不分區及僑居國外國民立委公報'


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage:', sys.argv[0], 'data', file=sys.stderr)
        exit(-1)
    
    fileName = sys.argv[1]

    with open(fileName, "r") as f:
        data = json.load(f)

    assert len(data) == 1
    dataType = list(data.keys())[0]
    # print some statistical information
    print('# type:', dataType)
    print('# lawmaker canidate:', len(data[dataType]))

    for d in data[dataType]:
        print(d['candidatename'], end=' ')
        if 'rptedu' in d:
            print(d['rptedu'])   
        else:
            print()

