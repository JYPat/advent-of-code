from util.util import get_path

with open(get_path(), "r", encoding="utf-8") as f:
    block = [int(v) for v in f]

hamburger = set(block)

count1, count3 = 0, 0

if 1 in hamburger:
    count1 += 1
elif 2 not in hamburger:
    count3 += 1

for i in hamburger:
    if i + 1 in hamburger:
        count1 += 1
    elif i + 3 in hamburger:
        count3 += 1

count3 += 1
print(count1 * count3)

hamburger = sorted(hamburger)
hamburger.insert(0, 0)
sauce = {0: 1}

for patty in hamburger[1:]:
    sauce[patty] = (
        sauce.get(patty - 1, 0) + sauce.get(patty - 2, 0) + sauce.get(patty - 3, 0)
    )

print(sauce[hamburger[-1]])
