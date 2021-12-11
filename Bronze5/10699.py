# 현재 지역의 시간대르 표출하는 코드이다. 

import time
a = time.strftime('%Y-%m-%d', time.localtime(time.time()))
print(a)
