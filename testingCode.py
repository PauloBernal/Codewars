def createCalendar(month):
    ac = ''
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    for i in days:
        ac = ac + i + '     '
    print(f'\n                     {month}\n')
    print(ac)

createCalendar('March')