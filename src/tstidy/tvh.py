# import json
import sys

import requests
from requests.auth import HTTPDigestAuth

import tstidy
from tstidy import errorExit, errorNotify, errorRaise


class TVHError(Exception):
    pass


def sendToTVH(route, data=None):
    """
    send a request to tvheadend
    """
    try:
        auth = HTTPDigestAuth(tstidy.tvhuser, tstidy.tvhpass)
        # print(f"{auth}")
        url = f"http://{tstidy.tvhipaddr}/api/{route}"
        # print(f"{url}")
        # return None
        r = requests.post(url, data=data, auth=auth)
        if r.status_code != 200:
            raise TVHError("error from tvh: {}".format(r))
        return r.json()
    except Exception as e:
        errorRaise(sys.exc_info()[2], e)


def getRecorded():
    try:
        route = "dvr/entry/grid_finished"
        recs = sendToTVH(route)
        tvrecs = [
            x for x in recs["entries"] if not x["channelname"].startswith("BBC Radio")
        ]
        radiorecs = [
            x for x in recs["entries"] if x["channelname"].startswith("BBC Radio")
        ]
        return tvrecs, radiorecs
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)


def deleteShow(show):
    try:
        route = "dvr/entry/remove"
        dat = {"uuid": show["uuid"]}
        junk = sendToTVH(route, data=dat)
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)
