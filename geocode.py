import requests
import json
from time import sleep

bing_maps_key = "AmQnuM6i5-v2Z1jM44W1OUVycySYZ_975GFp7vqKSZ9IqVW76bKThXgUujAfInq9"


def fail(location, status_code, reason, more_info=None):
    print("[Failure] [raising Exception] geocoding '%s' failed: error code '%d' ('%s') - [%s]" %
          (location, status_code, reason, more_info))
    raise Exception("geocoding '%s' failed: error code '%d' ('%s') - [%s]", location, status_code, reason, more_info)


def geocode_try(location):
    """
    @param location: name of a geocodable location - assumes a high quality geocoded result is available
    @return: lat, long of location -or- raise exception
    """
    request_url = "https:" + "//dev.virtualearth.net/REST/v1/Locations/" + location + "?key=" + bing_maps_key
    response = requests.get(request_url)

    if not response.ok:
        fail(location, response.status_code, response.reason)

    # print json.dumps(response.content)
    results = json.loads(response.content)[u'resourceSets'][0]
    resource_count = len(results[u'resources'])
    if resource_count == 0:
        fail(location, response.status_code, response.reason, 'no resources returned in response')
    confidence = results[u'resources'][0][u'confidence']
    confidence_high = confidence == u'High'
    if not confidence_high:
        fail(location, response.status_code, response.reason, '1st resource not high confidence: ' + confidence)
    coords = results[u'resources'][0][u'point'][u'coordinates']
    print("[geocoding] '%s' is at coordinates %s" % (location, coords))

    return coords[0], coords[1]


# Wraps real geocoder (geocode_try) to make retries easier
def geocode(location):
    max_try_count = 4
    seconds_delay_between_tries = 2.5
    try_count = 1

    for i in range(max_try_count):
        try:
            return geocode_try(location)
        except:
            if try_count >= max_try_count:
                raise
            else:
                try_count += 1
                print("Failed to geocode '%s', will retry %d more time(s)" % (location, max_try_count-try_count))
                sleep(seconds_delay_between_tries)



