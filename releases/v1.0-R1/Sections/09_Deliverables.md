## 9. Deliverables

This section defines the official catalogue of tangible outputs to be produced by the Development Round.

A Deliverable is a completed result, not an implementation activity. It must be capable of being reviewed, demonstrated, verified, and formally accepted.

### Deliverable Governance

Every Deliverable must:

* have a unique and stable identifier;
* represent a completed output;
* identify its related Work Package or Work Packages;
* identify its Development Scope classification;
* identify its primary related Milestone;
* have defined Verification Evidence;
* have defined Acceptance Criteria;
* remain traceable to the Development Objective and Beta Candidate;
* remain within the approved non-production boundaries.

Deliverables classified as **Minimum** are mandatory for successful completion of the Development Round.

Deliverables classified as **Recommended** or **Optional** become required only if their corresponding Work Packages are formally activated. Their absence does not prevent minimum completion unless they have been incorporated into the formally approved delivery commitment.

Completion of an activity, expenditure of allocated funds, submission of code, or passage of time does not establish Deliverable completion.

### 9.1 Product Deliverables

#### D-P01 — Completed Project Expense Workflow

**Description:** A complete user-visible Project Expense capability supporting the approved lifecycle within the correct Project, financial workflow, Operator, budget, category, currency, and evidence context.

**Related Work Packages:** WP-C01 and WP-C02.

**Development Scope:** Minimum.

**Related Milestone:** Milestone 1 — Expense Platform Complete.

**Verification Evidence:** End-to-end product demonstration, lifecycle records, authorization results, relevant test evidence, and completion review.

**Acceptance Criteria:** An authorized user can complete the supported Project Expense lifecycle; prohibited actions are rejected; applicable budget, lifecycle, and responsibility-separation controls remain effective.

#### D-P02 — Completed Operator Workspace

**Description:** A coherent Operator-facing product experience for managing the supported Project Expense, evidence, reporting, and operational workflow.

**Related Work Packages:** WP-C03, supported by WP-C01, WP-C02, and WP-C04.

**Development Scope:** Minimum.

**Related Milestone:** Milestone 2 — Operator Workspace Complete.

**Verification Evidence:** Operator journey demonstration, role-access evidence, resulting product records, and completion review.

**Acceptance Criteria:** An authorized Operator can follow the approved operational scenario without direct database intervention or reliance on disconnected administrative tools.

#### D-P03 — Completed Evidence Workflow

**Description:** A controlled product capability for associating, classifying, reviewing, retaining, and disclosing supporting evidence related to the approved Project Expense workflow.

**Related Work Packages:** WP-C04.

**Development Scope:** Minimum.

**Related Milestone:** Milestone 3 — Evidence Layer Complete.

**Verification Evidence:** Evidence records, association and disclosure demonstrations, validation results, and completion review.

**Acceptance Criteria:** Evidence is connected to the correct Expense and lifecycle context, remains accessible only to permitted roles, and is presented according to its actual authority and status.

#### D-P04 — Completed Investor Transparency Experience

**Description:** A controlled Investor-facing experience presenting permitted Project activity, Project Expense information, evidence availability, reporting, and lifecycle history.

**Related Work Packages:** WP-C05.

**Development Scope:** Minimum.

**Related Milestone:** Milestone 4 — Investor Transparency Complete.

**Verification Evidence:** Investor journey demonstration, disclosure-control results, role-access evidence, and acceptance review.

**Acceptance Criteria:** An authorized Investor can review the approved information while restricted or unsupported information remains protected and accurately labelled.

#### D-P05 — Completed Operational and Investor Reporting

**Description:** Reviewable reporting that connects operational activity, Project Expenses, evidence status, lifecycle information, and permitted Investor visibility.

**Related Work Packages:** WP-C06.

**Development Scope:** Minimum.

**Related Milestone:** Milestone 4 — Investor Transparency Complete.

**Verification Evidence:** Completed reports, source-record comparison, role-based review, and acceptance evidence.

**Acceptance Criteria:** Reports accurately reflect approved source records, preserve applicable status distinctions, and do not imply audited performance or production settlement.

#### D-P06 — Product Experience Enhancements

**Description:** Approved improvements to navigation, information hierarchy, responsive behaviour, accessibility, validation feedback, and user-visible clarity.

**Related Work Packages:** WP-R01.

**Development Scope:** Recommended; conditional upon activation.

**Related Milestone:** Milestone 5 — Beta Candidate Complete.

**Verification Evidence:** Usability review, responsive and accessibility checks, and updated product demonstration.

**Acceptance Criteria:** Activated enhancements function consistently and do not change mandatory workflow, authorization, or non-production boundaries.

#### D-P07 — Enhanced Reporting and Presentation Outputs

**Description:** Approved visual summaries, charts, exports, demonstration datasets, and external-review presentation capabilities beyond minimum reporting.

**Related Work Packages:** WP-R02.

**Development Scope:** Recommended; conditional upon activation.

**Related Milestone:** Milestone 5 — Beta Candidate Complete.

**Verification Evidence:** Export validation, report comparison, presentation review, and acceptance evidence.

**Acceptance Criteria:** Enhanced outputs remain consistent with authoritative product records, disclosure controls, and non-production positioning.

#### D-P08 — Advisory Analytics or AI Capability

**Description:** An optional advisory capability for analysis, summarization, consistency checking, or exception identification within approved operational records.

**Related Work Packages:** WP-O01.

**Development Scope:** Optional; conditional upon formal activation.

**Related Milestone:** Optional extension following Milestone 5.

**Verification Evidence:** Evaluation results, controlled sample outputs, limitation disclosures, and acceptance review.

**Acceptance Criteria:** The capability remains advisory, does not authorize financial actions, does not replace human judgment, and does not present generated conclusions as audited facts.

### 9.2 Technical Deliverables

#### D-T01 — Project Expense API and Authorization Capability

**Description:** A complete application capability through which permitted product users and interfaces can access and perform the supported Project Expense actions.

**Related Work Packages:** WP-C01 and WP-C02.

**Development Scope:** Minimum.

**Related Milestone:** Milestone 1 — Expense Platform Complete.

**Verification Evidence:** API behaviour evidence, authorization results, prohibited-action results, integration evidence, and relevant tests.

**Acceptance Criteria:** Supported actions are available to permitted users, prohibited actions are rejected consistently, and the capability preserves applicable database and workflow controls.

#### D-T02 — Integrated Project Expense and Evidence Data Flow

**Description:** A completed connection between Project Expense records, financial workflows, budgets, lifecycle events, evidence, reporting, and role-appropriate product views.

**Related Work Packages:** WP-C01, WP-C02, WP-C04, WP-C05, and WP-C06.

**Development Scope:** Minimum.

**Related Milestone:** Milestone 3 — Evidence Layer Complete.

**Verification Evidence:** End-to-end data-flow records, state comparison, integration tests, and review evidence.

**Acceptance Criteria:** Information remains connected to the correct Project and workflow context and is represented consistently across the supported Operator, evidence, reporting, and Investor experiences.

#### D-T03 — Role-aware Frontend Integration

**Description:** Completed frontend integration for the supported Operator and Investor journeys, including permitted actions, status presentation, evidence visibility, and prohibited-action feedback.

**Related Work Packages:** WP-C03 and WP-C05.

**Development Scope:** Minimum.

**Related Milestone:** Milestone 4 — Investor Transparency Complete.

**Verification Evidence:** Role-based user journeys, frontend behaviour evidence, access checks, and acceptance review.

**Acceptance Criteria:** Each supported role can access the appropriate experience, while unavailable or restricted functionality remains inaccessible or clearly rejected.

#### D-T04 — Controlled Beta Demonstration Deployment

**Description:** A controlled environment or equivalent review deployment containing the completed Beta Candidate and approved demonstration scenario.

**Related Work Packages:** WP-C07 and WP-C08.

**Development Scope:** Minimum.

**Related Milestone:** Milestone 5 — Beta Candidate Complete.

**Verification Evidence:** Deployment record, environment verification, accessibility check, version reference, and end-to-end demonstration.

**Acceptance Criteria:** The approved Beta Candidate can be reviewed reliably in a controlled environment with clearly identified demonstration data and non-production boundaries.

### 9.3 Demonstration Deliverables

#### D-D01 — Approved Demonstration Scenario and Data

**Description:** A repeatable demonstration scenario and controlled dataset covering the complete approved Operator-to-Investor workflow.

**Related Work Packages:** WP-C07.

**Development Scope:** Minimum.

**Related Milestone:** Milestone 5 — Beta Candidate Complete.

**Verification Evidence:** Scenario specification, dataset record, reset or preparation instructions, and completed scenario review.

**Acceptance Criteria:** The scenario covers the required workflow, produces reviewable system records, and clearly distinguishes demonstration data from live investment or pilot activity.

#### D-D02 — End-to-End Beta Candidate Demonstration

**Description:** A complete observable demonstration of the Project context, Operator workflow, Project Expense lifecycle, authorization controls, evidence, reporting, and Investor transparency.

**Related Work Packages:** WP-C01 through WP-C07.

**Development Scope:** Minimum.

**Related Milestone:** Milestone 5 — Beta Candidate Complete.

**Verification Evidence:** Live or recorded demonstration evidence, reviewer checklist, resulting system records, and acceptance review.

**Acceptance Criteria:** A reviewer can follow the complete approved scenario through observable product behaviour without relying on presentation claims alone.

#### D-D03 — Demonstration Review Package

**Description:** A reviewer-oriented package containing access guidance, scenario instructions, product boundaries, expected outcomes, and references to supporting evidence.

**Related Work Packages:** WP-C07 and WP-C09.

**Development Scope:** Minimum.

**Related Milestone:** Milestone 5 — Beta Candidate Complete.

**Verification Evidence:** Completed package, link and access validation, reviewer walkthrough, and approval record.

**Acceptance Criteria:** An external reviewer can understand how to access, operate, and evaluate the demonstration without interpreting it as a production or live-investment environment.

#### D-D04 — Enhanced Demonstration Reliability

**Description:** Additional reliability, reset, reviewer-access, observability, or repeatability capabilities beyond the minimum demonstration requirement.

**Related Work Packages:** WP-R03.

**Development Scope:** Recommended; conditional upon activation.

**Related Milestone:** Milestone 5 — Beta Candidate Complete.

**Verification Evidence:** Repeat-run results, environment checks, review-access validation, and acceptance record.

**Acceptance Criteria:** The enhanced environment supports repeatable external review without weakening security, data labelling, or product boundaries.

#### D-D05 — Extended Demonstration Coverage

**Description:** One or more approved additional scenarios, localizations, reporting formats, or non-financial demonstration integrations.

**Related Work Packages:** WP-O02.

**Development Scope:** Optional; conditional upon formal activation.

**Related Milestone:** Optional extension following Milestone 5.

**Verification Evidence:** Extended demonstration, boundary review, scenario records, and acceptance evidence.

**Acceptance Criteria:** The extension remains within the approved product boundaries and does not delay or redefine Core completion.

### 9.4 Security and QA Deliverables

#### D-Q01 — Functional and Regression Verification Results

**Description:** Completed verification results covering principal user journeys, Project Expense behaviour, evidence handling, reporting, role access, and relevant existing functionality.

**Related Work Packages:** WP-C08.

**Development Scope:** Minimum.

**Related Milestone:** Milestone 5 — Beta Candidate Complete.

**Verification Evidence:** Test results, regression results, test-environment information, defect records, and closure status.

**Acceptance Criteria:** Required verification passes, relevant regression protection is demonstrated, and no unresolved critical defect prevents the intended Beta Candidate workflow.

#### D-Q02 — Authorization and Financial-Control Verification

**Description:** Completed verification of prohibited actions, responsibility separation, lifecycle controls, Project and workflow boundaries, budget capacity, reservations, and overspending protection.

**Related Work Packages:** WP-C02 and WP-C08.

**Development Scope:** Minimum.

**Related Milestone:** Milestone 5 — Beta Candidate Complete.

**Verification Evidence:** Authorization test results, negative-path results, financial-control tests, and review records.

**Acceptance Criteria:** Applicable controls operate consistently across the supported workflow and known exceptions are documented and accepted.

#### D-Q03 — Product Security Validation Record

**Description:** A completed Beta-appropriate review of relevant authentication, authorization, data exposure, evidence access, configuration, and demonstration-environment security conditions.

**Related Work Packages:** WP-C08.

**Development Scope:** Minimum.

**Related Milestone:** Milestone 5 — Beta Candidate Complete.

**Verification Evidence:** Security review record, identified findings, remediation status, accepted limitations, and closure decision.

**Acceptance Criteria:** No unresolved critical security finding invalidates the Beta Candidate demonstration or approved product boundaries.

This Deliverable does not constitute an external security audit, regulatory certification, or production-readiness approval.

#### D-Q04 — Deployment Verification Record

**Description:** Completed evidence that the controlled review environment contains the intended Beta Candidate version and supports the approved demonstration.

**Related Work Packages:** WP-C07 and WP-C08.

**Development Scope:** Minimum.

**Related Milestone:** Milestone 5 — Beta Candidate Complete.

**Verification Evidence:** Version reference, deployment checks, environment status, access verification, and demonstration result.

**Acceptance Criteria:** The reviewed environment is identifiable, accessible as intended, and consistent with the version submitted for acceptance.

### 9.5 Documentation Deliverables

#### D-DO01 — Updated Product and Technical Documentation

**Description:** Documentation accurately describing the completed Beta Candidate, its capabilities, architecture, technical boundaries, verification approach, and known limitations.

**Related Work Packages:** WP-C09.

**Development Scope:** Minimum.

**Related Milestone:** Milestone 5 — Beta Candidate Complete.

**Verification Evidence:** Documentation review, repository references, consistency review, and approval record.

**Acceptance Criteria:** Documentation matches delivered behaviour, distinguishes implemented and planned capabilities, and preserves all non-production boundaries.

#### D-DO02 — Operator and Reviewer Guidance

**Description:** Practical guidance for operating and reviewing the supported Operator, evidence, reporting, Investor, and demonstration workflows.

**Related Work Packages:** WP-C09.

**Development Scope:** Minimum.

**Related Milestone:** Milestone 5 — Beta Candidate Complete.

**Verification Evidence:** Completed guidance, walkthrough results, and reviewer feedback.

**Acceptance Criteria:** An intended user or reviewer can follow the documented workflow without relying on undocumented implementation knowledge.

#### D-DO03 — Release and Known-Limitations Record

**Description:** A controlled record identifying the delivered version, included capabilities, excluded capabilities, accepted limitations, and non-production status.

**Related Work Packages:** WP-C09.

**Development Scope:** Minimum.

**Related Milestone:** Milestone 5 — Beta Candidate Complete.

**Verification Evidence:** Version record, scope comparison, limitation review, and approval.

**Acceptance Criteria:** The record accurately represents the accepted Beta Candidate and does not overstate production, regulatory, Mainnet, Corporate Setup, or pilot readiness.

#### D-DO04 — Deliverable Traceability Record

**Description:** A complete mapping between the Development Objective, Beta Candidate, Development Scope, Work Packages, Deliverables, Milestones, Verification Evidence, and Acceptance Criteria.

**Related Work Packages:** WP-C09.

**Development Scope:** Minimum.

**Related Milestone:** Milestone 5 — Beta Candidate Complete.

**Verification Evidence:** Completed traceability matrix, consistency check, exception record, and approval.

**Acceptance Criteria:** Every mandatory Deliverable has an unbroken traceability chain and no accepted implementation output exists outside the approved governance structure.

### 9.6 Grant Reporting Deliverables

#### D-G01 — Development Milestone Reports

**Description:** Reviewable reports documenting the status, completed Deliverables, Verification Evidence, exceptions, and acceptance position for each funded Development Milestone.

**Related Work Packages:** WP-C09 and the Work Packages supporting each Milestone.

**Development Scope:** Minimum.

**Related Milestone:** Applicable to Milestones 1–5.

**Verification Evidence:** Submitted reports, referenced Deliverables, evidence links, and review decisions.

**Acceptance Criteria:** Each report accurately represents achieved results, distinguishes incomplete work, and remains traceable to the approved Funding Package.

#### D-G02 — Verification Evidence Package

**Description:** An organized package containing the approved evidence required to verify completed Deliverables and Milestones.

**Related Work Packages:** WP-C08 and WP-C09.

**Development Scope:** Minimum.

**Related Milestone:** Milestone 5 — Beta Candidate Complete.

**Verification Evidence:** Evidence index, test and review records, demonstration evidence, deployment references, documentation references, and integrity review.

**Acceptance Criteria:** Evidence is complete, accessible to the intended reviewer, correctly attributed, and sufficient to evaluate the applicable Acceptance Criteria.

#### D-G03 — Development Round Completion Report

**Description:** A final report explaining what was delivered, what was verified, what remains excluded, how funds were used at the approved reporting level, and whether the Development Objective was achieved.

**Related Work Packages:** WP-C09, supported by all Core Work Packages.

**Development Scope:** Minimum.

**Related Milestone:** Milestone 5 — Beta Candidate Complete.

**Verification Evidence:** Final report, Deliverable status register, evidence references, acceptance decisions, and approved exceptions.

**Acceptance Criteria:** The report provides a factual and traceable account of Development Round completion without presenting planned, Recommended, Optional, or production capabilities as completed.

#### D-G04 — External Review and Demonstration Package

**Description:** A funder-adaptable package containing the Beta Candidate overview, demonstration access, reviewer guidance, selected evidence, milestone status, and non-production boundaries.

**Related Work Packages:** WP-C07 and WP-C09.

**Development Scope:** Minimum.

**Related Milestone:** Milestone 5 — Beta Candidate Complete.

**Verification Evidence:** Completed package, access validation, content review, and funder-adaptation checklist.

**Acceptance Criteria:** The package allows a grant programme, accelerator, investor, venture studio, or strategic partner to review the funded outcome without requiring unsupported claims or unrestricted repository access.

### Deliverable Traceability Rule

Every Deliverable must remain within the following traceability chain:

```text
Development Objective
        ↓
Beta Candidate
        ↓
Development Scope
        ↓
Work Package
        ↓
Deliverable
        ↓
Milestone
        ↓
Verification Evidence
        ↓
Acceptance Criteria
```

No Deliverable may exist outside this chain.

Any proposed output that cannot be traced to an approved Work Package and Development Scope classification must be excluded or processed through formal scope revision.

This Deliverable catalogue is the governing output register for the Development Round. Successful completion requires all Minimum Deliverables to be complete, verified, accepted, and accurately reported. Recommended and Optional Deliverables are governed by their activation status and cannot substitute for an incomplete Minimum Deliverable.
