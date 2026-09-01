# Lab 2 – Agile Backlog Creation & Sprint Simulation in Jira

**Project:** Centralized Audit Trail Compliance Engine
**Domain:** Developer Tools & IT Operations
**Target Actors:** Compliance Officer, Security Auditor

## Overview

This lab applies Agile backlog creation and sprint simulation to the Centralized Audit Trail Compliance Engine — a system that centrally ingests, searches, reports on, monitors, and secures audit trail data across an organization's developer tools and infrastructure, for use by Compliance Officers and Security Auditors.

## Epics & User Stories

### Epic 1: Audit Log Ingestion & Aggregation
*Centrally collect and normalize audit data from distributed developer tools and IT infrastructure (CI/CD pipelines, cloud IAM, version control, ticketing systems) into a single compliance-ready store.*

| ID | Story | As a | I want to | So that | Points | Priority |
|---|---|---|---|---|---|---|
| 1.1 | Multi-Source Log Ingestion | Security Auditor | ingest audit logs automatically from CI/CD, cloud IAM, and version control systems | I have a single unified view of all system activity | 8 | High |
| 1.2 | Log Normalization | Compliance Officer | have ingested logs normalized into a standard schema | I can compare events consistently across tools | 5 | High |
| 1.3 | Real-Time Streaming Ingestion | Security Auditor | see new audit events appear within minutes of occurring | I can investigate incidents as they happen | 5 | Medium |

### Epic 2: Audit Trail Search & Investigation
*Give security auditors powerful search, filter, and trace capabilities to investigate incidents and user activity across the audit trail.*

| ID | Story | As a | I want to | So that | Points | Priority |
|---|---|---|---|---|---|---|
| 2.1 | Advanced Search & Filtering | Security Auditor | search audit logs by user, resource, action type, and time range | I can quickly investigate a specific incident | 5 | High |
| 2.2 | Event Timeline Reconstruction | Security Auditor | reconstruct the chronological sequence of events tied to a specific user or resource | I can trace the full path of an incident | 8 | High |
| 2.3 | Saved Investigation Queries | Security Auditor | save and rerun common investigation queries | I can speed up recurring audit checks | 3 | Low |

### Epic 3: Compliance Reporting & Evidence Generation
*Enable compliance officers to generate audit-ready reports and evidence packages mapped to regulatory frameworks such as SOC 2, ISO 27001, and GDPR.*

| ID | Story | As a | I want to | So that | Points | Priority |
|---|---|---|---|---|---|---|
| 3.1 | Framework-Mapped Reports | Compliance Officer | generate reports mapped to specific compliance frameworks (SOC 2, ISO 27001, GDPR) | I can demonstrate control adherence during audits | 8 | High |
| 3.2 | Scheduled Compliance Reports | Compliance Officer | schedule recurring compliance reports | I always have up-to-date evidence without manual effort | 3 | Medium |
| 3.3 | Exportable Evidence Packages | Compliance Officer | export audit evidence as a signed, tamper-evident package | I can hand it to external auditors with confidence in its integrity | 5 | High |

### Epic 4: Anomaly Detection & Alerting
*Detect suspicious or policy-violating activity within the audit trail and alert the right stakeholders in real time.*

| ID | Story | As a | I want to | So that | Points | Priority |
|---|---|---|---|---|---|---|
| 4.1 | Policy Violation Detection | Security Auditor | have the system flag actions that violate predefined compliance policies | I can respond before they escalate | 8 | High |
| 4.2 | Real-Time Alerts | Compliance Officer | receive alerts when high-risk events occur | I can act immediately instead of discovering issues during periodic review | 5 | High |
| 4.3 | Alert Triage Dashboard | Security Auditor | see a dashboard summarizing open and resolved alerts | I can prioritize investigation effort | 3 | Medium |

### Epic 5: Audit Trail Integrity & Access Control
*Guarantee the audit trail itself is tamper-proof, immutable, and accessible only to authorized compliance and security personnel.*

| ID | Story | As a | I want to | So that | Points | Priority |
|---|---|---|---|---|---|---|
| 5.1 | Immutable Log Storage | Compliance Officer | have audit logs stored in a tamper-evident, immutable format | the trail itself can be trusted as legal/regulatory evidence | 8 | High |
| 5.2 | Role-Based Access Control | Security Auditor | have access to audit data restricted by role | sensitive audit information isn't exposed to unauthorized users | 5 | High |
| 5.3 | Retention Policy Management | Compliance Officer | configure retention periods per log category | we meet regulatory retention requirements without over-storing data | 3 | Medium |

## Story Point Estimation Approach (Planning Poker)

Story points were assigned using the Fibonacci sequence (3, 5, 8), reasoning about each story's complexity and uncertainty:

- **8 points** – stories requiring new subsystems or non-trivial logic (e.g. multi-source ingestion, timeline reconstruction, framework-mapped reporting, anomaly detection, immutable storage).
- **5 points** – stories involving moderate integration or cross-cutting work (e.g. normalization, streaming ingestion, RBAC, alerting).
- **3 points** – smaller, largely configuration-driven stories (e.g. saved queries, scheduled reports, retention settings).

As this lab was completed individually, estimation was done by evaluating each story independently against these criteria rather than through a live group Planning Poker session.

## Backlog Prioritization

Priority was set per story based on dependency and value to the target actors: ingestion, normalization, and access control were ranked **High** since search, reporting, and alerting all depend on them. Core search, reporting, and detection stories were also **High**. Enhancement-style stories (saved queries, scheduling, dashboards, retention config) were ranked **Medium/Low**. The backlog was reordered in Jira to reflect this, highest priority at the top.

## Sprint 1

**Sprint scope:** CEN-21 (1.1 Multi-Source Log Ingestion, 8 pts), CEN-7 (1.2 Log Normalization, 5 pts), CEN-9 (2.1 Advanced Search & Filtering, 5 pts) — 18 story points total.

Progress was simulated by moving stories across **To Do → In Progress → Done**, with comments added at each stage describing simulated work performed.

## Screenshots

### 1. Backlog with Story Points
![<img width="906" height="523" alt="WhatsApp Image 2026-09-01 at 3 41 24 PM" src="https://github.com/user-attachments/assets/c7dea142-014c-4ee4-99be-d20aa4c1763f" />
](screenshots/backlog-points.png)

### 2. Prioritized & Reordered Backlog
![<img width="860" height="548" alt="WhatsApp Image 2026-09-01 at 3 45 09 PM" src="https://github.com/user-attachments/assets/33f6ed21-f6b6-4c3c-bb5e-93ca4534d334" />
](screenshots/backlog-priority.png)

### 3. Sprint 1 Board (To Do / In Progress / Done)
![<img width="885" height="186" alt="WhatsApp Image 2026-09-01 at 3 46 01 PM" src="https://github.com/user-attachments/assets/756f518f-b395-40b6-b583-7b16ad278d6c" />
](screenshots/sprint-board.png)
### 4. Sprint 2 Board (To Do /In Progree /Done)
![<img width="897" height="407" alt="WhatsApp Image 2026-09-01 at 4 04 18 PM" src="https://github.com/user-attachments/assets/519afc91-34eb-42dc-b611-03fd5b217405" />


### 4. Comment on a Story
![<img width="362" height="746" alt="WhatsApp Image 2026-09-01 at 3 47 35 PM" src="https://github.com/user-attachments/assets/9123ab66-d165-44c6-a652-bb32f13bb0e3" />
](screenshots/comment.png)

### 5. Burndown Chart
![<img width="1426" height="370" alt="WhatsApp Image 2026-09-01 at 3 49 23 PM" src="https://github.com/user-attachments/assets/71a3c732-686d-4291-8a40-246dab0a7648" />
](screenshots/burndown.png)

### 6.Summary 
![<img width="1342" height="626" alt="image" src="https://github.com/user-attachments/assets/cd54916a-fb08-4dd0-ab26-15d209c15015" />]
![<img width="1080" height="617" alt="image" src="https://github.com/user-attachments/assets/0c2e5a99-9d2f-4340-bb1d-c26ca96c8da7" />]



## Reflection

Working through this lab made the difference between a backlog and a *prioritized* backlog concrete — reordering stories by dependency (ingestion before search, search before reporting) showed how Agile prioritization is really about sequencing value delivery, not just labeling importance. Estimating story points using Fibonacci also forced a more disciplined way of thinking about complexity versus effort, rather than guessing "big vs. small."

One practical challenge came up early: the project was initially set up as company-managed, which restricted permissions (I couldn't delete a mistakenly created issue without admin rights). Rebuilding it as a team-managed project resolved this immediately, since project ownership grants full admin control by default — a good reminder that Jira project type has real workflow implications beyond just backlog structure.

The burndown chart also clarified how sprint tracking works in practice: since this was a compressed, single-day simulation rather than a real multi-day sprint, the chart only showed a single drop in remaining points (from 18 to 13) rather than a smooth decline — but it still illustrated the core idea of comparing actual progress (red line) against the ideal pace (guideline line), which is the main value of a burndown chart in a real sprint.
