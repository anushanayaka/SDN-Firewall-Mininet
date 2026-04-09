# SDN Firewall using POX and Mininet

## Objective
To implement a firewall using SDN controller (POX) that blocks TCP traffic and allows ICMP.

## Tools Used
- Mininet
- POX Controller
- OpenFlow Protocol

## Features
- PacketIn handling
- Match-Action logic
- TCP traffic blocking
- ICMP (ping) allowed

## Topology
Single switch topology with 2 hosts (h1, h2)

## How to Run

### Step 1: Run Controller
python2.7 pox.py misc.firewall

### Step 2: Run Mininet
sudo mn --controller=remote,ip=127.0.0.1 --switch ovs,protocols=OpenFlow10

### Step 3: Test

Ping (Allowed):
h1 ping h2

TCP (Blocked):
h1 iperf -s &
h2 iperf -c h1

## Output
- Packet received at controller
- TCP BLOCKED

## Conclusion
Successfully implemented SDN firewall using POX controller with match-action rules.

 Output Screenshots

  CONTROLLER OUTPUT
  <img width="511" height="305" alt="image" src="https://github.com/user-attachments/assets/aeb59ea8-5bae-42e8-8022-5a832ec5910e" />
  PING TEST
  <img width="457" height="198" alt="image" src="https://github.com/user-attachments/assets/3e3cfb19-a98a-4591-92ba-459005b27cf6" />
  TCP BLOCKING
  <img width="423" height="174" alt="image" src="https://github.com/user-attachments/assets/491dd204-1756-48d5-81e1-6c79145d3e47" />
  <img width="258" height="219" alt="image" src="https://github.com/user-attachments/assets/234d6b9f-bb28-4b25-bc0d-be0c46b73169" />





