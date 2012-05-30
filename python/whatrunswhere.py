# -*- coding: utf-8 -*-

import requests
import urllib
import json


# Exception definitions
class APIError(Exception): pass


# Constants
API_URL = "http://api.whatrunswhere.com/v1/{req_type}/{domain}/{cmd}/"


class WhatRunsWhere(object):
    """ WhatRunsWhere API client """
    valid_filters = ['country', 'network', 'from_ts', 'until_ts']
    params = {}

    def __init__(self, auth_token):
        """ Constructor takes `auth_token` argument, which is the API token
        that you can find inside your account preference in the WRW site. """
        if not auth_token:
            raise APIError("No API token specified")
        self.params['token'] = auth_token

    def _api_call(self, req_type, domain, command):
        """ Makes the HTTP request to the WRW API.
        Returns dictionary of JSON API response. """
        base = API_URL.format(req_type=req_type, domain=domain, cmd=command)
        url = "{0}?{1}".format(base, urllib.urlencode(self.params))
        print "Requesting {0}".format(url)
        resp = requests.get(url).content
        json_data = json.loads(resp)
        if json_data['error']:
            raise APIError(json_data['error'])
        return json_data['data']

    def set_filter(self, filter_name, filter_value):
        if not filter_name in self.valid_filters:
            raise APIError("Invalid filter name: {0}".format(filter_name))
        if filter_value:
            self.params[filter_name] = filter_value
        else:
            del self.params[filter_name]

    # /advertiser functions
    def advertiser_overview(self, domain):
        return self._api_call("advertiser", domain, "overview")

    def advertiser_traffic_sources(self, domain):
        return self._api_call("advertiser", domain, "traffic_sources")

    def advertiser_ad_servers(self, domain):
        return self._api_call("advertiser", domain, "ad_servers")

    def advertiser_publishers(self, domain):
        return self._api_call("advertiser", domain, "publishers")

    def advertiser_related_domains(self, domain):
        return self._api_call("advertiser", domain, "related_domains")

    def advertiser_image_ads(self, domain):
        return self._api_call("advertiser", domain, "image_ads")

    def advertiser_flash_ads(self, domain):
        return self._api_call("advertiser", domain, "flash_ads")

    def advertiser_text_ads(self, domain):
        return self._api_call("advertiser", domain, "text_ads")

    def advertiser_hybrid_ads(self, domain):
        return self._api_call("advertiser", domain, "hybrid_ads")

    # /publisher functions
    def publisher_overview(self, domain):
        return self._api_call("publisher", domain, "overview")

    def publisher_traffic_sources(self, domain):
        return self._api_call("publisher", domain, "traffic_sources")

    def publisher_advertisers(self, domain):
        return self._api_call("publisher", domain, "advertisers")

    def publisher_iframe_domains(self, domain):
        return self._api_call("publisher", domain, "iframe_domains")

    def publisher_banner_hosts(self, domain):
        return self._api_call("publisher", domain, "banner_hosts")

    def publisher_image_ads(self, domain):
        return self._api_call("publisher", domain, "image_ads")

    def publisher_flash_ads(self, domain):
        return self._api_call("publisher", domain, "flash_ads")

    def publisher_text_ads(self, domain):
        return self._api_call("publisher", domain, "text_ads")

    def publisher_hybrid_ads(self, domain):
        return self._api_call("publisher", domain, "hybrid_ads")
