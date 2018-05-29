


from datetime import datetime

utc_time = datetime.strptime("2015-09-15T17:13:29.380Z",
                             "%Y-%m-%dT%H:%M:%S.%fZ")

milliseconds = (utc_time - datetime(1970, 1, 1))

print(milliseconds)