# Week 3: Creation of a Simple Network Topology Using Open-Source Network Virtualization Tools

## Objective
To create and configure simple network topologies using an open-source network virtualization tool (Mininet) and verify communication between the virtual network nodes.

## Environment & Prerequisites
* **Hypervisor:** VirtualBox
* **OS:** Ubuntu Linux Virtual Machine
* **Tool:** Mininet

## Part 1: Installation and Verification
First, i updated the package index and installed Mininet via the Ubuntu terminal:
```bash
sudo apt-get update
sudo apt-get install mininet
```
then verified the installation and ran a base communication test:
```bash
sudo mn --version
sudo mn --test pingall
```

---

## Part 2: Network Topology Configurations
As per the assignment requirements, i created five different types of topologies. For the configurable topologies, i tested two distinct node configurations, checked the links, verified connectivity using `pingall`, and safely stopped the network after each test using `sudo mn -c`.

### 1. Minimal Topology
The default configuration consisting of 1 switch and 2 hosts.
* **Start:** `sudo mn --topo minimal`
* **Test:** `pingall`
* **Clean:** `sudo mn -c`

### 2. Single Topology
A central switch connected to *k* hosts.
* **Configuration A (3 Hosts):**
  * **Start:** `sudo mn --topo single,3`
  * **Test:** `links`, `pingall`, then exit.
  * **Clean:** `sudo mn -c`
* **Configuration B (4 Hosts):**
  * **Start:** `sudo mn --topo single,4`
  * **Test:** `links`, `pingall`, then exit.
  * **Clean:** `sudo mn -c`

### 3. Linear Topology
A line of *k* switches, where each switch connects to the next and to exactly one host.
* **Configuration A (3 Nodes):**
  * **Start:** `sudo mn --topo linear,3`
  * **Test:** `pingall`, then exit.
  * **Clean:** `sudo mn -c`
* **Configuration B (4 Nodes):**
  * **Start:** `sudo mn --topo linear,4`
  * **Test:** `pingall`, then exit.
  * **Clean:** `sudo mn -c`

### 4. Tree Topology
A hierarchical structure.
* **Configuration A (Depth 3 - 7 switches, 8 hosts):**
  * **Start:** `sudo mn --topo tree,3`
  * **Test:** `links`, `pingall`, then exit.
  * **Clean:** `sudo mn -c`
* **Configuration B (Depth 2 - 3 switches, 4 hosts):**
  * **Start:** `sudo mn --topo tree,2`
  * **Test:** `links`, `pingall`, then exit.
  * **Clean:** `sudo mn -c`

### 5. Reversed Topology
Functionally equivalent to a tree or single topology, but the internal link connection ordering is reversed.
* **Configuration A (3 Hosts):**
  * **Start:** `sudo mn --topo reversed,3`
  * **Test:** `links`, `pingall`, then exit.
  * **Clean:** `sudo mn -c`
* **Configuration B (4 Hosts):**
  * **Start:** `sudo mn --topo reversed,4`
  * **Test:** `links`, `pingall`, then exit.
  * **Clean:** `sudo mn -c`

## Conclusion
All topologies were successfully generated. The `links` command confirmed proper connections, and the `pingall` tests consistently returned a `0% dropped` result, verifying full reachability and communication across all virtual network nodes.