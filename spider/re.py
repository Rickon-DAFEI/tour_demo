import re

words = "awdawd.aweracz.qawxzc"
ans = re.findall(r'(.)\s+(.)',words)
print(ans)