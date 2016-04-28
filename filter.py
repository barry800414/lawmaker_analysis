
import sys, json

# filter not regional lawmakers 
with open('not_regional_candidate.json', 'r') as f:
    candidate = json.load(f)
with open('not_regional.csv', 'r') as f:
    lawmaker = set()
    for line in f:
        entry = line.split(',')
        lawmaker.add(entry[0].strip())

assert len(candidate) == 1
dataType = list(candidate.keys())[0]

cnt = 0 
newList = [d for d in candidate[dataType] if d['candidatename'] in lawmaker]
print(len(newList), len(lawmaker))

candidate[dataType] = newList
with open('not_regional.json', 'w') as f:
    json.dump(candidate, f, ensure_ascii=False, indent=1)


# filter regional lawmakers 
with open('regional_candidate.json', 'r') as f:
    candidate = json.load(f)
with open('regional.csv', 'r') as f:
    lawmaker = set()
    for line in f:
        entry = line.split(',')
        lawmaker.add(entry[0].strip())

assert len(candidate) == 1
dataType = list(candidate.keys())[0]

cnt = 0 
newList = [d for d in candidate[dataType] if d['candidatename'] in lawmaker]
print(len(newList), len(lawmaker))

candidate[dataType] = newList
with open('regional.json', 'w') as f:
    json.dump(candidate, f, ensure_ascii=False, indent=1)

