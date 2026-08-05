## 15. Completion and Acceptance Criteria

This section establishes the official completion and acceptance framework for the Development Round.

It defines the conditions that must be satisfied before a Work Package, Deliverable, Milestone, or the completed **Pilot Operations & Investor Evidence Beta Candidate** may receive formal acceptance.

The governance sequence is:

```text
Implementation
        ↓
Verification
        ↓
Completion Assessment
        ↓
Acceptance Decision
        ↓
Formal Recognition
```

These stages are related but not interchangeable.

* **Implementation** produces the intended output.
* **Verification** produces evidence about that output.
* **Completion Assessment** evaluates the output and evidence against the applicable criteria.
* **Acceptance** is the documented governance decision.
* **Formal Recognition** records the accepted status for reporting and future reliance.

Completion is not acceptance. Verification is not acceptance. Evidence is not acceptance.

### 15.1 Product Completion Criteria

The product may be assessed as complete only when the delivered product demonstrates that the Development Objective has been achieved.

Product completion requires confirmation that:

* the Pilot Operations & Investor Evidence Beta Candidate defined in Section 6 exists;
* the Minimum Viable Development Scope has been delivered;
* all Core Work Packages are complete;
* all Minimum Deliverables are complete;
* all mandatory Milestones have satisfied their Exit Criteria;
* the required product capabilities operate as an integrated product state;
* mandatory role and authorization boundaries are preserved;
* Project Expense, evidence, reporting, and Investor Transparency capabilities are connected;
* required Verification Evidence exists;
* delivered behaviour corresponds to the accepted product version;
* no unresolved issue invalidates the Development Objective or Beta Candidate;
* non-production boundaries remain accurate and visible.

Completion must be assessed against delivered and observable product behaviour.

Planned, partially implemented, Recommended, Optional, or documented-only functionality must not be counted as completed Minimum Scope.

Recommended or Optional capabilities affect completion only when formally activated and incorporated into the approved delivery commitment.

### 15.2 End-to-End Workflow Criteria

The complete operational workflow must be observable, repeatable, and reviewable within the controlled Beta Candidate environment.

The end-to-end workflow must demonstrate:

* access to the relevant Project context;
* an authorized Operator interaction;
* initiation or recording of a supported Project Expense;
* association with the correct workflow, budget, category, currency, and Operator context;
* application of role and authorization controls;
* enforcement of the supported Expense lifecycle;
* association and review of supporting evidence;
* preservation of lifecycle history;
* generation or presentation of applicable reporting;
* controlled disclosure of relevant information to an Investor;
* resulting product and system records.

The workflow satisfies the completion criteria only when:

* the approved scenario can be completed through the product;
* required steps do not depend on direct database intervention;
* prohibited actions are rejected consistently;
* required controls remain effective;
* resulting records correspond to the performed actions;
* the workflow can be reviewed against documented evidence;
* demonstration data is clearly identified;
* known limitations remain visible;
* no critical defect prevents the intended scenario.

A walkthrough, presentation, video, or script cannot independently satisfy these criteria without corresponding observable product behaviour and reviewable records.

### 15.3 Operator Acceptance Criteria

The Operator-facing product experience may be accepted when an authorized Operator can complete the supported operational scenario within the approved product boundaries.

Operator acceptance requires confirmation that:

* the relevant Project context is accessible;
* applicable workflow, budget, Expense, evidence, and reporting information is understandable;
* the Operator can perform each permitted action required by the supported scenario;
* prohibited or unavailable actions are clearly rejected;
* role boundaries are applied consistently;
* authorization status is visible where necessary;
* Project Expense lifecycle state is reviewable;
* applicable budget and control information is available;
* supporting evidence can be associated and reviewed appropriately;
* errors and validation results provide sufficient user feedback;
* the workflow does not require an Uzbekistan-facing crypto wallet or on-chain financial action;
* the Operator journey can be completed without undocumented technical intervention.

Operator acceptance is product-level acceptance. It does not establish legal identity, corporate mandate, contract authority, banking authority, payment authority, or Operational Readiness.

### 15.4 Investor Demonstration Criteria

The Investor-facing experience may be accepted when an authorized Investor can review the permitted Project information through a coherent and controlled product experience.

Investor demonstration acceptance requires confirmation that:

* relevant Project context is available;
* operational progress is understandable;
* permitted Project Expense information is reviewable;
* applicable budget or budget-summary information is presented appropriately;
* evidence availability or permitted evidence references are visible;
* relevant reports are accessible;
* lifecycle history is reviewable;
* projected, recorded, approved, paid, reconciled, and completed states remain distinguishable;
* disclosure controls protect restricted information;
* internal records are not presented as possessing unsupported external authority;
* demonstration records are not presented as live investment activity;
* displayed returns are not presented as audited, verified, guaranteed, or production-settled results;
* the Investor journey can be demonstrated and reviewed against the applicable evidence.

The accepted Investor experience demonstrates controlled transparency. It does not demonstrate live Investor onboarding, live capital intake, custody, payouts, production settlement, or a regulated investment service.

### 15.5 QA and Security Criteria

Beta Candidate acceptance requires sufficient QA and product-level security evidence for the approved scope and version.

QA completion requires confirmation that:

* mandatory functional tests have been completed;
* relevant integration tests have been completed;
* relevant regression tests have been completed;
* negative-path and prohibited-action behaviour has been evaluated;
* authorization boundaries have been evaluated;
* Project Expense lifecycle controls have been evaluated;
* budget, reservation, and overspending controls have been evaluated;
* evidence-access and disclosure controls have been evaluated;
* the principal Operator and Investor journeys have been verified;
* failed, skipped, or excluded checks affecting acceptance are disclosed;
* material defects have documented status;
* resolved defects have been appropriately reverified.

Security completion requires confirmation that:

* authentication and authorization have received Beta-level review;
* relevant data-exposure risks have been reviewed;
* evidence-access boundaries have been reviewed;
* configuration and secret-handling conditions have been reviewed;
* relevant dependency risks have been reviewed where applicable;
* security findings have been recorded;
* required remediation has been verified;
* accepted security limitations are documented;
* no unresolved critical security issue invalidates the Beta Candidate or controlled demonstration environment.

These criteria establish Beta-level product quality and security acceptance only.

They do not constitute:

* production certification;
* an independent external security audit unless separately commissioned;
* regulatory approval;
* Mainnet approval;
* custody approval;
* banking approval;
* Operational Readiness.

### 15.6 Deployment Criteria

The controlled Beta Candidate deployment may be accepted when the reviewed environment corresponds to the version submitted for acceptance and supports the approved demonstration.

Deployment acceptance requires confirmation that:

* the deployed version or commit is identifiable;
* the environment is identified;
* the relevant build completed successfully;
* required configuration is present without exposing secrets;
* applicable database migrations and required data state are established;
* the environment is accessible to the intended reviewer;
* the approved demonstration scenario can be completed;
* the resulting records are reviewable;
* material differences between tested and deployed environments are documented;
* deployment limitations are disclosed;
* no unresolved deployment issue prevents Beta Candidate review.

The accepted deployment remains a controlled Beta or demonstration environment.

Deployment acceptance does not establish production availability, production scalability, disaster recovery, Mainnet readiness, production monitoring, financial infrastructure readiness, or authorization for live operations.

### 15.7 Documentation Criteria

Documentation may be accepted when it accurately represents the delivered Beta Candidate and provides sufficient guidance for operation, review, verification, and reporting.

Documentation acceptance requires:

* current product documentation;
* relevant technical documentation;
* relevant API or integration documentation;
* Operator guidance;
* reviewer or demonstration guidance;
* release record;
* known-limitations record;
* Deliverable register;
* evidence index;
* traceability matrix;
* appropriate version identification;
* documentation review and approval evidence.

Accepted documentation must:

* correspond to delivered product behaviour;
* distinguish implemented from planned functionality;
* distinguish Minimum from activated Recommended or Optional Scope;
* preserve the Estonia-to-Uzbekistan fiat boundary;
* distinguish Legacy Testnet Alpha behaviour from the target architecture;
* preserve non-production limitations;
* avoid unsupported product, security, regulatory, financial, traction, or return claims.

Documentation cannot compensate for missing product functionality. A documented capability is not accepted as implemented unless corresponding product and verification evidence exists.

### 15.8 Known-Limitations Criteria

Known limitations do not automatically prevent Beta Candidate acceptance.

A limitation may be acceptable when it:

* is documented clearly;
* is supported by an identifiable record;
* does not invalidate the Development Objective;
* does not prevent the approved end-to-end workflow;
* does not compromise a mandatory authorization or financial control;
* does not expose unacceptable security or data risk;
* does not make a Minimum Deliverable materially incomplete;
* remains consistent with Beta-level and non-production positioning;
* has an approved disposition;
* remains visible in relevant documentation and reporting.

A limitation is unacceptable when it:

* prevents completion of a mandatory workflow;
* invalidates a Core Deliverable;
* bypasses a required authorization boundary;
* compromises material financial or evidence integrity;
* creates an unresolved critical security risk;
* causes Investor disclosure to become materially misleading;
* requires planned functionality to be represented as implemented;
* conceals a failed verification requirement;
* contradicts an approved product or financial boundary;
* prevents objective review of the Beta Candidate.

Every accepted limitation must identify:

* the affected requirement;
* impact;
* residual risk;
* reason acceptance remains possible;
* compensating control where applicable;
* approving authority;
* relationship to future work or Operational Readiness.

Hidden or omitted limitations are unacceptable.

Acceptance of a limitation for the Beta Candidate does not mean that the limitation will be acceptable for Operational Readiness, production deployment, Mainnet use, or a real Pilot.

### 15.9 Milestone Exit Criteria

Milestone Exit Criteria determine whether each Milestone has reached the verified state defined in Section 13.

The governance sequence for each Milestone is:

```text
Included Work Packages completed
        ↓
Required Deliverables completed
        ↓
Verification Evidence assembled
        ↓
Exit Criteria assessed
        ↓
Milestone Acceptance Decision
```

Milestone acceptance requires:

* included mandatory Work Packages to be complete;
* required Deliverables to be complete;
* dependencies to be satisfied;
* Verification Evidence to be sufficient;
* Exit Criteria to be satisfied;
* material exceptions and limitations to be disclosed;
* unresolved issues not to invalidate the Milestone state;
* a documented decision by the authorized authority.

Completion of every mandatory Milestone is necessary but not sufficient for final Development Round acceptance.

Final acceptance additionally requires:

* successful integration across Milestones;
* completion of the full Beta Candidate;
* consistency of the complete evidence package;
* satisfaction of the final Completion Criteria;
* formal evaluation of the Development Objective.

A Milestone accepted earlier may be reopened if later integration reveals that its output no longer satisfies the applicable criteria. Any reopening must be documented and reflected in subsequent reporting.

### 15.10 Final Beta Candidate Acceptance

Final Beta Candidate acceptance is the formal decision that the Development Round has produced the product state approved in Sections 5 and 6.

Final acceptance requires confirmation that:

* the Development Objective has been achieved;
* the Pilot Operations & Investor Evidence Beta Candidate exists;
* the Minimum Viable Development Scope has been delivered;
* all Core Work Packages are complete;
* all Minimum Deliverables are complete;
* all mandatory Milestones are accepted;
* the end-to-end workflow satisfies the approved criteria;
* Operator Acceptance Criteria are satisfied;
* Investor Demonstration Criteria are satisfied;
* QA and Security Criteria are satisfied;
* Deployment Criteria are satisfied;
* Documentation Criteria are satisfied;
* Verification Evidence is sufficient;
* complete traceability exists;
* material exceptions and limitations are disclosed;
* accepted limitations do not invalidate the Beta Candidate;
* the Final Delivery Report accurately reflects the completed result;
* the authorized governance decision has been recorded.

Final Beta Candidate acceptance does not constitute:

* Corporate Setup completion;
* legal or regulatory readiness;
* Operational Readiness;
* Production Readiness;
* Mainnet Readiness;
* banking, payment, custody, or settlement readiness;
* live investment authorization;
* Feedlot Pilot approval;
* Hissar Pilot approval;
* a Pilot GO decision;
* verification or guarantee of investment returns.

An accepted Beta Candidate may proceed to a separate Operational Readiness Review. Final Beta Candidate acceptance does not predetermine that review’s outcome.

## Acceptance Governance

Acceptance requires:

* completed Verification Evidence;
* assessment against the applicable Completion or Exit Criteria;
* disclosure of material defects, risks, exceptions, and limitations;
* confirmation of applicable dependencies;
* a documented decision;
* an authorized approving authority;
* a retained Acceptance Record.

The appropriate approving authority or designated decision-makers must be determined under the applicable AgriPartners governance model and any funder-specific agreement.

Acceptance must never result automatically from:

* elapsed time;
* budget expenditure;
* repository activity;
* completed coding;
* a branch, commit, Pull Request, merge, or release tag;
* passing tests without requirement coverage;
* a completed demonstration without the required evidence;
* report submission;
* a task status;
* a planned launch or presentation date;
* external pressure or funding deadlines.

No schedule overrides acceptance criteria.

### Acceptance Record

Every formal Acceptance Decision must identify:

* the object being assessed;
* reviewed version or baseline;
* applicable criteria;
* Verification Evidence index;
* criteria assessment;
* unresolved defects or exceptions;
* accepted limitations;
* decision;
* decision rationale;
* approving authority;
* decision date;
* conditions or follow-up obligations where applicable.

Acceptance identifiers and decisions must remain stable and traceable throughout later reporting, audit, funder review, and Operational Readiness assessment.

## Acceptance Decision Types

The permitted formal decisions are:

### Accepted

All applicable Completion Criteria are satisfied, required evidence is sufficient, and no unresolved limitation invalidates the accepted result.

### Accepted with Approved Limitations

All requirements necessary for the intended Beta Candidate use are satisfied, while specifically documented, non-blocking limitations remain.

Each limitation must have an approved rationale, residual-risk assessment, and disclosure record.

### Conditionally Accepted

Acceptance is permitted subject to one or more explicit, measurable, and approved conditions.

The decision must identify:

* each unresolved condition;
* responsible owner;
* required evidence;
* resolution requirement;
* review authority;
* consequence of non-resolution.

Conditionally Accepted is not equivalent to final Accepted status. The result must not be represented as fully accepted until the conditions are resolved and the decision is formally updated.

A condition must not be used to defer a failure that invalidates the Development Objective, Core Scope, mandatory security boundary, or Beta Candidate.

### Not Accepted

One or more applicable Completion Criteria are not satisfied, required evidence is insufficient, or an unresolved issue invalidates the claimed result.

The decision must identify the rejection basis and the requirements for reconsideration where reconsideration remains possible.

## Acceptance Traceability

Every Acceptance Decision must remain within the following traceability chain:

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
Completion Criteria
        ↓
Acceptance Decision
```

No Work Package, Deliverable, Milestone, or Development Round result may be represented as accepted outside this chain.

## Relationship to Section 14

Section 14 establishes the Verification and Reporting Evidence used to assess Development Round results.

Section 15 establishes the Completion and Acceptance Criteria and the governance process through which those results receive a formal decision.

Evidence informs acceptance. Evidence never replaces acceptance.

Accordingly, this section is the governing acceptance standard for Work Packages, Deliverables, Milestones, the Beta Candidate, and final Development Round completion.
