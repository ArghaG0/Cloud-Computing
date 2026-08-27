# Week 1: Ubuntu Virtual Machine Setup & Troubleshooting Guide

## 1. Virtual Machine Configuration
- **Hypervisor:** Oracle VirtualBox
- **OS:** Ubuntu 26.04 (64-bit)
- **RAM:** 4096 MB (4 GB)
- **CPU:** 3 Cores
- **Storage:** 25 GB VDI (VirtualBox Disk Image)

## 2. Troubleshooting Steps

### Issue 1: Installer Crash
- **Symptom:** The installer crashed during the final system setup phase when trying to configure adcli.
- **Fix:** Disconnected the VirtualBox Network Adapter (set to "Not attached") during the installation phase to bypass network-dependent package failures.

### Issue 2: rsync Data Stream Error
- **Symptom:** Failed during curtin extract phase with rsync error in rsync protocol data stream.
- **Fix:** Ensured the Ubuntu ISO was properly mounted to the IDE controller, wiped the broken partitions, and selected Erase disk and install Ubuntu for a clean installation.

### Issue 3: Graphics Controller Conflict
- **Symptom:** System booted into a text screen displaying vmwgfx seems to be running on an unsupported hypervisor.
- **Fix:** Navigated to VM Settings > Display. Changed the Graphics Controller to VBoxSVGA, maxed Video Memory to 128MB, and disabled 3D Acceleration to force a clean software render.

### Issue 4: Black Screen & Windows Hypervisor Conflict
- **Symptom:** The VM would freeze on a black screen after the kernel logs.
- **Fix:** Disabled Windows Hyper-V and Core Isolation on the host machine using the command prompt: bcdedit /set hypervisorlaunchtype off. Rebooted the host PC to allow VirtualBox native access.

## 3. Finalizing Installation
After resolving the hypervisor and display issues, the Ubuntu 26.04 installation completed successfully.

## 4. Post-Installation: Build Tools and Kernel Headers
Once booted into the new Ubuntu environment, the network adapter was re-enabled (NAT). The final task was to install the prerequisite build tools for C compilation and kernel development.

```bash
sudo apt update
sudo apt install -y build-essential linux-headers-$(uname -r)