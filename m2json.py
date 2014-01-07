from google.appengine.ext import db
import datetime
import time

SIMPLE_TYPES = (int, long, float, bool, dict, basestring, list)

def to_dict(model):
    output = {}

    for key, prop in model.properties().iteritems():
        value = getattr(model, key)

        if value is None or isinstance(value, SIMPLE_TYPES):
            output[key] = value
        elif isinstance(value, datetime.date):
            # Convert date/datetime to MILLISECONDS-since-epoch (JS "new Date()").
            # ms = time.mktime(value.utctimetuple()) * 1000
            # ms += getattr(value, 'microseconds', 0) / 1000
            output[key] = str(value)
        # elif isinstance(value, db.GeoPt):
        #     output[key] = {'lat': value.lat, 'lon': value.lon}
        elif isinstance(value, db.Model):
            output[key] = to_dict(value)
        else:
            raise ValueError('cannot encode ' + repr(prop))

    return output

def gql_json_parser(query_obj):
    result = []
    for entry in query_obj:
        result.append(dict([(p, unicode(getattr(entry, p))) for p in entry.properties()]))
    return result

def get_milliseconds(value):
    ms = time.mktime(value.utctimetuple()) * 1000
    ms += getattr(value, 'microseconds', 0) / 1000
    return ms