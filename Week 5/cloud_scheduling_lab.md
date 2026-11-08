# Week 5 — Cloud Scheduling

A structured step-by-step setup, configuration, and execution guide for simulating Virtual Machine (VM) and Cloudlet scheduling policies using **CloudSim Plus** on Ubuntu.

---

## 1. System Update & Prerequisites

Refresh Ubuntu's local package index, install pending system updates, and set up OpenJDK 17, Apache Maven, and Git.

### 1.1 Update Ubuntu
```bash
sudo apt update
sudo apt upgrade -y
```
- `apt update`: Synchronizes package lists from upstream repositories.
- `apt upgrade -y`: Upgrades installed packages to their latest versions automatically.

### 1.2 Install Java 17, Maven & Git
```bash
sudo apt install openjdk-17-jdk maven git -y
```
- Installs the Java Development Kit (compiler and runtime), the Maven build manager, and Git version control.

### 1.3 Verify Toolchain Installation
```bash
java -version
javac -version
mvn -version
git --version
```
- **Check:** `java` and `javac` must report version `17.x`.
- **Check:** `mvn -version` must confirm it is running on Java 17. Resolve any version discrepancies using `update-alternatives --config java` before proceeding.

---

## 2. Directory Structure Setup

Set up the standard Maven project directory hierarchy:

```bash
mkdir -p ~/CloudSchedulingLab/src/main/java/lab
cd ~/CloudSchedulingLab
```
- `-p`: Recursively creates parent directories if they do not exist.
- Standard Maven path structure: `src/main/java/<package_name>/`.

---

## 3. Maven Configuration (`pom.xml`)

Open or create the project definition file in the project root:

```bash
nano pom.xml
```

### Configuration Requirements
Configure `pom.xml` with the following parameters:
- **Model Version:** `4.0.0`
- **Coordinates:** Group ID `lab`, Artifact ID `cloud-scheduling-lab`, Version `1.0-SNAPSHOT`
- **Compiler Release Properties:** Set `<maven.compiler.release>` to `17` and `<project.build.sourceEncoding>` to `UTF-8`
- **Dependencies:** Add `org.cloudsimplus:cloudsimplus:8.5.5`

> **Note on Lab Sheet Formatting Issues:**  
> Ensure no stray lab header/footer text (e.g., `CSE12045 | CLOUD COMPUTING LAB...`) is accidentally pasted inside XML attribute tags. Every tag must be properly formed and closed.

### Resolve Dependencies & Clean
```bash
mvn dependency:resolve
mvn clean
```
- `dependency:resolve`: Downloads CloudSim Plus and transitive libraries into `~/.m2/repository`.
- `clean`: Removes prior target builds to ensure a clean slate.

---

## 4. Experiment Implementation (`SchedulingExperiment.java`)

Create the experiment runner source file:

```bash
nano src/main/java/lab/SchedulingExperiment.java
```

### 4.1 Simulation Design & Scenarios
The experiment compares four distinct scheduling policy combinations across VM allocation and Cloudlet execution:

| Scenario | VM Scheduling Policy (`VmScheduler`) | Cloudlet Scheduling Policy (`CloudletScheduler`) | Description |
| :--- | :--- | :--- | :--- |
| **A** | `VmSchedulerSpaceShared` | `CloudletSchedulerSpaceShared` | Dedicated PEs to VMs; Cloudlets queue sequentially. |
| **B** | `VmSchedulerSpaceShared` | `CloudletSchedulerTimeShared` | Dedicated PEs to VMs; Cloudlets share VM capacity concurrently. |
| **C** | `VmSchedulerTimeShared` | `CloudletSchedulerSpaceShared` | Time-sliced host PEs across VMs; Cloudlets queue on VMs. |
| **D** | `VmSchedulerTimeShared` | `CloudletSchedulerTimeShared` | Full concurrent resource sharing at both host and VM levels. |

### 4.2 Architecture Implementation Points
Refer to the required simulation components:
- **Package & Imports:** Must reside in package `lab` and import required classes from `org.cloudbus.cloudsim.*`.
- **Constants:**
  - `HOST_PES`: 4
  - `VM_COUNT`: 2
  - `CLOUDLET_COUNT`: 4
  - `MIPS`: 1000
  - `CLOUDLET_LENGTH`: 20000
- **Datacenter Creation (`createDatacenter`):**
  - Creates a list of `PeSimple` matching `HOST_PES`.
  - Configures a `HostSimple` with 8 GB RAM, 100k BW, 1M Storage, and Simple Provisioners.
  - Attaches the selected `VmScheduler` to the host.
- **VM Allocation (`createVms`):**
  - Builds 2 VMs, each requesting 2 PEs, 2048 MB RAM, and 10 Gbps BW.
  - **Critical Requirement:** Instantiate a separate `CloudletScheduler` instance for each VM (e.g., using a supplier or fresh instantiation per loop iteration) rather than assigning one shared instance to multiple VMs.
- **Cloudlets (`createCloudlets`):**
  - Generates 4 tasks with length `20000`, 1 PE requirement, and `UtilizationModelFull`.
- **Execution & Output (`runScenario`):**
  - Submits entities to `DatacenterBrokerSimple`, starts the simulation, and prints a formatted summary table containing `Cloudlet ID`, `VM ID`, `Status`, `Start Time`, and `Finish Time`.

---

## 5. Build & Execution

### 5.1 Compile
```bash
mvn clean compile
```
- Compiles source code in `src/main/java/` against resolved classpath dependencies.

### 5.2 Execute
Run the simulation via the Maven Exec Plugin:
```bash
mvn exec:java -Dexec.mainClass="lab.SchedulingExperiment" -Dexec.classpathScope=compile
```

If the plugin prefix is unmapped or fails to resolve, invoke the plugin by its fully qualified descriptor:
```bash
mvn org.codehaus.mojo:exec-maven-plugin:3.5.0:java -Dexec.mainClass="lab.SchedulingExperiment" -Dexec.classpathScope=compile
```

---

## 6. Common Pitfalls & Solutions

| Error | Root Cause | Solution |
| :--- | :--- | :--- |
| `Non-parseable POM ... expected = after attribute name` | PDF header/footer copied into `pom.xml`. | Inspect line indicated in error (e.g. line 3) and remove extra text like `CSE12045`. |
| `package org.cloudbus.cloudsim... does not exist` | Missing or unresolved `cloudsimplus` dependency in `pom.xml`. | Check the `<dependencies>` block in `pom.xml` and rerun `mvn dependency:resolve`. |
| `CloudletScheduler already has a Vm assigned to it` | Sharing a single `CloudletScheduler` object instance across multiple VMs. | Instantiate a new scheduler instance inside the VM creation loop for each VM. |