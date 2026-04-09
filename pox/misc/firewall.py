from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

def _handle_ConnectionUp(event):
    log.info("Switch connected")

def _handle_PacketIn(event):
    packet = event.parsed

    print "Packet received at controller"

    if not packet:
        return

    #  BLOCK TCP
    if packet.find('tcp'):
        print "TCP BLOCKED"
        return

    #  ALLOW OTHER TRAFFIC
    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
    event.connection.send(msg)

def launch():
    log.info("Firewall Controller Started")
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
