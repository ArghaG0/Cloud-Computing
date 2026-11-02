# Week 4: Software-Defined Networking (SDN) - Mininet, Open vSwitch & Ryu Controller

This repository documents the setup, troubleshooting, and execution of a Software-Defined Networking (SDN) environment on Ubuntu Linux using **Mininet**, **Open vSwitch (OVS)**, and the **Ryu SDN Controller** (OpenFlow 1.3). 

It also includes patches for installing and running `ryu` on modern Python environments (**Python 3.14+**), resolving legacy `setuptools` build isolation failures and `eventlet.wsgi` import deprecations.

---

## Architecture & Prerequisites

* **OS:** Ubuntu Linux (VirtualBox VM)
* **Network Emulator:** Mininet
* **Virtual Switch:** Open vSwitch (`openvswitch-switch`)
* **SDN Controller:** Ryu (`ryu-manager 4.34` running `simple_switch_13`)
* **Python Environment:** Python 3.14 (`venv`)

---

## Part 1: Environment Setup & Installation

### 1. Update Ubuntu
Update the package lists and upgrade existing system packages:
```bash
sudo apt update && sudo apt upgrade -y
```

### 2. Install Mininet
Install Mininet for creating virtual network topologies:
```bash
sudo apt install mininet -y
```

### 3. Install Open vSwitch
Install the software-based OpenFlow SDN switch:
```bash
sudo apt install openvswitch-switch -y
```

### 4. Verify Open vSwitch Service
Confirm that the Open vSwitch daemon is active and running:
```bash
sudo systemctl status openvswitch-switch
```

### 5. Verify Base Mininet Functionality
Launch a default Mininet topology to verify host and switch creation:
```bash
sudo mn
```
Inside the `mininet>` CLI, verify the nodes and test connectivity:
```text
mininet> nodes
mininet> pingall
mininet> exit
```

---

## Part 2: Ryu SDN Controller Installation & Python 3.14 Troubleshooting

### 6. Install Python and Virtual Environment Tools
Install `pip` and `venv` support:
```bash
sudo apt install python3-pip python3-venv -y
```

### 7. Create and Activate the Ryu Virtual Environment
Create an isolated virtual environment (`ryu-env`) and activate it:
```bash
python3 -m venv ryu-env
source ryu-env/bin/activate
```

### 8. Install Ryu (with Python 3.14 Compatibility Fixes)

Attempting a standard `pip install ryu` on modern Python/Ubuntu environments fails due to two legacy incompatibilities in Ryu (`4.34`). Follow the steps below to resolve both.

#### Issue A: `AttributeError: 'types.SimpleNamespace' object has no attribute 'get_script_args'`
* **Cause:** `pip` uses isolated build environments with the latest `setuptools` (v68+), which removed `easy_install.get_script_args` required by Ryu's setup hooks.
* **Fix:** Downgrade `setuptools` below version 68 and disable build isolation when installing `ryu`:

```bash
pip install "setuptools<68" wheel
pip install --no-build-isolation ryu
```

#### Issue B: `ImportError: cannot import name 'ALREADY_HANDLED' from 'eventlet.wsgi'`
* **Cause:** Modern `eventlet` versions (`0.31.0+`) required for Python 3.14 compatibility removed the private `ALREADY_HANDLED` attribute from `eventlet.wsgi`, causing `ryu-manager` to crash on startup.
* **Fix:** Patch `ryu/app/wsgi.py` inside the virtual environment to fall back to `object()` when `ALREADY_HANDLED` is not exported:

```bash
sed -i 's/from eventlet.wsgi import ALREADY_HANDLED/ALREADY_HANDLED = getattr(__import__("eventlet.wsgi").wsgi, "ALREADY_HANDLED", object())/' ~/ryu-env/lib/python3.14/site-packages/ryu/app/wsgi.py
```

### 9. Test Ryu Installation
Verify that `ryu-manager` executes properly:
```bash
ryu-manager --version
```
**Expected Output:**
```text
ryu-manager 4.34
```

---

## Part 3: Running the SDN Topology & Traffic Filtering

### 10. Start the Ryu Controller (Terminal 1)
Start `ryu-manager` with the OpenFlow 1.3 Simple Switch application:
```bash
ryu-manager ryu.app.simple_switch_13
```
**Expected Output:**
```text
loading app ryu.app.simple_switch_13
loading app ryu.controller.ofp_handler
instantiating app ryu.app.simple_switch_13 of SimpleSwitch13
instantiating app ryu.controller.ofp_handler of OFPHandler
```
> **Note:** Keep this terminal open so the controller remains active in the foreground.

### 11. Create the Mininet SDN Topology (Terminal 2)
Open a **new terminal window** and create a topology with 3 virtual hosts (`h1`, `h2`, `h3`) connected to a single Open vSwitch (`s1`) managed by the remote Ryu controller:
```bash
sudo mn --topo single,3 --controller=remote --switch ovsk
```

### 12. Inspect Available Nodes
Inside the `mininet>` prompt, list all network nodes (`h1`, `h2`, `h3`, `s1`, `c0`):
```text
mininet> nodes
```

### 13. Inspect Network Links
View the port mappings connecting the hosts to switch `s1`:
```text
mininet> net
```

### 14. Test Initial Host Connectivity
Verify that the Ryu controller dynamically installs L2 forwarding rules to allow communication between all hosts:
```text
mininet> pingall
mininet> h1 ping -c 4 h2
```

---

## Part 4: OpenFlow Flow Table Inspection & Packet Filtering

### 15. View Installed OpenFlow Rules (Terminal 3)
Open a **third terminal window** and dump the active OpenFlow 1.3 flow entries installed on switch `s1`:
```bash
sudo ovs-ofctl -O OpenFlow13 dump-flows s1
```

### 16. Add a Traffic Filtering Rule (Drop Port 1 Ingress)
Insert a higher-priority OpenFlow rule (`priority=100`) on switch `s1` to drop all packets entering through port 1 (`h1`):
```bash
sudo ovs-ofctl -O OpenFlow13 add-flow s1 "priority=100,in_port=1,actions=drop"
```

### 17. Verify the Filtering Rule
Return to **Terminal 2 (`mininet>`)** and attempt to ping `h2` from `h1`:
```text
mininet> h1 ping -c 4 h2
```
* **Observation:** 100% packet loss occurs because traffic entering `s1` on `in_port=1` matches the `priority=100` drop rule before reaching the reactive forwarding rules.

### 18. Remove Flow Rules
Return to **Terminal 3** and clear the flow table on switch `s1`:
```bash
sudo ovs-ofctl -O OpenFlow13 del-flows s1
```

### 19. Clean Up the Mininet Environment
Exit the Mininet CLI (`mininet> exit`) and clean up all virtual interfaces, switches, and lingering namespaces:
```bash
sudo mn -c
```

---

## Result

The SDN environment was successfully created using **Mininet**, **Open vSwitch**, and the **Ryu Controller** on Ubuntu with Python 3.14. Compatibility issues with modern `setuptools` and `eventlet` were resolved, and both reactive Layer-2 packet forwarding and OpenFlow 1.3 flow-table traffic filtering (`actions=drop`) were demonstrated.