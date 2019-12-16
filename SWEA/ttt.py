import re
from collections import Counter
s = " {{1},{1, 2},{1, 2, 3},{1, 2, 3, 4}}"

k = re.sub("{","",s)
j = re.sub("}","",k)
print(j)
c = Counter(j)
print(c)