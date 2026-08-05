## 14. Verification and Reporting Evidence

This section defines the official evidence framework used to verify Work Packages, Deliverables, Milestones, and final Development Round completion.

A completion claim is valid only when relevant, attributable, accessible, and reviewable evidence demonstrates that the applicable result exists and can be evaluated against its approved requirements.

The evidence framework distinguishes between:

* implementation activity;
* evidence that implementation activity occurred;
* verification of the completed result;
* formal reporting of that result;
* acceptance of the result.

These stages are related but are not interchangeable.

Money spent, time elapsed, code written, a commit created, a Pull Request merged, a demonstration prepared, a report submitted, or a task marked complete does not independently prove that a Deliverable or Milestone has been achieved.

### Evidence Register

Verification Evidence must be recorded in a controlled Evidence Register.

Each evidence entry should identify:

* a unique evidence identifier;
* evidence title and type;
* related Work Package;
* related Deliverable;
* related Milestone;
* requirement or criterion supported;
* source or owner;
* creation or execution date;
* relevant product version;
* relevant environment where applicable;
* storage location or review link;
* access classification;
* review status;
* known limitations;
* integrity information where appropriate.

Evidence must be accessible to the authorized reviewer. Accessibility does not require all evidence to be made public.

Security-sensitive information, personal data, credentials, private keys, environment secrets, confidential commercial information, and unresolved vulnerability details must not be published in the public repository or unrestricted evidence packages.

### 14.1 Repository and Pull Request Evidence

Repository evidence establishes what changed within the product source and documentation baseline, why it changed, how it was reviewed, and whether it entered the accepted implementation baseline.

Repository evidence may include:

* commit identifiers;
* commit messages;
* branch references;
* Pull Request references;
* changed-file records;
* code or documentation review records;
* review comments and resolution records;
* merge records;
* accepted baseline commit identifiers;
* release tags;
* repository status records;
* implementation traceability references;
* relevant CI or workflow-run records.

Repository evidence supporting a completion claim should identify:

* the Work Package and Deliverable supported;
* the purpose of the change;
* the relevant files or components;
* the review performed;
* the resulting decision;
* whether the change was merged;
* the exact accepted baseline containing the change.

Unmerged branches, draft Pull Requests, abandoned commits, or local changes may demonstrate activity but do not establish inclusion in the accepted baseline.

A commit, Pull Request, review, merge, or release tag is supporting evidence only. It does not independently prove:

* correct product behaviour;
* satisfaction of Acceptance Criteria;
* successful deployment;
* completed integration;
* absence of defects;
* Milestone completion;
* formal acceptance.

Repository evidence must be evaluated together with the applicable test, product, demonstration, documentation, and review evidence.

### 14.2 Test and QA Evidence

Test and QA evidence demonstrates whether the applicable product capability behaves as required within the tested scope.

Acceptable evidence may include:

* automated test results;
* unit-test results;
* integration-test results;
* database and migration verification;
* regression-test results;
* negative-path tests;
* authentication and authorization tests;
* responsibility-separation tests;
* Project Expense lifecycle tests;
* budget and overspending-control tests;
* concurrency tests;
* evidence-access and disclosure tests;
* API behaviour tests;
* frontend user-journey verification;
* deployment checks;
* defect records;
* remediation and closure records;
* manual review checklists where automation is not appropriate.

Every test record used as Verification Evidence should identify:

* the tested product version or commit;
* the applicable environment;
* the execution date;
* the tested Work Package or Deliverable;
* the relevant requirement;
* the test result;
* failures, warnings, skips, or exclusions;
* the responsible reviewer or execution source;
* any limitation affecting interpretation.

A passing test suite proves only the behaviour covered by its tested scope. It does not prove requirements that were omitted, disabled, skipped, excluded, or evaluated in a materially different environment.

Skipped and excluded tests must remain visible where they affect a completion claim. A test report must not be represented as fully passing if relevant failures or exclusions have been removed from the reported result without explanation.

Manual QA evidence must identify the scenario, expected result, observed result, tested version, environment, reviewer, and outcome.

Defect records must distinguish among:

* open;
* under investigation;
* resolved;
* verified closed;
* accepted limitation;
* deferred outside the approved scope.

Resolution without verification does not establish defect closure.

### 14.3 Security Evidence

Security evidence supports Beta-level product security validation within the approved Development Scope.

It may include:

* authentication review;
* authorization review;
* role-boundary review;
* prohibited-action testing;
* data-exposure review;
* evidence-access review;
* configuration review;
* dependency review;
* secret-handling review;
* demonstration-environment review;
* security findings register;
* remediation records;
* retest results;
* accepted limitations;
* closure decision.

Each material security finding should identify:

* the affected capability;
* severity or risk classification;
* evidence supporting the finding;
* potential impact;
* remediation or control;
* retest result where applicable;
* residual risk;
* disposition;
* approving authority for any accepted limitation.

Security evidence must be handled according to its sensitivity. Evidence made available to a funder or reviewer may use controlled summaries where unrestricted disclosure would create security risk.

No secret, token, private key, seed phrase, unrestricted credential, or sensitive production-style configuration may be included in the public repository or public evidence package.

Security Evidence produced under the Development Round is:

* Beta-level product security evidence;
* limited to the reviewed scope and version;
* subject to documented limitations.

It must not be described as:

* an independent external security audit unless one was actually commissioned and completed;
* production certification;
* regulatory approval;
* Mainnet smart-contract audit;
* custody approval;
* banking-security approval;
* Operational Readiness approval.

### 14.4 Deployment Evidence

Deployment Evidence demonstrates that the controlled review or demonstration environment corresponds to the product version submitted for verification.

It may include:

* deployed version or commit reference;
* environment identifier;
* deployment record;
* build result;
* configuration summary;
* migration status;
* database status appropriate to the demonstration;
* access verification;
* health or availability check;
* dependency status;
* demonstration result;
* deployment limitation record.

Deployment Evidence should establish:

* what version was deployed;
* where it was deployed;
* when deployment occurred;
* which configuration class was used;
* whether required components were available;
* whether the approved demonstration could be completed;
* whether the environment differed materially from the verified test environment.

Sensitive configuration values must not be exposed. Evidence should confirm the presence and correct treatment of required configuration without publishing secrets.

Deployment Evidence confirms only the controlled Beta Candidate review environment. It does not independently establish:

* production readiness;
* production scalability;
* production monitoring;
* disaster recovery;
* regulatory compliance;
* live financial capability;
* Mainnet readiness;
* Operational Readiness.

### 14.5 Demonstration Evidence

Demonstration Evidence shows that the completed Beta Candidate can be observed and reviewed as an integrated product state.

The required evidence may include:

* approved demonstration scenario;
* clearly labelled demonstration dataset;
* demonstration version reference;
* environment and access instructions;
* live walkthrough;
* recorded walkthrough where appropriate;
* resulting product records;
* resulting lifecycle and evidence records;
* Operator journey evidence;
* Investor journey evidence;
* reviewer checklist;
* repeat-run evidence where required;
* known-limitations statement;
* demonstration outcome record.

The demonstration must show observable product behaviour. Presentation slides, scripts, screenshots, diagrams, or verbal explanations may support the demonstration but cannot replace functioning product behaviour and resulting reviewable records.

Demonstration Evidence must distinguish clearly between:

* demonstration data;
* internal product records;
* Testnet records;
* external authoritative records;
* real operational or financial evidence.

Demonstration records must not be presented as:

* live Investor funding;
* real pilot expenditure;
* audited accounting;
* bank-confirmed payment;
* production settlement;
* verified or guaranteed investment returns.

A recorded walkthrough must identify the demonstrated version and environment. Where the recording is edited, the edit must not conceal failed steps, missing functionality, or material limitations.

### 14.6 Documentation Evidence

Documentation Evidence demonstrates that the delivered product can be understood, reviewed, operated within its approved scope, and compared with its governing requirements.

It may include:

* product documentation;
* technical documentation;
* API documentation;
* architecture documentation;
* Operator guidance;
* Investor or reviewer guidance;
* demonstration instructions;
* release record;
* known-limitations record;
* Deliverable register;
* traceability matrix;
* documentation review record;
* approval record.

Documentation used as Verification Evidence must:

* describe the delivered product accurately;
* identify the applicable version or baseline;
* distinguish current capabilities from planned capabilities;
* distinguish demonstration behaviour from production architecture;
* preserve the approved financial and non-production boundaries;
* remain consistent with product behaviour and repository evidence;
* identify material limitations.

Documentation does not prove implementation merely because it describes a capability. An implementation claim must remain supported by product, repository, test, deployment, or demonstration evidence as applicable.

Planned functionality must not be presented as implemented. Historical Legacy Testnet Alpha behaviour must not be presented as the target production financial architecture.

### 14.7 Work Package Evidence

Every Work Package must have an independently reviewable Work Package Evidence Record.

The record must include:

* Work Package identifier and title;
* Development Scope classification;
* Work Package objective;
* delivered outputs;
* related Deliverables;
* Acceptance Criteria assessment;
* Verification Evidence index;
* dependency status;
* applicable test or review results;
* defects and findings;
* unresolved issues;
* accepted exceptions or limitations;
* relevant budget status at the approved reporting level;
* related Milestone;
* completion recommendation;
* formal completion or non-completion decision.

The record must distinguish between:

* activity performed;
* output produced;
* output verified;
* output accepted.

A Work Package must not be reported as complete when:

* a mandatory Deliverable is incomplete;
* required Verification Evidence is missing;
* a dependency remains unresolved;
* an unresolved issue invalidates the intended result;
* applicable Acceptance Criteria have not been assessed.

Work Package evidence remains independently reviewable even when several Work Packages contribute to the same Deliverable or Milestone.

Completion of one Work Package does not establish completion of another.

### 14.8 Milestone Reporting Package

Each Development Milestone requires a formal Milestone Reporting Package.

The package must include:

* Milestone identifier and title;
* Milestone objective;
* included Work Packages;
* Work Package completion status;
* required Deliverables;
* Deliverable completion status;
* Verification Evidence index;
* Exit Criteria assessment;
* dependency status;
* defects and security findings;
* risks and exceptions;
* accepted limitations;
* budget and variance summary at the approved reporting level;
* contingency or reallocation information relevant to the Milestone;
* formal completion recommendation;
* formal decision and decision authority.

Each Work Package and Deliverable must use one of the approved reporting statuses:

* **Not Started** — no approved delivery activity or output exists;
* **In Progress** — approved work has begun, but completion requirements are not satisfied;
* **Blocked** — progress or verification cannot continue because of an unresolved dependency or condition;
* **Incomplete** — work or review occurred, but one or more completion requirements remain unsatisfied;
* **Conditionally Complete** — outputs are substantially complete, but a specifically documented and approved condition remains;
* **Complete** — all applicable completion requirements have been satisfied and formally recognised.

Conditionally Complete is not equivalent to Complete. A mandatory condition must be resolved before it can support final Beta Candidate acceptance unless the later acceptance governance explicitly permits and documents the remaining condition.

A Milestone report must not conceal:

* failed checks;
* skipped verification;
* incomplete Deliverables;
* blocked dependencies;
* unresolved defects;
* budget variance;
* accepted exceptions;
* scope changes.

The formal Milestone decision must be one of:

* Complete;
* Not Complete;
* Conditionally Complete where permitted;
* Blocked.

Submission of the Milestone Reporting Package does not itself establish Milestone completion.

### 14.9 Final Delivery Report

The Development Round requires a Final Delivery Report after the Milestone evidence packages have been assembled.

The report must include:

* Development Round identification;
* reviewed product version and baseline;
* Development Objective assessment;
* Beta Candidate status;
* Development Scope status;
* Core Work Package status;
* Recommended and Optional Work Package activation and status;
* Minimum Deliverable status;
* Milestone completion status;
* Verification Evidence index;
* Acceptance Criteria assessment reference;
* total budget summary;
* Work Package and cost-category expenditure summary;
* material variance summary;
* contingency-use summary;
* budget-reallocation summary;
* funding and payment status where relevant;
* defects, risks, and exceptions;
* accepted limitations;
* unresolved issues;
* excluded-cost compliance statement;
* non-production boundary statement;
* formal acceptance position;
* readiness to proceed to a separate Operational Readiness Review.

The Final Delivery Report must distinguish clearly between:

* completed;
* verified;
* accepted;
* conditionally accepted;
* incomplete;
* planned;
* excluded.

It must not declare or imply:

* production readiness;
* Operational Readiness;
* Mainnet readiness;
* regulatory approval;
* live investment capability;
* production custody or settlement;
* Feedlot Pilot approval;
* Hissar Pilot approval;
* a Pilot GO decision;
* verified or guaranteed investment returns.

The Final Delivery Report may conclude that the Beta Candidate is ready to enter an Operational Readiness Review. It must not predetermine the result of that review.

### Evidence Quality Principles

Acceptable Verification Evidence must be:

* **Relevant** — directly connected to the requirement being assessed;
* **Attributable** — linked to an identifiable source, version, owner, or execution record;
* **Accessible** — available to the authorized reviewer in a usable form;
* **Reviewable** — sufficiently clear to support an independent evaluation of the claim;
* **Version-specific** — linked to the product version or baseline being assessed;
* **Environment-specific** — linked to the relevant environment where environment affects interpretation;
* **Complete enough** — sufficient to determine whether the applicable requirement is satisfied;
* **Consistent** — aligned with related repository, product, test, deployment, demonstration, and documentation records;
* **Integrity-protected** — protected against unsupported alteration through appropriate repository history, access control, hashes, immutable storage, signed records, or equivalent controls where proportionate;
* **Status-aware** — clear about whether the evidence is draft, current, superseded, historical, or accepted.

Evidence must also be classified according to its authority.

#### Primary evidence

Directly demonstrates the claimed product state or result, such as observable product behaviour, test results, system records, or an accepted deployed version.

#### Supporting evidence

Provides context or corroboration, such as commits, Pull Requests, screenshots, diagrams, explanations, or review notes.

#### External authoritative evidence

Originates from an appropriate external authority, such as a bank, payment provider, auditor, regulator, legal adviser, or signed contractual source.

#### Internal product records

Records created by AgriPartners systems. They may demonstrate internal workflow state but do not automatically prove an external legal, banking, accounting, or operational event.

#### Demonstration records

Records produced using controlled demonstration data. They demonstrate product behaviour but not live investment or agricultural activity.

An evidence item must not be represented as possessing greater authority than its source provides.

### Evidence Sufficiency Rule

Evidence is sufficient only when it enables the reviewer to determine whether the applicable requirement has been satisfied.

Evidence volume does not establish evidence quality. Large quantities of irrelevant, duplicated, outdated, or untraceable material do not compensate for missing primary evidence.

One artifact may support multiple requirements, but:

* every requirement must be explicitly mapped to the artifact;
* the supported relationship must be understandable;
* limitations of the artifact must remain visible;
* the artifact must remain applicable to the reviewed version and environment.

Where evidence conflicts, the conflict must be investigated and documented. The most favourable evidence must not be selected while contradictory material is omitted.

Absence of a recorded problem is not evidence that the requirement was satisfied.

### Exception and Limitation Reporting

All material exceptions, failed checks, unresolved defects, blocked dependencies, scope deviations, and accepted limitations must be documented.

Each exception or limitation record should identify:

* a unique identifier;
* affected Work Package, Deliverable, Milestone, or requirement;
* description;
* cause;
* impact;
* risk;
* current status;
* proposed resolution or compensating control;
* responsible owner;
* target resolution condition where applicable;
* whether verification may continue;
* whether acceptance remains possible;
* approving authority for any accepted limitation.

An exception must not be closed merely because it has been documented.

Accepted limitations must remain visible in:

* the relevant Work Package Evidence Record;
* the relevant Milestone Reporting Package;
* the Final Delivery Report;
* the release and known-limitations documentation where applicable.

Silence, omission, missing evidence, or lack of a recorded defect must not be treated as evidence that no issue exists.

### Verification Traceability

Every Verification Evidence item must remain within the following traceability chain:

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
        ↓
Acceptance Decision
```

No evidence item may be accepted without a clearly identified relationship to the requirement it supports.

The Traceability Matrix must allow an authorized reviewer to move in both directions:

* from a requirement to its supporting evidence;
* from an evidence item to the requirement and decision it supports.

### Relationship to Section 15

Section 14 defines the evidence used to verify Development Round results.

Section 15 defines the Completion and Acceptance Criteria against which that evidence is evaluated.

Evidence does not automatically produce acceptance.

Acceptance requires a documented decision based on:

* the applicable criteria;
* sufficient Verification Evidence;
* disclosed exceptions and limitations;
* satisfied governance requirements;
* the authorized acceptance process.

This Verification and Reporting Evidence framework is the official evidence standard for the Development Round. It ensures that completion claims are based on demonstrated and reviewable outcomes rather than activity, expenditure, unsupported statements, or presentation materials alone.
