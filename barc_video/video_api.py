"""Barc TV integration."""

from zeep import Client
import datetime as d

"""Client initialization."""
client = Client(
    "http://barc.clearhub.tv/Teleview/api/TeleviewStreamService.svc?wsdl")


def get_video_url(channel_code, start_time, end_time):
    """Provide video url."""
    try:
        """Create a login session."""
        session = client.service.Login('teleview', 'br0adca$t')
        url = client.service.GetClip(
            session['SessionId'], channel_code, start_time, end_time)
        client.service.Logout(session['SessionId'])
        return url
    except Exception:
        return None


if __name__ == "__main__":
    """Use the list below for getting the channel codes.
    BTV News - 1010591
    NTV Telugu - 1010280
    10 TV - 1010003
    ABP News - 1010022
    CNN News18 - 1010071
    ET Now - 1010118
    CNBC TV 18 - 1010068
    Zee 24 Taas - 1010468
    ABP Ananda - 1010020
    ABP Asmita - 1010654
    """
    start_time = d.datetime.now() - d.timedelta(days=1)
    end_time = d.datetime.now() - d.timedelta(days=1) + d.timedelta(hours=0.1)
    print start_time, end_time
    urls1 = get_video_url(1010118, start_time, end_time)
    print urls1
    urls2 = get_video_url(1010591, start_time, end_time)
    print urls2
    urls3 = get_video_url(1010280, start_time, end_time)
    print urls3
    urls4 = get_video_url(1010003, start_time, end_time)
    print urls4
