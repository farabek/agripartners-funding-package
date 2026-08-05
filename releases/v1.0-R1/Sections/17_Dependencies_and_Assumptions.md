## 17. Dependencies and Assumptions

This section defines the conditions, resources, systems, and planning premises upon which successful completion of the Development Round depends.

A **Dependency** is a prerequisite or supporting condition required for delivery, verification, or acceptance.

An **Assumption** is a planning premise accepted for the purpose of preparing the Development Round but remaining subject to validation where material.

An Assumption is not evidence and must not be presented as a completed fact.

Collectively, the identified Dependencies and Assumptions define the planning conditions under which the Development Objective is considered achievable.

### Dependency Status

Dependencies should be classified as:

* **Established** — already present and supported by the approved baseline;
* **Required during delivery** — must remain available or be satisfied during the Development Round;
* **External or conditional** — depends on a funder, provider, partner, or other external party;
* **Future-phase dependency** — required for Corporate Setup, Operational Readiness, production, or a real Pilot, but not for Beta Candidate completion.

A future-phase dependency must not be treated as a current Development Round blocker unless a specific funding agreement makes it a commencement or payment condition.

### Dependency Register

Material Dependencies must be recorded in a controlled Dependency Register.

Each record should identify:

* a stable Dependency ID;
* title and description;
* dependency category;
* current status;
* affected Work Packages, Deliverables, or Milestones;
* responsible owner;
* internal or external source;
* required condition;
* evidence of satisfaction where applicable;
* validation or review date;
* consequence of failure;
* escalation or reassessment requirement.

The Dependency Register is a control record. It does not replace the underlying evidence demonstrating that a Dependency has been satisfied.

### 17.1 Internal Product Dependencies

The Development Round begins from established product and governance foundations.

#### Verified Alpha baseline

The Development Round depends on the current verified AgriPartners Alpha platform remaining available as the starting product baseline.

The established baseline includes:

* public and demonstration experiences;
* Investor, Farmer, and administrative product experiences;
* wallet authentication;
* reporting and lifecycle visibility;
* Treasury and Presentation Mode capabilities;
* backend API;
* PostgreSQL database;
* NEAR Testnet integration;
* existing testing and documentation foundations.

This dependency is established through the approved Current Product Baseline in Section 4.

#### Financial Workflow Foundation

The Development Round depends on the completed Stage 2 Financial Workflow Foundation.

This foundation provides the approved database basis for:

* Project financial workflows;
* Operator representation and assignment;
* fiat-only Operator transfers;
* financial states and lifecycle history;
* evidence references;
* financial-control boundaries.

The Development Round extends this foundation. It does not redefine it.

#### Project Expense Accounting Foundation

The Development Round depends on the completed Stage 2 Project Expense Accounting Foundation.

This foundation provides:

* workflow budgets;
* Project Expenses;
* Expense categories;
* immutable Expense lifecycle events;
* evidence references;
* derived reservations;
* responsibility separation;
* concurrency and overspending controls.

The existing foundation must remain consistent and available throughout the Development Round.

#### Approved product architecture

Delivery depends on preservation of the approved product and financial architecture, including:

* AgriPartners OÜ as the future central company and Investor counterparty;
* cryptocurrency stopping at the Estonia layer;
* fiat-only Uzbekistan-facing financial operations;
* Farmer and Uzbekistan Operator roles remaining non-crypto;
* NEAR records remaining supplementary to legal, banking, accounting, and reconciliation authority.

A material architectural change would require formal reassessment rather than informal expansion of a Work Package.

#### Approved governance framework

The Development Round depends on the continued authority of:

* the Development Objective;
* Beta Candidate definition;
* Development Scope;
* Work Package portfolio;
* Deliverable catalogue;
* Development Budget;
* Milestone framework;
* Verification Evidence framework;
* Completion and Acceptance Criteria.

These established elements form the internal governance basis for execution.

### 17.2 Technical Dependencies

Technical Dependencies are the product capabilities and system conditions required to integrate, verify, and demonstrate the Beta Candidate.

#### Backend capability

The Development Round depends on the existing backend remaining available as the application service foundation for authentication, profiles, Projects and Deals, reporting, administration, financial workflows, and Project Expense integration.

#### Frontend capability

The existing browser application must remain available as the user-visible foundation for Operator, Investor, reporting, and demonstration experiences.

#### Database consistency

The PostgreSQL schema and ordered migration history must remain consistent with the accepted financial and Project Expense foundations.

Database changes must preserve:

* workflow ownership;
* lifecycle integrity;
* evidence relationships;
* budget controls;
* reservations;
* concurrency protection;
* historical records.

#### Authentication and authorization context

The current authentication and role baseline must remain available while the Beta Candidate adds the approved Project Expense authorization capability.

Product roles must remain distinguishable from legal, contractual, corporate, banking, or payment authority.

#### Workflow integration

The Beta Candidate depends on a consistent relationship among:

* Project context;
* financial workflow;
* workflow budget;
* Project Expense;
* Expense lifecycle;
* evidence;
* Operator actions;
* reporting;
* Investor disclosure.

Failure of this relationship would prevent the integrated Beta Candidate outcome even if individual components existed separately.

#### Reporting and evidence context

The reporting and evidence capabilities depend on accurate source records, consistent lifecycle semantics, and role-appropriate disclosure.

Reports and product records must preserve distinctions among projected, recorded, approved, paid, reconciled, and completed states.

#### Controlled deployment capability

The accepted Beta Candidate depends on a controlled environment in which the approved version and end-to-end scenario can be reviewed.

This is a development and demonstration dependency, not a production infrastructure dependency.

### 17.3 Infrastructure Dependencies

The Development Round requires sufficient infrastructure to support development, verification, documentation, and controlled demonstration.

Required infrastructure may include:

* development environments;
* source repository availability;
* branch and Pull Request workflows;
* testing environments;
* safe disposable database verification;
* build and deployment tooling;
* controlled demonstration hosting;
* test or demonstration databases;
* access control for review environments;
* documentation storage;
* Evidence Register storage;
* logs and monitoring appropriate to Beta verification;
* backup or retention of required evidence.

Infrastructure must support:

* reproducible product review;
* version identification;
* evidence preservation;
* authorized reviewer access;
* protection of credentials and sensitive data.

The Development Round does not depend on production banking, production payment infrastructure, production custody, Mainnet operation, or live agricultural infrastructure.

A temporary provider interruption may delay affected verification or demonstration activity without redefining the Development Objective or completed Scope.

### 17.4 Funding Dependencies

Successful completion depends on sufficient financing for the full approved Minimum Viable Development Scope.

#### Availability of the Development Budget

The principal funding dependency is availability of the approved **USD 40,000 Development Budget** or a legally committed financing structure sufficient to complete the full Beta Candidate.

The Development Round must not rely on an uncommitted future funding gap.

#### Agreed funding mechanism

Before commencement, the applicable funding mechanism must be sufficiently defined, including:

* single-tranche or multi-tranche structure;
* eligible expenditure;
* reporting requirements;
* payment conditions;
* commencement conditions;
* currency and payment process;
* any permitted budget variance;
* any funder approval requirements.

#### Multi-tranche funding

Where funding is released by Milestone, the full financing commitment and tranche conditions must preserve the ability to complete the approved Core Scope.

A completed early tranche must not create an unfunded obligation to complete the entire Beta Candidate.

#### Delayed funding

Where committed funding is delayed, commencement or continued delivery may be adjusted. Unfunded work is not assumed.

Funding delay does not reduce the approved Scope or allow an incomplete result to be represented as complete.

#### Partial funding

Partial funding is not sufficient for the complete Development Round unless:

* the remaining capital is legally committed; or
* a separately approved, independently valuable funding phase is defined before expenditure begins.

#### Funder compliance

Completion also depends on compliance with applicable funder requirements, including:

* cost eligibility;
* reporting;
* procurement where applicable;
* evidence access;
* Milestone review;
* payment conditions.

A funder-specific requirement may change the format of the funding request or reporting package. It must not silently redefine the Development Objective or Beta Candidate.

### 17.5 External Dependencies

#### NEAR Ecosystem Dependencies

The current platform uses NEAR Testnet for wallet-linked Alpha workflows, smart-contract experimentation, selected references, and demonstration capabilities.

Relevant Development Round Dependencies may include:

* NEAR Testnet availability;
* wallet and access-key functionality;
* supported wallet tooling;
* relevant NEAR development libraries;
* Testnet account and transaction availability;
* ecosystem documentation and tooling.

The Beta Candidate does not require NEAR Mainnet operation.

Uzbekistan-facing Operator and Farmer financial workflows must not depend on NEAR, cryptocurrency, wallets, tokens, or on-chain actions.

A temporary Testnet or wallet-provider interruption may affect verification of the retained Testnet capabilities. It must not redefine the fiat-only product boundary or convert Mainnet operation into Development Scope.

No NEAR ecosystem grant, partnership, endorsement, or future technical support is assumed unless formally confirmed.

#### Estonia-related Dependencies

AgriPartners OÜ is part of the approved future corporate and financial architecture.

The Development Round’s technical product objective does not inherently require completion of Estonian incorporation before product development can occur.

Estonia-related conditions may become external Dependencies where a specific funder requires:

* a registered legal entity before signing;
* an eligible corporate recipient before payment;
* an Estonian account or corporate representation;
* company documentation before commencement.

Such requirements must be confirmed for each funder rather than assumed universally.

#### Corporate Setup Dependencies

Corporate Setup is governed separately from the USD 40,000 Development Budget.

AgriPartners may apply as a founder or team where the relevant programme permits application before incorporation.

Where company registration is required after conditional approval but before agreement or payment, the dependency sequence may be:

```text
Founder or Team Application
        ↓
Conditional Approval or Equivalent Decision
        ↓
Corporate Setup Funding
        ↓
AgriPartners OÜ Registration
        ↓
Funding Agreement
        ↓
Development Funding
```

Corporate Setup is expected to be required for later corporate contracting, banking, KYB, Operational Readiness, and real Pilot operations.

It is not a technical prerequisite for building the Beta Candidate and is not a prerequisite for every founder-first application.

Corporate Setup must not be represented as completed until the relevant legal and administrative evidence exists.

#### External Provider Dependencies

The Development Round may depend on third-party services such as:

* repository hosting;
* development tooling;
* application hosting;
* database hosting;
* domain or certificate services;
* wallet tooling;
* documentation services;
* monitoring or logging services;
* specialist QA, security, accessibility, or product review.

Provider availability does not guarantee successful delivery. Material provider changes, service discontinuation, pricing changes, or access restrictions may require reassessment.

No specific provider relationship should be presented as secured unless supported by an agreement or active service record.

#### Feedlot Operator Dependencies

The Beta Candidate uses approved agricultural workflow and demonstration context but does not require commencement of real Feedlot operations.

Development may rely on:

* approved Feedlot model documentation;
* controlled demonstration data;
* established operational categories;
* available domain input where formally included.

A real Uzbekistan Feedlot Operator, executed Operator agreement, live bank transfer, livestock acquisition, or operational agricultural activity is not required for Beta Candidate completion unless a formally approved scope revision states otherwise.

Operator identity, contractual authority, operational capacity, and Pilot readiness remain future-phase Dependencies for Operational Readiness and the real Feedlot Pilot.

The same principle applies to the future Hissar Pilot.

### 17.6 Assumptions Requiring Validation

The following planning Assumptions support Development Round preparation but remain subject to confirmation.

#### Funding assumption

It is assumed that the complete USD 40,000 Development Budget will be secured or legally committed before AgriPartners undertakes the full delivery obligation.

This is not evidence that funding has been obtained.

#### Funder eligibility assumption

It is assumed that the selected funder can support the approved product-development purpose and that the final budget can be adapted to its eligible-cost rules without invalidating Core Scope.

This must be validated for each funding source.

#### Corporate Setup timing assumption

It is assumed that at least some founder-first funding sources will permit application before AgriPartners OÜ is registered and will require incorporation only before agreement, payment, or implementation.

This must be confirmed through the rules and written guidance of each programme.

#### Product baseline assumption

It is assumed that the verified current baseline remains available and does not undergo an unapproved material architectural change before Development Round commencement.

Any material change requires a baseline and scope reassessment.

#### Delivery-capacity assumption

It is assumed that suitable product, engineering, QA, security, documentation, and specialist capacity can be engaged under the approved budget and funding conditions.

No specific contractor or provider is assumed to be committed without supporting evidence.

#### Infrastructure assumption

It is assumed that appropriate repository, development, testing, deployment, and documentation infrastructure will remain available on commercially and operationally reasonable terms.

#### Demonstration-data assumption

It is assumed that controlled demonstration data can support the approved end-to-end scenario without requiring live Investor funds, personal data, real agricultural expenditure, or production payment activity.

#### NEAR Testnet assumption

It is assumed that NEAR Testnet and the necessary supporting tooling remain sufficiently available for the retained Testnet demonstration capabilities.

This assumption does not extend to Mainnet.

#### Operational Readiness assumption

It is assumed that the completed Beta Candidate may become eligible for a separate Operational Readiness Review.

It is not assumed that the review will produce a GO decision.

#### Corporate and partner participation assumption

It is assumed that future Corporate Setup, service-provider relationships, Operator participation, legal preparation, and financial infrastructure may be pursued through separate governance and funding.

None is assumed completed or contractually secured.

#### Pilot funding assumption

It is assumed that Feedlot and Hissar Pilot funding will be pursued separately.

Development Round completion does not establish that either Pilot will be financed or approved.

## Dependency Principles

Dependencies:

* identify conditions required for successful delivery, verification, or acceptance;
* must remain visible and attributable;
* must have an identifiable status;
* must be reassessed when materially changed;
* may affect one or more Work Packages, Deliverables, or Milestones.

Dependencies do not:

* guarantee successful delivery;
* prove that implementation occurred;
* substitute for Verification Evidence;
* replace Acceptance Criteria;
* establish Corporate Setup;
* establish Operational Readiness;
* guarantee funding, provider support, or partner participation.

A Dependency is considered satisfied only when appropriate evidence confirms the required condition.

## Assumption Principles

Assumptions:

* support planning;
* reduce unnecessary repetition;
* remain explicitly identifiable;
* must not be presented as verified facts;
* require validation where material;
* must identify the consequence of invalidation where relevant.

If a material Assumption is invalidated, the affected Work Packages, Deliverables, Milestones, budget, schedule, and risks must be reassessed through the applicable governance process.

An invalidated Assumption must not be concealed through scope relabelling or unsupported completion claims.

## Dependency Traceability

Dependencies must remain traceable through:

```text
Development Objective
        ↓
Beta Candidate
        ↓
Development Scope
        ↓
Work Package
        ↓
Dependency
        ↓
Verification Evidence
        ↓
Acceptance
```

Dependencies support delivery. They do not replace delivery.

## Relationship to Risks

Dependencies and risks are related but distinct.

* **Dependencies** identify required conditions.
* **Risks** evaluate uncertainty, likelihood, impact, and controls associated with possible events or failures.

A Dependency is not automatically a risk.

Failure, delay, degradation, or invalidation of a critical Dependency may create or increase a Development Round risk. Such risk must be assessed under Section 18 — Risks and Controls.

This section is the governing Dependency and Assumption framework for the Development Round. It distinguishes established foundations, active delivery conditions, external dependencies, and planning assumptions without presenting any of them as evidence of completion, Corporate Setup, Operational Readiness, Pilot approval, or future funding success.
