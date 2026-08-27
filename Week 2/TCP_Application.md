# Week 2: Client-Server Communication Between Two Virtual Machines

## Phase 1: Virtual Machine & Network Configuration
* Configured two Ubuntu Virtual Machines in VirtualBox.
* Created a NAT Network with an IPv4 Prefix of 10.0.2.0/24 and DHCP enabled.
* Attached both VMs to the NAT Network via Network settings and restarted them to apply changes.

## Phase 2: Connectivity & System Access
* Checked the IP addresses of both VMs using the `ip a` command.
* Tested network connectivity using the `ping` command to ensure packets were transmitted without loss.

## Phase 3: Workspace Preparation
* Created a dedicated project directory (`~/Desktop/lab2`) on both VMs to organize the application files.

## Phase 4: TCP Application Implementation
* Designated one VM as the Server and the other as the Client.
* Used the `nano` editor to script and save the server and client logic.
* Implemented the server-side logic in: `server.py`
* Implemented the client-side logic in: `client.py`

## Phase 5: Execution and Testing
* Established a connection between the two VMs by running the server script followed by the client script.
* Sent and received messages through the chat application to demonstrate two-way communication.