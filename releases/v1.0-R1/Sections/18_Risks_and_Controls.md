## 18. Risks and Controls

This section establishes the official Risk Management Framework of the Development Round.

A **Risk** is an uncertain event or condition that may affect delivery, verification, acceptance, or appropriate future use of the Development Round results.

A **Control** is a preventive, detective, corrective, or governance measure intended to reduce the likelihood or impact of a Risk.

Controls reduce risk. They do not guarantee that a Risk has been eliminated.

Collectively, the identified Risks, Controls, escalation rules, and Residual Risk requirements define the complete Risk Management Framework supporting the Development Round.

### Risk Classification

Risks must remain distinguishable from related governance concepts:

* a **Dependency** is a required condition;
* a **Risk** is uncertainty concerning a possible event or condition;
* an **Issue** is a Risk or other condition that has occurred and requires action;
* a **Known Limitation** is a present and documented constraint;
* a **Control** is a measure intended to reduce Risk;
* **Residual Risk** is the Risk remaining after applicable Controls.

A failed or delayed Dependency may cause a Risk to materialize as an Issue. It does not change the definitions.

### Risk Assessment

Each material Risk should be assessed using documented qualitative or funder-approved criteria.

#### Likelihood

Likelihood may be classified as:

* Low;
* Medium;
* High.

#### Impact

Impact may be classified as:

* Low;
* Medium;
* High;
* Critical.

Impact should consider possible effects on:

* Minimum Scope;
* Core Work Packages;
* Deliverables;
* Milestones;
* budget;
* schedule;
* evidence sufficiency;
* security;
* acceptance;
* non-production boundaries;
* external reporting.

Risk classification must reflect current evidence and may change as delivery progresses.

### Risk Register

All material Risks must be recorded in a controlled Risk Register.

Each Risk record should include:

* stable Risk ID;
* title and description;
* category;
* source or related Dependency;
* affected Work Packages, Deliverables, or Milestones;
* likelihood;
* impact;
* overall priority;
* current status;
* preventive Controls;
* detective Controls;
* corrective or contingency response;
* Control owner;
* Risk owner;
* review date;
* evidence supporting the assessment;
* Residual Risk;
* escalation threshold;
* escalation status;
* closure or acceptance decision where applicable.

Approved Risk statuses should distinguish among:

* Identified;
* Under Assessment;
* Monitoring;
* Mitigation in Progress;
* Escalated;
* Realized as an Issue;
* Closed;
* Accepted as Residual Risk.

The Risk Register supports governance, traceability, and review. It does not replace the evidence supporting the Risk assessment, Control operation, mitigation result, or Residual Risk decision.

Risk identifiers must remain stable throughout planning, delivery, verification, reporting, acceptance, and subsequent funder review.

### 18.1 Scope Risk

#### Risk

Scope Risk may arise when:

* unapproved functionality is introduced;
* Recommended or Optional work displaces Core work;
* a funder or stakeholder requests additional functionality without approving the corresponding change;
* existing Scope is substituted with easier but less valuable outputs;
* Work Packages expand informally;
* mandatory capabilities remain incomplete;
* implementation activity is mistaken for completed Scope.

Uncontrolled Scope growth may consume budget and delivery capacity without producing the approved Beta Candidate.

#### Controls

Scope Risk is controlled through:

* the governing Development Objective;
* the approved Beta Candidate definition;
* Minimum, Recommended, and Optional Scope classifications;
* the approved Work Package portfolio;
* unique Deliverable identifiers;
* formal change control;
* Optional Scope Activation Rules;
* Deliverable and Milestone traceability;
* Completion and Acceptance Criteria;
* prohibition of informal scope expansion.

Core Work Packages and Minimum Deliverables retain priority over all Recommended and Optional work.

A material Scope change requires documented impact assessment, formal approval, traceability updates, and any required funder approval.

Scope Risk remains open until the Minimum Scope has been completed and accepted.

### 18.2 Budget Risk

#### Risk

Budget Risk may arise from:

* insufficient funding;
* underestimated Core work;
* cost increases;
* budget overrun;
* contingency exhaustion;
* ineligible expenditure;
* uncontrolled reallocation;
* duplicate charging;
* spending outside approved Scope;
* cross-subsidisation of Corporate Setup or Pilot activity;
* expenditure without a Deliverable relationship.

Budget failure may prevent completion even where technical progress has occurred.

#### Controls

Budget Risk is controlled through:

* the fixed USD 40,000 Development Budget;
* Work Package allocations;
* internal cost categories;
* dual expenditure classification;
* Minimum Scope protection;
* controlled contingency;
* approved reallocation rules;
* Section 11 eligibility requirements;
* Section 12 exclusions;
* financial records and variance reporting;
* no-cross-subsidisation rules;
* partial-funding restrictions.

Contingency use must identify the protected Work Package, Deliverable, and Milestone. It must not be used to conceal overruns or finance unrelated activity.

Verified savings must follow the approved reallocation priority and cannot weaken Core delivery.

### 18.3 Schedule Risk

#### Risk

Schedule Risk may arise from:

* delayed funding;
* delayed commencement;
* implementation delay;
* unexpected integration work;
* provider interruption;
* specialist unavailability;
* delayed reviews;
* delayed evidence collection;
* Milestone slippage;
* delayed funder decisions or tranche release.

Schedule Risk affects delivery timing. It does not change what constitutes completion.

#### Controls

Schedule Risk is controlled through:

* dependency-aware Work Package sequencing;
* permitted parallel execution where dependencies remain protected;
* early identification of blocking conditions;
* Milestone-based progress assessment;
* explicit status reporting;
* delayed-funding provisions;
* reassessment when a material Assumption becomes invalid;
* escalation of critical delays;
* controlled adjustment of planning dates where necessary.

The governing principle is:

> **No Schedule Overrides Completion, Verification, Acceptance, or Operational Readiness.**

A deadline, launch date, presentation, funding window, or stakeholder expectation must not cause an incomplete result to be represented as complete.

Where delay threatens the Beta Candidate, governance may pause, resequence, or formally reassess delivery. It must not silently weaken the approved Scope or Acceptance Criteria.

### 18.4 Technical Risk

#### Risk

Technical Risk may arise from:

* integration complexity;
* regression in existing capabilities;
* authorization defects;
* inconsistent role behaviour;
* data-integrity failures;
* Project or workflow misassociation;
* lifecycle inconsistency;
* evidence-linkage defects;
* budget or reservation-control failure;
* reporting inconsistency;
* deployment failure;
* environment differences;
* incompatibility with the current baseline.

A technically present feature may still fail to produce the integrated Beta Candidate.

#### Controls

Technical Risk is controlled through:

* accepted architecture and financial boundaries;
* stable current baseline;
* Work Package decomposition;
* dependency-aware integration;
* preservation of existing database invariants;
* automated and manual verification;
* integration and regression testing;
* negative-path testing;
* financial-control testing;
* controlled deployment verification;
* version-specific evidence;
* defect tracking and closure verification;
* formal architecture and Scope change governance.

Technical Controls must protect the complete workflow rather than only isolated components.

A passing test suite does not eliminate Technical Risk outside the tested scope. Residual uncertainty must remain documented.

### 18.5 Security Risk

#### Risk

Beta-level product Security Risk may arise from:

* unauthorized access;
* privilege escalation;
* incorrect role assignment;
* bypass of authorization controls;
* exposure of restricted Investor, Operator, Expense, or evidence information;
* insecure token handling;
* leaked credentials or secrets;
* insecure configuration;
* dependency vulnerabilities;
* insufficient environment access control;
* disclosure of sensitive security evidence;
* public-repository exposure of private keys, seed phrases, tokens, or `.env` data.

#### Controls

Security Risk is controlled through:

* authentication and authorization review;
* role-boundary verification;
* prohibited-action tests;
* data-exposure review;
* evidence-access review;
* configuration review;
* dependency review where applicable;
* controlled demonstration access;
* secret-handling rules;
* prohibition on publishing secrets in the public repository;
* Security Findings Register;
* remediation and retesting;
* documented accepted limitations;
* Beta-level security closure decision.

No unresolved critical security issue may be accepted where it invalidates the Beta Candidate or controlled review environment.

This Risk framework addresses Beta-level product security. It does not constitute:

* an independent external security audit;
* production certification;
* Mainnet audit;
* custody approval;
* regulatory approval;
* Operational Readiness.

### 18.6 External Dependency Risk

#### Risk

External Dependency Risk may arise from:

* NEAR Testnet interruption or change;
* wallet-provider interruption;
* hosting-provider outage;
* repository-service unavailability;
* database or deployment-provider changes;
* documentation-tool interruption;
* third-party price changes;
* external specialist unavailability;
* third-party service discontinuation;
* changes to access or usage conditions.

The Development Round cannot fully control external providers.

#### Controls

External Dependency Risk is controlled through:

* identification in the Dependency and Risk Registers;
* provider-status monitoring where proportionate;
* version and configuration records;
* preservation of source and evidence;
* controlled backups;
* alternative provider or local verification options where practical;
* limited reliance on non-essential third-party functionality;
* reassessment following material provider change;
* documentation of external interruptions;
* formal escalation where a critical provider affects Milestone completion.

The Beta Candidate does not require NEAR Mainnet.

Uzbekistan-facing Operator and Farmer financial workflows must remain fiat-only and must not acquire a new crypto or wallet dependency as a response to an external provider issue.

### 18.7 Demonstration Risk

#### Risk

Demonstration Risk may arise when:

* the review environment is unavailable;
* the deployed version differs from the accepted version;
* demonstration data is incomplete or misleading;
* the scenario is not repeatable;
* access instructions are unclear;
* a reviewer cannot complete the intended journey;
* presentation materials obscure missing functionality;
* demonstration records are mistaken for live operations;
* known limitations are hidden;
* evidence cannot be traced to demonstrated behaviour.

A demonstration failure may reduce external confidence even where parts of the product are complete.

#### Controls

Demonstration Risk is controlled through:

* an approved demonstration scenario;
* controlled and clearly labelled data;
* deployed-version identification;
* environment verification;
* access verification;
* reviewer guidance;
* known-limitations disclosure;
* resulting product and system records;
* repeat-run evidence where required;
* evidence traceability;
* separation between observable product behaviour and presentation materials;
* prohibition on representing demonstration records as real investment or Pilot activity.

A video, screenshot, slide, or scripted explanation must not substitute for required observable product behaviour.

### 18.8 Funding Continuity Risk

#### Risk

Funding Continuity Risk may arise from:

* funding withdrawal;
* delayed payment;
* delayed tranche release;
* discretionary release conditions;
* changing grant requirements;
* ineligible-cost determinations;
* currency or payment restrictions;
* insufficient partial funding;
* dependence on an uncommitted follow-on source;
* inability to finance remaining Core Scope.

This Risk is particularly material because spending an insufficient initial amount may create incomplete outputs without producing the Beta Candidate.

#### Controls

Funding Continuity Risk is controlled through:

* full-funding or legally committed financing requirements;
* clear commencement conditions;
* documented tranche conditions;
* milestone-linked release structure where applicable;
* eligibility confirmation;
* delayed-funding provisions;
* no obligation to perform unfunded work;
* partial-funding restrictions;
* independently valuable preliminary phases only where formally approved;
* preservation of Minimum Scope;
* formal reassessment if funding conditions change.

Partial funding must not create an obligation to complete an unfunded Development Scope.

AgriPartners must not begin the full Development Round merely on the assumption that the remaining funding gap will later be filled.

If committed funding is interrupted, governance must determine whether delivery should pause, whether a contractually funded phase can be completed independently, or whether formal restructuring is required.

### 18.9 Claims and Positioning Risk

#### Risk

Claims and Positioning Risk may arise from:

* overstating product maturity;
* presenting planned functionality as implemented;
* presenting Beta Candidate acceptance as production readiness;
* implying Operational Readiness;
* implying Mainnet readiness;
* presenting the platform as a regulated financial service;
* implying live investment or custody;
* presenting demonstration data as real operations;
* presenting projected returns as verified or guaranteed;
* implying Corporate Setup completion;
* implying Feedlot or Hissar Pilot approval;
* implying endorsement, partnership, grant approval, or investment commitment without evidence.

Unsupported claims may damage credibility, mislead funders, and create legal or reputational exposure.

#### Controls

Claims and Positioning Risk is controlled through:

* approved terminology;
* frozen Development Objective and Beta Candidate definition;
* verified Current Product Baseline;
* explicit non-production boundaries;
* Use of Funds and Excluded Costs;
* Verification Evidence requirements;
* Acceptance Governance;
* known-limitations disclosure;
* content review against repository evidence;
* distinction between Alpha, Beta Candidate, Operational Readiness, and production;
* distinction between projected, recorded, paid, reconciled, and verified returns;
* prohibition on unsupported partnership, funding, and traction claims.

Approved external positioning must state only what the accepted evidence supports.

Adaptation for a funder may change emphasis, length, or terminology required by that programme. It must not change the underlying facts or maturity status.

### 18.10 Mitigation and Escalation Principles

Risk management must follow the following principles.

#### Early identification

Material Risks should be identified before they prevent delivery or invalidate evidence.

#### Proportional response

Controls should be proportionate to likelihood, impact, cost, Development Scope, and Beta-level context.

#### Clear ownership

Every material Risk and Control must have an identifiable owner.

#### Evidence-based assessment

Likelihood, impact, Control effectiveness, and Residual Risk should be supported by available evidence and professional judgment.

#### Continuous reassessment

Risks must be reassessed when:

* a material Dependency changes;
* an Assumption is invalidated;
* a Work Package changes status;
* a Milestone review occurs;
* a significant defect or security finding appears;
* funding conditions change;
* an external provider changes;
* new evidence affects the assessment.

#### Transparent reporting

Material Risks, realized Issues, failed Controls, and Residual Risks must remain visible in Work Package evidence, Milestone reporting, and the Final Delivery Report where relevant.

#### Escalation

A Risk should be escalated when it may materially affect:

* the Development Objective;
* Minimum Scope;
* a Core Work Package;
* a Minimum Deliverable;
* a mandatory Milestone;
* budget sufficiency;
* funding continuity;
* security;
* evidence sufficiency;
* acceptance;
* approved product or financial boundaries.

Escalation may result in:

* additional review;
* Control strengthening;
* contingency use;
* Work Package resequencing;
* delivery pause;
* funder notification;
* formal Scope or budget change request;
* decision not to proceed.

Escalation does not imply project failure. It is a normal governance response to material uncertainty.

#### No unsupported closure

A Risk must not be closed solely because:

* no incident has yet occurred;
* the scheduled date has arrived;
* related work was performed;
* a Control was designed;
* a report was submitted.

Closure requires evidence that the Risk is no longer applicable, has been resolved, or has been formally accepted as Residual Risk.

## Residual Risk

Some Risk remains after Controls are applied.

Residual Risk must:

* be identified;
* be assessed;
* be documented;
* remain linked to the original Risk;
* identify applicable Controls;
* remain visible during verification and acceptance;
* have an approved disposition where material.

Residual Risk is not automatically unacceptable.

It may be accepted where:

* the Development Objective remains achievable;
* Minimum Deliverables remain valid;
* mandatory security and authorization boundaries remain protected;
* the end-to-end workflow remains demonstrable;
* the Risk is consistent with Beta-level positioning;
* the limitation is disclosed;
* the authorized authority approves the residual position.

Residual Risk is unacceptable where it invalidates the Beta Candidate, conceals incomplete Core Scope, creates an unresolved critical security condition, or makes external positioning materially misleading.

Acceptance of Residual Risk for the Beta Candidate does not mean that the same Risk is acceptable for Operational Readiness, production, Mainnet, custody, or real Pilot operations.

## Risk Traceability

Every material Risk must remain traceable through:

```text
Development Objective
        ↓
Development Scope
        ↓
Work Package
        ↓
Dependency
        ↓
Risk
        ↓
Control
        ↓
Residual Risk
        ↓
Verification Evidence
        ↓
Acceptance Decision
```

A Risk or Control must not be represented as evidence that a Deliverable or Milestone has been completed.

## Relationship to Operational Readiness

Development Round Risk Management supports completion and acceptance of the Beta Candidate.

It does not replace:

* corporate risk management;
* legal or regulatory risk assessment;
* production security assessment;
* banking or payment-provider risk assessment;
* agricultural operational risk assessment;
* livestock and biosecurity risk management;
* Feedlot Pilot risk assessment;
* Hissar Pilot risk assessment;
* Operational Readiness Review.

Risks acceptable within a controlled Beta environment may be unacceptable for live financial or agricultural operations.

This section is the governing Risk Management Framework for the Development Round. It ensures that material uncertainty is identified, assessed, controlled, documented, escalated, and reflected in Verification and Acceptance without being misrepresented as evidence of completion or a guarantee of success.
