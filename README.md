# alma_time

Print available ALMA time in different configurations for a given LST range.

```
import alma_time

# print all
alma_time.time_available()

# print specific
alma_time.time_available(lst_start=1, lst_end=5, configs=['C3','C10'], bands=['Total','Band 9/10'])

# Total C3 126.1 h
# Total C10 62.4 h
# Total total (excl. ACA) 188.5 h

# Band 9/10 C3 3.1 h
# Band 9/10 C10 2.6 h
# Band 9/10 total (excl. ACA) 5.7 h

# All bands total (excl. ACA) 194.2 h
# All bands total ACA 0 h
```
