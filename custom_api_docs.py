# custom_api_docs.py
CUSTOM_API_DOCS = {
    "url": "https://wsgx.cisco.com/wwchannels/services/external/getData",
    "method": "POST",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "Basic ZGlzdGlfc2VydmljZXMuZ2VuOkQhc3RyaWJ1dDFu",
    },
    "payload": {
        "service": "getRessellerData",
        "ccoId": "rubend@synnex.com",
        "profileId": "975",
        "entity": [
            {
                "sourceName": "COMSTOR",
                "resellerAccNo": "",
                "soldToName": "",
                "partnerName": "24/7 NETWORKS LLC",
                "city": "",
                "state": "",
                "postalCode": "",
                "country": "USA",
                "specialization": "",
                "certification": "",
                "authorization": "",
                "theaterCode": "USA",
                "partnerType": "",
                "partnerSiteid": "",
                "pageNumber": 1,
                "pageSize": 50,
            }
        ],
    },
}

