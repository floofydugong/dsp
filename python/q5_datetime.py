# Hint:  use Google to find python function

####a)

from datetime import datetime

date_start = '01-02-2013'
date_stop = '07-28-2015'

start = datetime.strptime(date_start, "%m-%d-%Y")
stop = datetime.strptime(date_stop, "%m-%d-%Y")

return (stop-start)

####b)

date_start = '12312013'
date_stop = '05282015'

start = datetime.strptime(date_start, "%m%d%Y")
stop = datetime.strptime(date_stop, "%m%d%Y")

return (stop-start)

####c)

date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'

start = datetime.strptime(date_start, "%d-%b-%Y")
stop = datetime.strptime(date_stop, "%d-%b-%Y")

return (stop-start)
