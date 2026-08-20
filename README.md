# SE_Lab1_PES1UG24AM907
# Centralized Audit Trail Compliance Engine

**Course:** PES University — Dept. of CSE(AIML) — Software Engineering
**Lab 1:** Requirements Engineering & UML Use-Case Modelling
**Problem Statement #50** | Developer Tools & IT Operations

## Problem Context

A compliance logging platform that ingests enterprise application event logs, masks sensitive PII fields (SSNs, credit card numbers) in accordance with GDPR before persisting them, and generates cryptographically verifiable, immutable audit exports. The system exists to help organizations prove regulatory compliance while giving auditors a trustworthy, tamper-evident record of historical activity.

## Actors

- **Compliance Officer** — configures PII masking policy and generates audit exports for regulators.
- **Security Auditor** — searches historical audit logs and verifies the integrity of generated exports.

## Repository Structure

```
/requirements       → Functional & Non-Functional Requirements table
/diagrams           → UML use-case diagram (source file + exported image)
/flow-spec           → Use-case flow specification document
README.md           → This file
```

## Requirements Summary

Five functional requirements (FR-001 to FR-005) and two non-functional requirements (NFR-001, NFR-002) are documented in [`/requirements`](./requirements). They cover log ingestion & PII masking, masking policy configuration, audit log search, audit export generation, and export integrity verification, along with performance and security constraints.

## Use-Case Diagram

![Use case diagram](diagrams/use-case-diagram.png)

- `Generate Audit Export` **«include»s** `Compute Integrity Hash` — hashing always runs as part of export generation.
- `Flag Tampering Alert` **«extend»s** `Verify Export Integrity` — the alert only fires conditionally, when a tamper check fails.

Full diagram source is available in [`/diagrams`](./diagrams).

## Use-Case Flow Specification

The detailed flow specification is documented for **Generate Audit Export**, covering preconditions, postconditions, the main success scenario, and one alternate flow. See [`/flow-spec`](./flow-spec).

## Author

**Name:K Preksha**
**SRN:PES1UG24AM907**
**Section:D**
**Semester:5**
