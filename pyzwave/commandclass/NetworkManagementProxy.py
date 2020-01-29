from pyzwave.const.ZW_classcmd import (
    COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY,
    NODE_INFO_CACHED_GET,
    NODE_INFO_CACHED_REPORT,
    NODE_LIST_GET,
    NODE_LIST_REPORT,
)
from pyzwave.message import Message
from pyzwave.types import BitStreamReader, bits_t, bytes_t, flag_t, reserved_t, uint8_t
from . import ZWaveMessage, registerCmdClass

registerCmdClass(COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY, "NETWORK_MANAGEMENT_PROXY")


class NodeList(set):
    """Deserializer for nodelist returned in NODE_LIST_REPORT"""

    @classmethod
    def deserialize(cls, stream: BitStreamReader):
        """Deserialize nodes from stream"""
        nodeList = cls()
        for i in range(28):
            nodeByte = uint8_t.deserialize(stream)
            for j in range(8):
                if nodeByte & (1 << j):
                    nodeList.add(i * 8 + j + 1)
        return nodeList


@ZWaveMessage(COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY, NODE_INFO_CACHED_GET)
class NodeInfoCachedGet(Message):
    """Command Class message COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY NODE_INFO_CACHED_GET"""

    NAME = "NODE_INFO_CACHED_GET"

    attributes = (
        ("seqNo", uint8_t),
        ("-", reserved_t(4)),
        ("maxAge", bits_t(4)),
        ("nodeID", uint8_t),
    )


@ZWaveMessage(COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY, NODE_INFO_CACHED_REPORT)
class NodeInfoCachedReport(Message):
    """Command Class message COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY NODE_INFO_CACHED_REPORT"""

    NAME = "NODE_INFO_CACHED_REPORT"

    attributes = (
        ("seqNo", uint8_t),
        ("status", bits_t(4)),
        ("age", bits_t(4)),
        ("listening", flag_t),
        ("zwaveProtocolSpecific", reserved_t(7)),
        ("optFunc", flag_t),
        ("zwaveProtocolSpecific", reserved_t(7)),
        ("-", reserved_t(8)),
        ("basicDeviceClass", uint8_t),
        ("genericDeviceClass", uint8_t),
        ("specificDeviceClass", uint8_t),
        ("commandClass", bytes_t),
    )


@ZWaveMessage(COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY, NODE_LIST_GET)
class NodeListGet(Message):
    """Command Class message COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY NODE_LIST_GET"""

    NAME = "NODE_LIST_GET"

    attributes = (("seqNo", uint8_t),)


@ZWaveMessage(COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY, NODE_LIST_REPORT)
class NodeListReport(Message):
    """Command Class message COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY NODE_LIST_REPORT"""

    NAME = "NODE_LIST_REPORT"

    attributes = (
        ("seqNo", uint8_t),
        ("status", uint8_t),
        ("nodeListControllerId", uint8_t),
        ("nodes", NodeList),
    )
