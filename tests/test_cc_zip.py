from pyzwave.commandclass import Zip
from pyzwave.message import Message


def test_zip_packet():
    pkt = b"#\x02\x80P\x02\x00\x00R\x01\x02"
    msg = Message.decode(pkt)
    assert isinstance(msg, Zip.ZipPacket)
    assert msg.ackRequest == True
    assert msg.ackResponse == False
    assert msg.nackResponse == False
    assert msg.nackWaiting == False
    assert msg.nackQueueFull == False
    assert msg.nackOptionError == False
    assert msg.headerExtIncluded == False
    assert msg.zwCmdIncluded == True
    assert msg.moreInformation == False
    assert msg.secureOrigin == True
    assert msg.seqNo == 2
    assert msg.ackRequest == True
    assert msg.sourceEP == 0
    assert msg.destEP == 0
    assert msg.compose() == pkt
