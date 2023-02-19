from datetime import datetime
date1=datetime(2023, 2, 20, 0, 23, 0)
date2=datetime(2023, 2, 19, 0, 23, 0)
x=(date1-date2).total_seconds()
print(x)