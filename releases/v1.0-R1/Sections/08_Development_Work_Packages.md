## 8. Development Work Packages

Development Work Packages divide the approved Development Scope into controlled, independently manageable implementation units.

Each Work Package has a defined purpose, output, completion basis, dependency position, budget reference, and relationship to the approved Development Milestones.

Independent management does not mean that every Work Package can produce a complete Beta Candidate by itself. Work Packages may depend on one another and must operate collectively to achieve the Development Objective.

### 8.1 Work Package Governance

#### Work Package identification

Every Work Package must have:

* a unique identifier;
* a unique title;
* a defined scope classification: Core, Recommended, or Optional;
* a clearly stated purpose;
* one accountable ownership assignment under the approved delivery governance;
* a current status;
* a reference to the relevant Development Scope.

Identifiers defined in this section must remain stable throughout planning, delivery, reporting, verification, and acceptance.

#### Sequencing rules

Work Packages may depend on capabilities, decisions, or outputs produced by other Work Packages.

Sequencing must:

* respect material dependencies;
* reduce integration and delivery risk;
* preserve the approved Development Objective;
* protect completion of Core Work Packages;
* allow verification evidence to be produced at the appropriate stage;
* avoid treating unfinished dependencies as completed inputs.

Sequencing may be adjusted when necessary, but it must not redefine the Beta Candidate, expand the Development Scope, or weaken applicable Acceptance Criteria.

Parallel execution is permitted where dependencies, resources, controls, and verification responsibilities remain clear.

#### Scope change rules

A Work Package must remain within the Development Scope approved in Section 7.

A proposed change must identify:

* the reason for the change;
* the affected scope classification;
* the impact on Deliverables;
* the impact on dependencies;
* the impact on Acceptance Criteria and Verification Evidence;
* the impact on related Milestones;
* the applicable budget effect;
* any effect on Beta Candidate completion.

No Work Package may be expanded through informal implementation decisions.

Material scope changes require formal approval through the applicable Development Round governance process. Approved changes must preserve complete traceability and, where necessary, trigger a formal revision of this Funding Package.

#### Work Package completion rules

A Work Package is complete only when:

* all approved Deliverables are complete;
* all Acceptance Criteria are satisfied;
* the required Verification Evidence exists and is reviewable;
* applicable dependencies and blocking conditions are resolved;
* unresolved defects do not invalidate the intended outcome;
* the result remains within the approved product and non-production boundaries;
* completion has been formally recorded through the applicable review process.

Budget expenditure, engineering activity, elapsed time, code submission, or a demonstration alone does not establish completion.

A Work Package may be marked conditionally complete only where the remaining condition is explicitly documented, does not invalidate the completed output, and is accepted by the applicable governance authority. Conditional completion cannot be used to declare a related Milestone or the Beta Candidate complete when mandatory criteria remain unsatisfied.

#### Scope priority

Core Work Packages take priority over Recommended and Optional Work Packages.

Recommended work may proceed only while successful delivery of all Core Work Packages remains achievable. Optional work may proceed only under the activation rules established in Section 7.3.

Recommended or Optional outputs cannot compensate for an incomplete Core Work Package.

### 8.2 Mandatory Work Package Template

Every Development Work Package must use the following template.

#### Objective

Explains why the Work Package exists and how it contributes to the Development Objective and Beta Candidate.

#### Scope

Defines the body of work included within the Work Package and identifies the applicable Minimum, Recommended, or Optional Development Scope.

The Scope must also make important exclusions visible where confusion with another Work Package or a non-production capability is reasonably possible.

#### Deliverables

Identifies the tangible, reviewable outputs produced by the Work Package.

Deliverables must be capable of being verified and linked to the related Milestone.

#### Dependencies

Identifies earlier Work Packages, product foundations, external conditions, approvals, or inputs required for successful completion.

A dependency must not be treated as resolved without appropriate evidence.

#### Acceptance Criteria

Defines the conditions that must be satisfied before the Work Package can be considered complete.

Acceptance Criteria must describe outcomes rather than activity alone.

#### Verification Evidence

Identifies the evidence required to demonstrate that the Deliverables exist and the Acceptance Criteria have been satisfied.

Evidence may include product behaviour, system records, tests, review records, controlled demonstrations, documentation, deployment evidence, or other approved artifacts.

#### Budget

References the corresponding Development Budget allocation defined in Section 10.

A Work Package budget field must identify the applicable allocation but must not independently redefine the Development Budget or duplicate detailed financial calculations.

#### Related Milestone

Identifies the Development Milestone primarily supported by the Work Package.

A Work Package may contribute to more than one Milestone, but one primary relationship must remain identifiable.

### 8.3 Work Package Portfolio

The Development Round portfolio consists of Core, Recommended, and Optional Work Packages.

#### Core Work Packages

Core Work Packages are mandatory for completion of the Minimum Viable Development Scope.

##### WP-C01 — Project Expense Platform

**Objective:** Establish the complete user-visible Project Expense capability required by the Beta Candidate.

**Scope:** Project Expense initiation, context, supported lifecycle, status visibility, and connection to the existing financial workflow and accounting foundation.

**Deliverables:** A complete and reviewable Project Expense product capability operating within the approved Project, workflow, budget, category, currency, and Operator boundaries.

**Dependencies:** Verified Stage 2 financial workflow and Project Expense accounting foundations.

**Acceptance Criteria:** The supported Expense lifecycle functions coherently, preserves applicable financial controls, and can be followed through the product.

**Verification Evidence:** Product demonstration, lifecycle records, relevant tests, and acceptance review records.

**Budget:** Section 10 — Project Expense Platform allocation.

**Related Milestone:** Milestone 1 — Expense Platform Complete.

##### WP-C02 — Project Expense Authorization and Operational Controls

**Objective:** Ensure that Project Expense actions are available only to permitted product roles and remain subject to the approved operational controls.

**Scope:** Authentication context, role-appropriate actions, prohibited-action handling, responsibility separation, and enforcement of relevant Project Expense boundaries.

**Deliverables:** A reviewable authorization and control capability covering the supported Expense workflow.

**Dependencies:** WP-C01 and the existing authentication and role baseline.

**Acceptance Criteria:** Permitted actions succeed for the appropriate role, prohibited actions are consistently rejected, and required responsibility separation remains effective.

**Verification Evidence:** Authorization tests, prohibited-action evidence, role-based demonstrations, and review records.

**Budget:** Section 10 — Authorization and Operational Controls allocation.

**Related Milestone:** Milestone 1 — Expense Platform Complete.

##### WP-C03 — Operator Workspace

**Objective:** Provide an authorized Operator with one coherent product experience for managing the supported operational and Project Expense workflow.

**Scope:** Operator access to Project context, budgets, Expenses, permitted actions, evidence, lifecycle information, and operational reporting.

**Deliverables:** A functional Operator Workspace supporting the approved end-to-end operational scenario.

**Dependencies:** WP-C01 and WP-C02.

**Acceptance Criteria:** An authorized Operator can complete the supported workflow without relying on disconnected administrative tools or direct database intervention.

**Verification Evidence:** Operator journey demonstration, product records, role validation, and acceptance review.

**Budget:** Section 10 — Operator Workspace allocation.

**Related Milestone:** Milestone 2 — Operator Workspace Complete.

##### WP-C04 — Evidence Management

**Objective:** Connect Project Expenses and operational activity to supporting evidence within a controlled and reviewable product workflow.

**Scope:** Evidence association, classification, status, role-appropriate review, retention, and permitted disclosure.

**Deliverables:** An integrated evidence workflow supporting the approved Project Expense scenario.

**Dependencies:** WP-C01, WP-C02, and relevant Operator Workspace capabilities.

**Acceptance Criteria:** Required evidence can be associated with the correct record, reviewed according to product authority, and distinguished from external legal, banking, accounting, or blockchain authority.

**Verification Evidence:** Evidence records, product demonstrations, validation tests, disclosure checks, and acceptance records.

**Budget:** Section 10 — Evidence Management allocation.

**Related Milestone:** Milestone 3 — Evidence Layer Complete.

##### WP-C05 — Investor Transparency

**Objective:** Provide Investors with appropriate visibility into disclosed Project operations, Expenses, evidence, reporting, and lifecycle history.

**Scope:** Investor-facing Project Expense information, operational progress, status semantics, evidence availability, and disclosure controls.

**Deliverables:** A controlled Investor transparency experience connected to the supported operational workflow.

**Dependencies:** WP-C01, WP-C04, and applicable disclosure rules.

**Acceptance Criteria:** An authorized Investor can review the permitted information while restricted, internal, or unsupported information remains protected and accurately labelled.

**Verification Evidence:** Investor journey demonstration, disclosure tests, role-access evidence, and acceptance review.

**Budget:** Section 10 — Investor Transparency allocation.

**Related Milestone:** Milestone 4 — Investor Transparency Complete.

##### WP-C06 — Operational and Investor Reporting

**Objective:** Present operational activity, Project Expenses, evidence status, and lifecycle information in reviewable reports.

**Scope:** Minimum reporting required for Operator use, Investor review, demonstration, and Development Round verification.

**Deliverables:** Integrated reports supporting the approved Beta Candidate workflow.

**Dependencies:** WP-C01, WP-C03, WP-C04, and WP-C05.

**Acceptance Criteria:** Reports accurately represent the supported records, preserve applicable status distinctions, and do not imply audited or production-settled results.

**Verification Evidence:** Report outputs, source-record comparison, role-based review, and acceptance records.

**Budget:** Section 10 — Reporting allocation.

**Related Milestone:** Milestone 4 — Investor Transparency Complete.

##### WP-C07 — Demonstration Environment and Scenario

**Objective:** Provide a controlled, repeatable environment in which the complete Beta Candidate can be demonstrated and reviewed.

**Scope:** Demonstration environment, approved scenario, clearly labelled demonstration data, repeatable product journey, and resulting system records.

**Deliverables:** A reviewable end-to-end demonstration of the Beta Candidate.

**Dependencies:** WP-C01 through WP-C06.

**Acceptance Criteria:** A reviewer can follow the approved scenario through observable product behaviour without interpreting demonstration data as live investment or pilot activity.

**Verification Evidence:** Deployed or controlled review environment, demonstration record, scenario evidence, and reviewer checklist.

**Budget:** Section 10 — Demonstration Environment allocation.

**Related Milestone:** Milestone 5 — Beta Candidate Complete.

##### WP-C08 — Quality Assurance and Product Security

**Objective:** Establish that the Beta Candidate functions reliably within its approved scope and that relevant product controls have been evaluated.

**Scope:** Principal user journeys, regression protection, authorization behaviour, financial and evidence controls, critical-defect resolution, and Beta-appropriate product security review.

**Deliverables:** Verified quality and security evidence supporting Beta Candidate acceptance.

**Dependencies:** All product-facing Core Work Packages.

**Acceptance Criteria:** Required journeys and controls pass the approved verification process, and no unresolved critical defect prevents demonstration or invalidates the target workflow.

**Verification Evidence:** Test results, defect records, security review evidence, regression evidence, and closure review.

**Budget:** Section 10 — Quality Assurance and Product Security allocation.

**Related Milestone:** Milestone 5 — Beta Candidate Complete.

##### WP-C09 — Documentation, Delivery Evidence, and Acceptance Support

**Objective:** Ensure that the completed Beta Candidate can be operated, reviewed, reported, and assessed against the Funding Package.

**Scope:** Required technical and user documentation, demonstration guidance, delivery evidence, completion records, and acceptance support.

**Deliverables:** A complete review package connecting delivered capabilities to Deliverables, Milestones, Verification Evidence, and Acceptance Criteria.

**Dependencies:** All Core Work Packages.

**Acceptance Criteria:** Documentation reflects the delivered product accurately, evidence is traceable, non-production boundaries remain explicit, and the completion review can be conducted without unsupported claims.

**Verification Evidence:** Approved documentation, traceability records, delivery report, acceptance checklist, and review decision.

**Budget:** Section 10 — Documentation and Delivery allocation.

**Related Milestone:** Milestone 5 — Beta Candidate Complete.

#### Recommended Work Packages

Recommended Work Packages materially improve the value of the Beta Candidate but are subordinate to Core completion.

##### WP-R01 — Product Experience and Accessibility Enhancements

**Objective:** Improve the usability, clarity, responsiveness, and accessibility of the Operator and Investor experiences.

**Scope:** Navigation, information hierarchy, status communication, validation feedback, responsive behaviour, and accessibility improvements beyond minimum completion.

**Deliverables:** Improved user-visible product experience across the supported Beta Candidate workflow.

**Dependencies:** Relevant Core user-facing Work Packages.

**Acceptance Criteria:** Approved usability improvements function consistently without changing mandatory workflow or authorization boundaries.

**Verification Evidence:** Usability review, responsive checks, accessibility evidence, and updated demonstrations.

**Budget:** Section 10 — Product Experience Enhancement allocation.

**Related Milestone:** Milestone 5 — Beta Candidate Complete.

##### WP-R02 — Enhanced Reporting, Export, and Presentation

**Objective:** Improve the clarity and external review value of reporting and presentation capabilities.

**Scope:** Enhanced visual summaries, charts, exports, demonstration datasets, and audience-appropriate presentation views.

**Deliverables:** Improved reporting and presentation outputs built upon verified Core records.

**Dependencies:** WP-C05 and WP-C06.

**Acceptance Criteria:** Enhanced outputs remain consistent with source records, disclosure controls, and non-production positioning.

**Verification Evidence:** Report comparisons, export validation, presentation review, and acceptance records.

**Budget:** Section 10 — Enhanced Reporting and Presentation allocation.

**Related Milestone:** Milestone 5 — Beta Candidate Complete.

##### WP-R03 — Demonstration Reliability and Environment Enhancements

**Objective:** Improve the repeatability, stability, and reviewer accessibility of the demonstration environment.

**Scope:** Environment reliability, demonstration reset capability, review access, operational guidance, and supporting observability.

**Deliverables:** A more reliable and repeatable external review environment.

**Dependencies:** WP-C07 and WP-C08.

**Acceptance Criteria:** The demonstration can be repeated consistently without weakening security, data labelling, or product boundaries.

**Verification Evidence:** Repeat-run demonstrations, environment checks, operational records, and reviewer validation.

**Budget:** Section 10 — Demonstration Reliability allocation.

**Related Milestone:** Milestone 5 — Beta Candidate Complete.

#### Optional Work Packages

Optional Work Packages are not required for Development Round completion and may be activated only under the Optional Scope Activation Rules.

##### WP-O01 — Advanced Analytics and AI Assistance

**Objective:** Explore advisory capabilities that improve interpretation of operational reports, Expenses, or evidence.

**Scope:** Advanced analytics, trend or exception views, and optional AI-assisted summarization or consistency checks.

**Deliverables:** Clearly labelled advisory outputs that do not replace authorized decisions or establish evidence authority.

**Dependencies:** Completed and verified Core data, evidence, reporting, and authorization capabilities.

**Acceptance Criteria:** Outputs are accurate within the approved use case, remain advisory, disclose applicable limitations, and do not perform financial approval or autonomous decision-making.

**Verification Evidence:** Evaluation results, sample outputs, limitation review, and acceptance record.

**Budget:** Section 10 — Optional Analytics and AI allocation, if activated.

**Related Milestone:** Optional extension following Milestone 5.

##### WP-O02 — Extended Demonstration Coverage

**Objective:** Extend the review value of the Beta Candidate through additional approved scenarios or audience support.

**Scope:** Additional demonstration scenarios, localization, extended reporting formats, or non-financial integrations consistent with the approved boundaries.

**Deliverables:** One or more approved extensions to the Core demonstration experience.

**Dependencies:** Completed Core demonstration capability and formal Optional Scope activation.

**Acceptance Criteria:** The extension does not alter the Development Objective, delay Core completion, introduce live financial activity, or create unsupported product claims.

**Verification Evidence:** Extended scenario demonstration, boundary review, and acceptance record.

**Budget:** Section 10 — Optional Demonstration Extension allocation, if activated.

**Related Milestone:** Optional extension following Milestone 5.

#### Cross-Work-Package Dependencies

Dependencies must be managed according to the following principles:

* the Project Expense Platform and Authorization capabilities establish the controlled workflow foundation;
* the Operator Workspace depends on that controlled workflow;
* Evidence Management depends on the relevant Expense, authorization, and Operator context;
* Investor Transparency depends on approved operational records, evidence status, and disclosure controls;
* Reporting depends on verified source records and role-appropriate visibility;
* the complete demonstration depends on the integrated Core product experience;
* Quality Assurance and Product Security apply across all Core Work Packages;
* Documentation and acceptance evidence must reflect the delivered product rather than anticipated functionality;
* Recommended and Optional Work Packages remain subordinate to Core completion.

A dependency relationship does not transfer completion status. Every Work Package must satisfy its own Deliverables, Acceptance Criteria, and Verification Evidence requirements.

#### Traceability requirements

Every Work Package must remain traceable through the complete governance chain:

```text
Development Objective
        ↓
Beta Candidate
        ↓
Development Scope
        ↓
Work Package
        ↓
Deliverables
        ↓
Milestone
        ↓
Verification Evidence
        ↓
Acceptance Criteria
```

No Work Package may exist outside this chain.

If a proposed Work Package cannot demonstrate a direct contribution to the Development Objective and Beta Candidate, it must be excluded or processed through formal scope revision.

#### Budget discipline

Each Work Package must reference the corresponding allocation in Section 10 — Development Budget.

Work Package budget references must not:

* create an additional funding request;
* alter the approved Development Round amount;
* transfer resources across independent funding components;
* include Corporate Setup or Pilot Capital;
* treat expenditure as evidence of completion;
* duplicate or supersede the detailed Development Budget.

Any material budget reallocation must follow the applicable funding and scope-change governance while preserving successful completion of all Core Work Packages.

This Work Package portfolio is the governing implementation structure for the Development Round. Implementation activity must be assigned to an approved Work Package, remain within its scope, produce its Deliverables, satisfy its Acceptance Criteria, and generate the required Verification Evidence.
