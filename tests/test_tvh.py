from tstidy import setConfig
from tstidy.tvh import getRecorded


def test_getRecorded():
    setConfig()
    tvrecs, radiorecs = getRecorded()
    assert len(tvrecs) > 0
    assert len(radiorecs) > 0
