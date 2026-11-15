# LAB 6: Familiarization and Usage of Cloud Services Using AWS and Open-Source Cloud Tools  

**Aim:** To become familiar with different cloud services and perform basic cloud operations using Amazon Web Services (AWS), Ubuntu Linux, Oracle VirtualBox, and the AWS Command Line Interface (CLI).

---

## Overview of Practical Tasks

| Task | What needs to be done? | How to demonstrate? |
| :--- | :--- | :--- |
| **1. Virtual Machine Setup** | Install Ubuntu using VirtualBox and execute basic Linux commands. | A working Ubuntu virtual machine and terminal output. |
| **2. Cloud Storage (S3)** | Create an Amazon S3 bucket, upload a file, view it, and download it. | Successful file upload and download in AWS S3. |
| **3. Cloud Service Exploration** | Explore IAM, EC2, and VPC through the AWS Console. | Understanding of cloud security, virtual machines, and networking. |
| **4. Cloud Monitoring & CLI** | Explore CloudWatch and execute basic AWS CLI commands. | Service metrics and successful command outputs. |

---

## Task 1: Virtual Machine (VM) Setup

### Step 1 & 2: Create VM & Install Ubuntu
1. Ensure Oracle VirtualBox is installed and your Ubuntu Linux Virtual Machine is created and running.
2. Log in to your Ubuntu desktop environment and open the **Ubuntu Terminal**.

### Step 3 & 4: Update Ubuntu & Install Basic Utilities
Run the following commands inside your **Ubuntu Terminal**:

```bash
sudo apt update
sudo apt upgrade -y
```

---

## Task 2A: Introduction to AWS Management Console

1. Open a web browser *(Tip: Open the browser **inside your Ubuntu VM** so you can easily upload files created in your Ubuntu terminal directly to AWS later)*.
2. Visit [https://console.aws.amazon.com/](https://console.aws.amazon.com/)
3. Sign in using your authorized AWS account.
4. Explore the AWS Management Console home page and locate the top **Search bar** used to find AWS services.

---

## Task 2B: Implementation of Cloud Storage Using Amazon S3

### Step 1: Open Amazon S3
1. In the AWS Management Console top search bar, search for **S3** and open **Amazon S3**.
2. Click **Create bucket**.

### Step 2: Create an S3 Bucket
1. **Bucket name:** Enter a globally unique name (only lowercase letters, numbers, and hyphens).  
   *Example:* `cse12045-cloud-lab6-student01` or `omgpleaseworkim`
2. **AWS Region:** Keep your default region selected (e.g., `ap-southeast-2`).
3. **Block Public Access:** Keep **Block all public access** enabled (checked). *Never make the bucket public for this experiment.*
4. **Bucket Versioning & Encryption:** Keep default encryption enabled.
5. Scroll down and click **Create bucket**.

### Step 3: Create a Sample File in Ubuntu
Open your **Ubuntu Terminal** (`argha@argha-VirtualBox`) and run:

```bash
mkdir -p ~/cloud-lab6
cd ~/cloud-lab6
echo "Cloud Computing Lab Experiment 6" > lab-note.txt
cat lab-note.txt
```
* **Expected Output:** `Cloud Computing Lab Experiment 6`

### Step 4: Upload the File to S3 (via Browser GUI)
1. In your browser (inside the Ubuntu VM), open the S3 bucket you created in Step 2.
2. Click **Upload** -> **Add files**.
3. Navigate to your `/home/argha/cloud-lab6/` folder (or wherever you created it) and select `lab-note.txt`.
4. Click **Upload** at the bottom of the page and verify `lab-note.txt` appears inside the bucket.

### Step 5: Download the File
1. Check the box next to `lab-note.txt` inside your S3 bucket.
2. Click **Download**.
3. Open the downloaded file and verify its contents match the original file.

### Step 6: Delete the Test Object *(Hold off on deleting the bucket until Task 4B is finished!)*
1. Select `lab-note.txt` in your S3 bucket, click **Delete**, type `permanently delete` in the confirmation box, and click **Delete objects**.
2. **Pro Tip:** Your manual says you can delete the bucket here, **but Task 4B Step 6 requires a bucket to upload via AWS CLI**. Keep your bucket alive until you finish Task 4B, or recreate it when you get to Task 4B!

---

## Task 3A: Identity and Access Management Using AWS IAM

> **Safety Note:** This is an observation activity only. Do not create users, generate access keys, or change policies without instructor approval.

### Step 1: Open IAM
1. Search for **IAM** in the AWS Console search bar and open the **IAM Dashboard**.
2. Click through the left navigation menu to observe **Users**, **User groups**, **Roles**, and **Policies**.

### Step 2 & 3: Understand IAM Policies & Least Privilege
Review this illustrative IAM Policy structure that adheres to the **Principle of Least Privilege** (granting only the minimum permissions required—in this case, only listing a specific bucket):

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:ListBucket"
      ],
      "Resource": "arn:aws:s3:::example-bucket"
    }
  ]
}
```
* **Version:** Policy language version.
* **Effect:** `Allow` or `Deny`.
* **Action:** Specific AWS operation allowed (`s3:ListBucket`).
* **Resource:** Specific AWS resource ARN the permission applies to.

---

## Task 3B: Virtual Machine Provisioning Using Amazon EC2

### Step 1 & 2: Open EC2 & Explore Instance Launch
1. Search for **EC2** in the AWS Console and open the **EC2 Dashboard**.
2. Click **Instances** in the left menu, then click **Launch instances**.
3. Observe the configuration steps without actually launching (unless instructed):
   * **Name and tags:** Enter an instance name (e.g., `Lab6-Test-VM`).
   * **Application and OS Images (AMI):** Explore available Linux/Ubuntu Amazon Machine Images.
   * **Instance type:** Observe available hardware sizes (e.g., `t2.micro` or `t3.micro`).
   * **Key pair (login):** Used for secure SSH authentication.
   * **Network settings:** Security group firewall rules (e.g., allowing SSH port 22).
   * **Configure storage:** Root EBS volume size (e.g., 8 GiB gp3).
4. **Stop at the review stage** and click **Cancel** (unless your instructor explicitly asked you to launch and terminate a Free Tier instance).

---

## Task 4A: Virtual Networking Using Amazon VPC

> **Note:** Do not modify or delete any default VPC resources during this observation exercise.

### Step 1 & 2: Open Amazon VPC & Explore Components
1. Search for **VPC** in the AWS Console and open the **VPC Dashboard**.
2. Click through the left sidebar and observe:
   * **Your VPCs:** Observe the default VPC CIDR block.
   * **Subnets:** Observe the available subnets across Availability Zones.
   * **Route tables:** Identify which VPC they belong to and how traffic is routed.
   * **Internet gateways:** Enables communication between the VPC and the internet.
   * **Security groups:** Observe the **Inbound rules** and **Outbound rules**.

---

## Task 3D: Cloud Monitoring Using Amazon CloudWatch

### Step 1, 2 & 3: Explore Metrics and Alarms
1. Search for **CloudWatch** in the AWS Console and open the **CloudWatch Dashboard**.
2. In the left menu, click **Metrics** -> **All metrics**:
   * Browse metrics organized by AWS service (e.g., S3 or EC2 CPU Utilization).
3. In the left menu, click **Alarms** -> **All alarms**:
   * Click **Create alarm** (to observe only—cancel before finishing) to see how a metric is chosen and a threshold condition (e.g., `CPUUtilization > 80%`) triggers a state change.

---

## Task 4B: Basic AWS Operations Using AWS CLI

> **CRITICAL TROUBLESHOOTING NOTE:**  
> **AWS CloudShell** runs on a remote Amazon server in your browser, **NOT** on your VirtualBox Ubuntu machine. Any file you want to upload using `aws s3 cp` in CloudShell **must be created inside CloudShell itself**! Follow every command below **inside the AWS CloudShell browser terminal**.

### Step 1: Open AWS CloudShell
1. In the top navigation bar of the AWS Management Console, click the **CloudShell icon** (`>_` icon near the top right).
2. Wait for the terminal environment to initialize (`~ $`).

### Step 2: Verify AWS CLI Installation
Run inside CloudShell:
```bash
aws --version
```

### Step 3: Verify AWS Account Identity
Run inside CloudShell:
```bash
aws sts get-caller-identity
```
*(Take a screenshot for your lab report if required, but do not post your Account ID publicly).*

### Step 4: List Available S3 Buckets (and Create One if Empty!)
Run inside CloudShell:
```bash
aws s3 ls
```
* **If `aws s3 ls` returns nothing** (because you deleted your bucket in Task 2B), create your bucket right now in CloudShell by running:
  ```bash
  aws s3 mb s3://omgpleaseworkim
  ```
  *(Replace `omgpleaseworkim` with your own unique bucket name if desired).*

### Step 5: Create a Local File Inside CloudShell
Run these exact commands **inside the AWS CloudShell terminal** (do not run them in VirtualBox):

```bash
mkdir -p ~/cloud-lab6-cli
cd ~/cloud-lab6-cli
echo "AWS CLI Cloud Storage Test" > sample.txt
ls -l
```
* Verify that `sample.txt` is listed in the output of `ls -l`.

### Step 6: Upload the File to S3
Still inside `~/cloud-lab6-cli` in CloudShell, run (replace `omgpleaseworkim` with your actual bucket name):

```bash
aws s3 cp sample.txt s3://omgpleaseworkim/sample.txt
```
* **Expected Output:** `upload: ./sample.txt to s3://omgpleaseworkim/sample.txt`

### Step 7: List Objects in the Bucket
```bash
aws s3 ls s3://omgpleaseworkim/
```
* **Expected Output:** Displays the timestamp, file size, and `sample.txt`.

### Step 8: Download the File from S3
```bash
aws s3 cp s3://omgpleaseworkim/sample.txt downloaded.txt
```
* **Expected Output:** `download: s3://omgpleaseworkim/sample.txt to ./downloaded.txt`

### Step 9: Verify the Downloaded File
```bash
cat downloaded.txt
```
* **Expected Output:** `AWS CLI Cloud Storage Test`

### Step 10: Delete the Test Object and Clean Up Bucket
Delete the uploaded object from S3:
```bash
aws s3 rm s3://omgpleaseworkim/sample.txt
```
Once your lab screenshots are taken and you are completely done with the experiment, delete the empty test bucket so no resources remain active:
```bash
aws s3 rb s3://omgpleaseworkim
```

---

## Final Lab Cleanup & Cost Precautions Checklist
- [ ] Verify that your test S3 bucket and all objects inside it have been deleted (`aws s3 ls` should return empty).
- [ ] If you launched an optional EC2 instance, verify it is **Terminated** and no EBS volumes or Elastic IPs remain.
- [ ] Check the **AWS Billing and Cost Management Dashboard** to confirm no unexpected billable services are running.
- [ ] Never share secret access keys, session tokens, or root credentials in your lab report.