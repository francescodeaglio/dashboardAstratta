import json
import os
from dashboard_abstract.utils import get_session_id

class Logger():

    def __init__(self, name, screen_name = None, chart_name = None):
        self.name = name

        filename = os.path.join(os.curdir, "json", str(get_session_id()))
        dir = os.listdir(os.path.join(os.curdir, "json"))

        print(get_session_id() in dir)

        if get_session_id() in dir:
            with open(filename, "r") as fp:
                data = json.load(fp)


            for key in name:
                if screen_name is None:
                    #è un widget del main
                    data[key] = name[key]
                elif chart_name is None:
                    #è un widget dello screen
                    if screen_name not in data:
                        data[screen_name] = {}
                    data[screen_name][key] = name[key]
                else:
                    if screen_name not in data:
                        data[screen_name] = {}
                    if chart_name not in data[screen_name]:
                        data[screen_name][chart_name] = {}
                    data[screen_name][chart_name][key] = name[key]

            with open(filename, "w") as fp:
                fp.write(json.dumps(data, default=self.default)+"\n")
        else:

            with open(filename, "w") as fp:
                fp.write(json.dumps(name, default=self.default)+"\n")

    def default(self, obj):
        """Default JSON serializer."""
        import calendar, datetime

        if isinstance(obj, datetime.datetime):
            if obj.utcoffset() is not None:
                obj = obj - obj.utcoffset()
            millis = int(
                calendar.timegm(obj.timetuple()) * 1000 +
                obj.microsecond / 1000
            )
            return millis
        if isinstance(obj, datetime.date):
            return str(obj)
        raise TypeError('Not sure how to serialize %s' % (obj,))