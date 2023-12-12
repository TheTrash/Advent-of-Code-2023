import re
test = "?###???????? 3,2,1"

onsen = test.split(" ")[0]
work = test.split(" ")[1].split(",")

print(onsen, work)

unknown = r'\?+'
working = r'\#+'


unknown_onsen = [(match.start(), match.end(), match.group()) for match in re.finditer(unknown, onsen)]
working_onsen = [(match.start(), match.end(), match.group()) for match in re.finditer(working, onsen)]

print(unknown_onsen)
print(working_onsen)