# Classes for re-use

# Core library and/or django imports

# 3rd-party imports

# Local app imports

# Load the .env



############################

class make_faa_api_request:
    def __init__(self, station_id):
        self.station_id = station_id


    def request_result_all(self):
        # Needfuls
        import requests
        import urllib3
        import json
        import math

        # Disable SSL warnings
        urllib3.disable_warnings()

        # Base METAR query URL
        query_url = "https://www.aviationweather.gov/adds/dataserver_current/httpparam?datasource=metars&requestType=retrieve&format=xml&mostRecentForEachStation=constraint&hoursBeforeNow=1.25&stationString={}".format(self.station_id)

        # Final list to be returned if query is successful
        #faa_response_final = []

        # Initial query parameters
        #header = {'Authorization': 'Bearer {}'.format(self.bearer_token)}

        # Make the initial query
        try:
            faa_response = requests.get(query_url, verify=False)
            #faa_response = requests.get(query_url)

        except Exception as e:
            fail_message = "Failed to make initial request (1.1). Got HTTP response: {}".format(faa_response.status_code)
            return (fail_message, e)

        # Now check the HTTP status code
        # Some requests (e.g. Custom Fields) return '0' on success in the result content
        if faa_response.status_code == 200:
          
            # Return the data
            #faa_response_json = json.loads(faa_response.content)
            if faa_response:
                return (faa_response.status_code, faa_response.content)#, faa_response_json)
            else:
                return "what the fuck"


        # Got a 401, unauthorized
        elif faa_response.status_code == 401:
            # Return the code
            fail_message = "Failed to parse initial request (1.1). Got HTTP response: {}".format(faa_response.status_code)
            return (faa_response.status_code, fail_message)


        # Didn't get a 200 or a 401, so wtf
        else:
            fail_message = "Failed to parse initial request (1.2). Got HTTP response: {}".format(faa_response.status_code)
            return (faa_response.status_code, fail_message)

##########################



