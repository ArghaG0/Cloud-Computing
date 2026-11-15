# CLOUD COMPUTING LAB 7: Step-by-Step Practical Guide

**Experiment 7:** Familiarization and Usage of Collaborative Applications (SaaS)

**Aim:** To become familiar with Software as a Service (SaaS) and perform basic collaborative activities using cloud-based productivity and communication applications (such as Google Workspace or Microsoft 365).

---

## Overview of Practical Tasks

| Task | What needs to be done? | How to demonstrate? |
| :--- | :--- | :--- |
| **1. SaaS Introduction & Account Setup** | Explore the concept of SaaS and access a cloud-based collaborative application using an authorized account. | Successful login and identification of SaaS features. |
| **2. Cloud Document Collaboration** | Create, edit, share, and collaboratively modify an online document. | Shared document with evidence of collaborative editing, comments, and version history. |
| **3. Cloud Spreadsheet Collaboration** | Create and share an online spreadsheet and perform basic collaborative data operations. | Shared spreadsheet showing data entry, formulas, and collaborative editing. |
| **4. Online Presentation & Communication** | Create a cloud-based presentation and explore online communication/collaboration features. | Shared presentation and demonstration of collaborative features. |

> **Pro Tip for Solo Testing:** If you do not have a lab partner immediately available to act as your collaborator, you can share the files with a **secondary email account of your own** (opened in an Incognito/Private browser window) to perform the collaborator edits, comments, and version history steps!

---

## Task 1: Introduction to SaaS and Collaborative Applications

### What is SaaS?
**Software as a Service (SaaS)** is a cloud computing service model in which software applications are provided to users over the internet via a web browser, without needing to install or maintain underlying infrastructure locally.
* **Common Examples:** Google Docs, Google Sheets, Google Slides, Microsoft 365, Microsoft Teams, Zoom, Dropbox, Salesforce.
* **Key Features:** Online access, cloud storage, automatic updates, user authentication, file sharing, real-time collaboration, version history, and multi-device access.

### Step 1: Access a Cloud-Based SaaS Platform
1. Open your web browser.
2. Navigate to **Google Drive** (<https://drive.google.com>) or **Microsoft 365** (<https://www.office.com>).
3. Sign in using your authorized institutional or personal account.
4. Explore the homepage and locate the buttons for creating, opening, and sharing files (e.g., the **+ New** button in Google Drive).

### Step 2: Explore and Identify SaaS Features
Locate and observe the following elements on your dashboard (take a screenshot if required for your lab record):
1. **User account/profile options** (top-right corner).
2. **Application dashboard** and **Cloud storage location** (*My Drive* / *OneDrive*).
3. **File creation options** (Docs, Sheets, Slides).
4. **Sharing & Access-control options** (*Share* button, Viewer/Commenter/Editor roles).
5. **Collaboration & Version/Activity history** (*Last edit was...* / *Activity dashboard*).

---

## Task 2: Collaborative Document Creation Using Cloud SaaS (Google Docs)

### Step 1: Create a New Cloud Document
1. Open **Google Docs** (<https://docs.google.com>).
2. Click **Blank document** to create a new file.
3. In the top-left corner, set the document title to:
   `Cloud Computing Lab 7 – Collaborative Document`

### Step 2: Enter Sample Content
Copy and paste (or type) the following heading, paragraph, and table into your document:

**Title:** Software as a Service

**Content:** SaaS is a cloud service model in which software applications are delivered to users through the internet. Users can access the application without managing the underlying infrastructure.

Insert a **4x2 table** (*Insert* -> *Table*) and fill in the following details:

| SaaS Feature | Description |
| :--- | :--- |
| **Accessibility** | Application can be accessed through the internet |
| **Collaboration** | Multiple users can work on shared content |
| **Updates** | Software updates are managed by the provider |
| **Storage** | Data can be stored in the cloud |

### Step 3: Share the Document
1. Click the **Share** button in the top-right corner.
2. Enter the email address of your lab partner (or your second email account).
3. Change the permission dropdown on the right to **Editor** (observe that *Viewer*, *Commenter*, and *Editor* are available).
4. Click **Send**.

### Step 4: Perform Collaborative Editing
Have the collaborator open the shared document and perform these steps:
1. Add or modify a small portion of the content (e.g., add a fifth row to the table or an extra sentence).
2. Highlight a sentence, click **Add comment** (the speech bubble icon), and leave a comment.
3. On your primary account, reply to or click the checkmark to **Resolve** the comment.

### Step 5: Observe Version History
1. In the top menu, click **File** -> **Version history** -> **See version history** (or click the clock icon at the top right).
2. Expand the timestamps on the right panel to see the exact changes highlighted by user color, along with the user's name and timestamp.
3. *(Take a screenshot of the Version History view to demonstrate collaborative editing for your lab report).*

---

## Task 3: Collaborative Spreadsheet Using Cloud SaaS (Google Sheets)

### Step 1: Create a New Spreadsheet
1. Open **Google Sheets** (<https://sheets.google.com>).
2. Click **Blank spreadsheet**.
3. Set the title in the top-left corner to:
   `Cloud Computing Lab 7 - Collaborative Spreadsheet`

### Step 2: Enter Sample Data
Starting at cell **A1** (row 1 as headers, rows 2–6 as data), enter the following table:

| Cell | Column A (`Student ID`) | Column B (`Student Name`) | Column C (`Subject`) | Column D (`Marks`) |
| :--- | :--- | :--- | :--- | :--- |
| **Row 1** | **Student ID** | **Student Name** | **Subject** | **Marks** |
| **Row 2** | S101 | Student A | Cloud Computing | 82 |
| **Row 3** | S102 | Student B | Cloud Computing | 75 |
| **Row 4** | S103 | Student C | Cloud Computing | 91 |
| **Row 5** | S104 | Student D | Cloud Computing | 68 |
| **Row 6** | S105 | Student E | Cloud Computing | 87 |

### Step 3: Perform Basic Spreadsheet Operations
Below the table (in rows 7 to 10), add labels in Column C and type the corresponding formulas in Column D:

| Row | Column C Label | Column D Formula | Expected Result |
| :--- | :--- | :--- | :--- |
| **Row 7** | **Total Marks** | `=SUM(D2:D6)` | `403` |
| **Row 8** | **Average Marks** | `=AVERAGE(D2:D6)` | `80.6` |
| **Row 9** | **Highest Marks** | `=MAX(D2:D6)` | `91` |
| **Row 10** | **Lowest Marks** | `=MIN(D2:D6)` | `68` |

* Apply bold formatting to the header row (`A1:D1`) and summary labels (`C7:C10`), and add cell borders to make the table clean.

### Step 4: Share the Spreadsheet
1. Click **Share** in the top-right corner.
2. Add your collaborator's email address, assign **Editor** permission, and click **Send**.

### Step 5 & 6: Perform Collaborative Data Entry & Observe Features
Ask your collaborator to:
1. Insert a new row for `S106 | Student F | Cloud Computing | 95` (or add it below the table).
2. Modify one existing mark (e.g., change `Student B` from `75` to `80`) and watch the `SUM` and `AVERAGE` formulas automatically update in real time.
3. Right-click a cell, select **Comment**, and add a note.
4. Check **File** -> **Version history** -> **See version history** (or right-click a modified cell and select **Show edit history**) to verify the changes.

---

## Task 4: Collaborative Presentation and Online Communication

### Task 4A: Creating a Cloud-Based Presentation (Google Slides)

#### Step 1: Create a New Presentation
1. Open **Google Slides** (<https://slides.google.com>).
2. Click **Blank presentation**.
3. Set the presentation title in the top-left corner to:
   `Cloud Computing - SaaS Applications`

#### Step 2: Create Sample Slides (4 Slides Minimum)
Create 4 slides using the following structure:

* **Slide 1 (Title Slide):**
  * **Title:** Software as a Service (SaaS)
  * **Subtitle:** Cloud Computing Lab 7

* **Slide 2:**
  * **Title:** What is SaaS?
  * **Bullet Points:**
    * Cloud-based software delivery model
    * Accessed through the internet
    * Provider manages the underlying infrastructure
    * Usually accessible through a web browser or application

* **Slide 3:**
  * **Title:** Examples of SaaS
  * **Bullet Points:**
    * Google Docs
    * Google Sheets
    * Microsoft 365
    * Microsoft Teams
    * Salesforce

* **Slide 4:**
  * **Title:** Advantages of SaaS
  * **Bullet Points:**
    * Easy accessibility
    * Collaboration
    * Automatic updates
    * Reduced local maintenance
    * Scalable access

#### Step 3: Share the Presentation
1. Click **Share** in the top-right corner.
2. Add your collaborator's email, assign **Editor** permission, and click **Send**.

#### Step 4: Collaboratively Modify the Presentation
Have the collaborator open the presentation and:
1. Edit the text on one of the slides and add an extra bullet point (e.g., add *Zoom* to Slide 3).
2. Change the slide theme or font formatting.
3. Add a comment on a slide.
4. Observe the real-time cursor presence and review changes in **File** -> **Version history**.

---

### Task 4B: Exploring Online Communication and Collaboration

#### Step 1: Access an Online Communication Platform
1. Open **Google Meet** (<https://meet.google.com>), **Microsoft Teams**, or **Zoom** in your browser.
2. Sign in with your authorized account and explore the main dashboard.

#### Step 2: Explore Collaboration Features
Start an instant test meeting (or explore the interface) and identify the following SaaS communication features:
* **Audio/Video Conferencing:** Microphone and camera toggles.
* **Screen Sharing (*Present now*):** Sharing a browser tab, window, or entire screen for real-time walkthroughs.
* **In-Meeting Chat:** Sending real-time text messages and links to participants.
* **Interactive Tools:** Raising hands, digital whiteboarding (e.g., FigJam/Whiteboard integration), and live captions.

---

## Lab Report Screenshot Checklist
To easily demonstrate all four tasks to your instructor, take the following screenshots:
- [ ] **Task 1:** Google Drive / Microsoft 365 dashboard showing file creation and cloud storage options.
- [ ] **Task 2:** Google Docs showing the SaaS table, an active comment thread, and the **Version History** sidebar showing two users.
- [ ] **Task 3:** Google Sheets showing the Student Marks table, computed `SUM`/`AVERAGE`/`MAX`/`MIN` values, and cell edit history/comments.
- [ ] **Task 4A:** Google Slides showing the 4 created slides and collaborative edits/comments.
- [ ] **Task 4B:** Google Meet / Microsoft Teams dashboard or test meeting interface.