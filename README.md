WhatRunsWhere.com API Reference
===============================

Introduction
-------------------------------
The WhatRunsWhere API provides a programmatic interface to the extensive
WhatRunsWhere advertising intelligence dataset.


Authentication
-------------------------------
You must use your account's API token to access the WRW API.  This token
can be found in the account settings panel on the WRW web site.  Attempts
to access the API without a valid API token are actively monitored.  To 
obtain a new API token please contact customer service.

Display vs. Mobile
-------------------------------
The main product, search.whatrunswhere.com, returns data for display and
search advertising.  The mobile.whatrunswhere.com site returns data for
Mobile Web and Android-based advertisements.  In order to use the mobile
data, your account must be specifically authorized to do so.  The requests
are of the same format as the display side, except the extra `mobile` 
filter is used to indicate that you want mobile data for your query.

Request Format
-------------------------------
Requests to the API are standard HTTP `GET` requests.  Each request contains 
three essential elements: resource type, resource, and attribute.  Requests 
are formed by adding these elements to the API base URL path, which is 
`http://api.whatrunswhere.com/v1`.

For example, to request the text ads for advertiser **landingpage.com**
the request would look like:

`/advertiser/landingpage.com/text_ads/`

The full request URL would be:

`http://api.whatrunswhere.com/v1/advertiser/landingpage.com/text_ads/?token=XXX`

In this case, `advertiser` is the resource type, `landingpage.com` is the 
specific resource of that type, and `text_ads` is the type of attribute you are 
seeking.  `XXX` should be replaced with your API token.

The available resource types are split into two categories.

+ **WHERE**: To find out where a domain is advertising, use the `advertiser` resource
type.  To find out who is advertising on a domain, use the `publisher` resource.

+ **WHAT**: You can also find information about specific ads themselves.  Each ad type 
has its own resource type: `image_ad`, `flash_ad`, `text_ad`, `hybrid_ad`.


Additional Parameters ("Filters")
-------------------------------
Additional parameters are specified as standard HTTP parameters.  Some 
parameters, like `token`, are always required.  However, there are also 
optional parameters that you may use to filter the results of the API
response.  The complete list of parameters is:

+ `token` (**required**) - Your WRW API token 
+ `country` - URL-encoded string of the country name 
+ `network` - URL-encoded string of the ad network name
+ `from_ts` - Return only data newer than this UNIX timestamp
+ `until_ts` - Return only data older than this UNIX timestamp
+ `advertiser` - Return only data matching this advertiser (when searching by publisher)
+ `publisher` - Return only data matching this publisher/placement (when searching by advertiser)
+ `mobile` - "true" to seek mobile data; any value other than "true" indicates "false"

You can omit or submit as blank data any parameter that is not required.  For 
example, the following parameters are valid:

+ `/advertiser/landingpage.com/text_ads?token=XXX`
+ `/advertiser/landingpage.com/text_ads?token=XXX&country=United%20States`
+ `/advertiser/landingpage.com/text_ads?token=XXX&country=`

The `advertiser` and `publisher` filters are used to limit data to specific domains.  They
can only be used opposite each other, i.e.:
+ `/advertiser/landingpage.com/text_ads?token=XXX&publisher=pagewithads.com`
+ `/publisher/apublisher.com/text_ads?token=XXX&advertiser=landingpage.com`

However, the following requests are **not valid**, since they are missing the 
required `token` parameter:

+ `/advertiser/landingpage.com/text_ads`
+ `/advertiser/landingpage.com/text_ads?country=United%20States`


Response Format
-------------------------------
Responses from the API are returned in JSON format.  A response will always 
contain the following elements:

    {
    'error': ERROR_MESSAGE,
    'data': RESPONSE_DATA
    }

`RESPONSE_DATA` contains the actual data in the response, or returns `null` if
no data is available.

`ERROR_MESSAGE` will always return `null`, except when an error has occurred.

See the provided code examples for the recommended way to handle responses.

_Note: All date/time fields in responses are in UNIX timestamp format._


API Functions Reference
===============================

Advertisers
-------------------------------

### Advertiser Overview
`/advertiser/{domain}/overview/`
Returns information regarding the length of the advertiser's campaigns and 
the frequency with which they target different countries.

### Advertiser Traffic Sources (Networks)
`/advertiser/{domain}/traffic_sources/`
Returns the ad networks that the advertiser used to bring traffic to their site.

### Advertiser Publishers (Placements)
`/advertiser/{domain}/publishers/`
Returns a list of publishers and associated ad placements where ads for this 
advertiser were found.

### Advertiser Ad Servers
`/advertiser/{domain}/ad_servers`
Returns a list of ad servers that were hosting the advertiser's ad data.

### Advertiser Landing Pages
`/advertiser/{domain}/landing_pages`
Returns a list of complete URLs that the advertiser's ads point to.

### Advertiser Related Domains
`/advertiser/{domain}/related_domains`
Returns a list of related domains that may be associated with the specified
advertiser.  This data is based on the similarity of analytics tracking tags
and IP addresses.

_Note: This call does not support optional filtering parameters._

### Advertiser Image Ads
`/advertiser/{domain}/image_ads/`
Returns a list of image ads used by the advertiser.

### Advertiser Flash Ads
`/advertiser/{domain}/flash_ads/`
Returns a list of flash ads used by the advertiser.

### Advertiser Text Ads 
`/advertiser/{domain}/text_ads/`
Returns a list of text ads used by the advertiser.

### Advertiser Hybrid Ads 
`/advertiser/{domain}/hybrid_ads/`
Returns a list of hybrid (containing text and image) ads used by the advertiser.


Publishers
-------------------------------
### Publisher Overview
`/publisher/{domain}/overview/`
Returns information about campaigns running on this domain.

### Publisher Traffic Sources
`/publisher/{domain}/traffic_sources/`
Returns a list of networks seen advertising on this domain.

### Publisher Advertisers
`/publisher/{domain}/advertisers/`
Returns a list of advertisers whose ad placements were seen on this domain.

### IFrame Domains
`/publisher/{domain}/iframe_domains/`
Returns a list of ad tags that were found on this domain.

### Banner Hosts
`/publisher/{domain}/banner_hosts/`
Returns a list of hosts that were found hosting ad resources on this domain.


### Publisher Image Ads
`/publisher/{domain}/image_ads/`
Returns a list of image ads used by the publisher.

### Publisher Flash Ads
`/publisher/{domain}/flash_ads/`
Returns a list of flash ads used by the publisher.

### Publisher Text Ads 
`/publisher/{domain}/text_ads/`
Returns a list of text ads used by the publisher.

### Publisher Hybrid Ads 
`/publisher/{domain}/hybrid_ads/`
Returns a list of hybrid (containing text and image) ads used by the publisher.



Ad data 
-------------------------------
### Ad Types 
There are four ad types: `image_ad`, `flash_ad`, `text_ad`, and `hybrid_ad`. 
Each ad in the system is identified by an ad type and an MD5 hash.  To request 
an ad object you format a request like `/image_ad/MD5_HASH/`, where `MD5_HASH`
is the ad's unique MD5 hash identifier.  _Please note that an attribute field 
is not required to request an ad object._

When you receive data for a banner or flash ad, there will be a filename 
included along with the dimensions of the ad.  To retrieve the actual image
or SWF file, prefix the filename with `http://assets.whatrunswhere.com/banners/`
and make an HTTP `GET` request for the file.

### Ad Landing Pages
The only valid attribute for a specific request to an ad object is 
`landing_pages`.  The request should look like `/image_ad/MD5_HASH/landing_pages`. 
This will return a list of landing pages that were linked to by the advertiser 
using this ad.
