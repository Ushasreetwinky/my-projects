"""Barc Video Integration."""

from video_api import get_video_url
import datetime as d
import json

def video_urls(*args):
    """Return list of video urls of all channels."""
    channels_mapping = {"BTV News": 1010591,
                        "NTV Telugu": 1010280,
                        "10 TV": 1010003,
                        "ABP News": 1010022,
                        "CNN News18": 1010071,
                        "ET Now": 1010118,
                        "CNBC TV 18": 1010068,
                        "Zee 24 Taas": 1010468,
                        "ABP Ananda": 1010020,
                        "ABP Asmita": 1010654
                        }
    start_time = d.datetime.now() - d.timedelta(days=1)
    end_time = d.datetime.now() - d.timedelta(days=1) + d.timedelta(hours=0.1)
    urls = {}
    for x in channels_mapping.values():
        url = get_video_url(x, start_time, end_time)
        if url is not None:
            urls[x] = url[0]['StreamUrl']
    return json.dumps(urls)

# print video_urls("")
