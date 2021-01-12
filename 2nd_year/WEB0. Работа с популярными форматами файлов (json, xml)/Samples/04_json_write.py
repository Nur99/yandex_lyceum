import json

weekdays = {i: day
            for i, day in enumerate(['Sunday', 'Monday',
                                     'Tuesday', 'Wednesday',
                                     'Thursday', 'Friday',
                                     'Saturday'])}
data = json.dumps(weekdays)
print(data)
print(type(data))
