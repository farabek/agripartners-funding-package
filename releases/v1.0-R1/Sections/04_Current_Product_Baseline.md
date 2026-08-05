## 4. Current Product Baseline

This section establishes the verified starting point for the Development Round.

The baseline was reviewed against the current main branch of the public farabek/agripartners repository at commit:

2d46df862f49346e876d9bb16a75d4714c69a9c8

The repository classifies the current product as AgriPartners Alpha v1.2 — working prototype on NEAR Testnet.

AgriPartners is beyond the concept stage: it contains an implemented browser application, backend API, PostgreSQL database model, role-based workflows, NEAR Testnet integration, demonstration capabilities, executable tests, and maintained technical and product documentation.

The current baseline is not a production investment platform. It does not accept live investments and does not provide production custody, banking, payment execution, crypto-to-fiat conversion, KYC/KYB, Mainnet settlement, or live agricultural pilot operations.

4.1 Product Capabilities
Public and demonstration experience

The current frontend provides an implemented public-facing product experience, including:

a public landing page;
an Alpha opportunity catalog;
Project and Deal presentation views;
Feedlot and Hissar demonstration profiles;
audience-specific Presentation Mode;
guided Investor, NEAR ecosystem, accelerator, and enterprise demonstrations.

Presentation Mode can be reviewed without configuring a backend, database, wallet, or Testnet funds. It is a demonstration capability and does not represent a live investment offering.

Feedlot and Hissar profiles use demonstration data derived from the approved Master Investment Models. Their displayed activity, projected economics, recorded returns, and lifecycle states are not evidence of deployed capital, audited performance, or production settlement.

Investor experience

The Investor Portal is implemented and demonstrable for Alpha-stage workflows.

It provides:

opportunity and Project review;
investor profile and portfolio views;
projected economic information with Alpha-stage status framing;
Project progress and reporting visibility;
recorded return information;
withdrawal-readiness and lifecycle presentation;
access to Farmer-submitted reports where supported by the current workflow.

The Investor experience demonstrates how relevant Project information may be organized and disclosed. It does not provide live investor onboarding, KYC/KYB, production capital intake, custody, banking, or production settlement.

Projected, recorded, paid, and reconciled values remain distinct concepts. Alpha return records are demonstration and workflow-validation records rather than audited or production-settled performance.

Farmer experience

The Farmer Portal is implemented and demonstrable as an Alpha product workflow.

It currently supports:

Farmer role and profile records;
access to assigned Deals;
funding-status visibility;
Production Cycle visibility;
operational progress reporting;
funding confirmation;
report submission;
access controls based on the current Alpha identity model.

Some current Farmer flows retain wallet-linked, NEAR-funding, withdrawal, and smart-contract behavior from the Legacy Testnet Alpha. These capabilities are historical technical demonstrations and are not the target production financial architecture.

Under the approved target model, the Farmer is a fiat-only, non-crypto product role. The current repository has not yet completed the implementation migration required to remove all Farmer wallet and crypto dependencies.

Administrative experience

The current Alpha includes administrative routes and product controls for managing platform records and selected lifecycle actions.

The administrative experience supports aspects of:

Deal and Project preparation;
participant and role coordination;
lifecycle monitoring;
reporting oversight;
return and treasury record visibility;
selected administrative actions;
Alpha-stage access control.

Current application roles and administrative permissions do not establish legal signing authority, payment authority, corporate mandate, or production-grade segregation of duties.

Reporting and lifecycle visibility

The current platform includes implemented reporting and lifecycle capabilities across Investor, Farmer, and administrative experiences.

These include:

Farmer progress reports;
Production Cycle records;
Deal and Project lifecycle events;
recorded return information;
operational status visibility;
role-filtered access to relevant information.

The platform can demonstrate how operational activity becomes visible across participant roles. It does not yet provide the complete evidence-linked Project Expense workflow planned for the Beta Candidate.

Treasury visibility

The Treasury Dashboard and Treasury Shadow Accounting capabilities are implemented for Alpha-stage visibility and demonstration.

They show how capital activity, return records, and selected operational events may be organized and presented. Treasury Shadow Accounting is non-authoritative and does not replace bank records, accounting records, contracts, reconciliation evidence, or production treasury controls.

Wallet authentication and NEAR Testnet demonstration

Wallet-signature authentication is implemented and verified within the Alpha environment.

The current platform also demonstrates selected NEAR Testnet capabilities, including:

wallet-linked authentication;
smart-contract experimentation;
contract status and balance reads;
selected lifecycle and transaction actions;
recording of Testnet transaction references;
presentation of blockchain-supported transparency concepts.

These capabilities are limited to NEAR Testnet. They do not constitute audited smart contracts, Mainnet readiness, production custody, production payments, or authoritative evidence that a fiat transaction occurred.

4.2 Technical Baseline
Application architecture

The current application uses a hybrid browser, API, database, and Testnet architecture:

Browser application
        |
        v
Node.js / Express REST API
        |
        v
PostgreSQL database

Wallet-signed messages and selected Legacy Alpha actions
        |
        v
NEAR Testnet

The frontend is a Vite-built single-page application using JavaScript, HTML, and CSS. It uses hash-based routing and provides public, Investor, Farmer, administrative, Treasury, and Presentation Mode experiences.

The backend is a Node.js and Express REST API. Its current responsibilities include:

authentication;
role-scoped access;
profiles;
Deals and Projects;
Farmer cycles and reports;
investor views;
administrative actions;
return records;
treasury visibility;
database access and migrations;
selected NEAR Testnet interactions.

PostgreSQL is the operational application data store. Ordered SQL migrations are the schema authority.

Authentication baseline

The Alpha contains two implemented authentication paths:

legacy username-and-password authentication using role-bearing JWTs;
wallet-signature authentication using wallet-linked JWTs.

The wallet flow uses a backend-issued challenge, a signed NEAR message, access-key verification, and a time-limited JWT.

This is an Alpha authentication baseline. It is not a completed production identity, KYC/KYB, legal-authority, or corporate-mandate system. Existing limitations include Testnet-specific configuration, process-local authentication elements, browser-accessible token storage, and continued wallet dependency in Legacy Farmer flows.

NEAR technical baseline

The repository contains NEAR Testnet integration using near-api-js and Rust smart-contract code using near-sdk.

The current integration supports Testnet experimentation with wallet authentication, contract deployment and initialization, selected state reads, lifecycle actions, funding or withdrawal demonstrations, and transaction references.

Farmer withdrawal, Farmer NEAR balances, smart-contract payouts, and related signer behavior remain Legacy Testnet Alpha functionality. They must not be presented as the approved production financial model.

Under the approved architecture, any future NEAR audit and automation infrastructure must remain on the External Investor and AgriPartners OÜ Estonia side. Uzbekistan-facing Operator and Farmer workflows must remain fiat-only.

Financial Workflow Foundation

Stage 2 Slice 1 — Financial Workflow Foundation is completed and merged.

Migration 016 establishes a database foundation for:

Uzbekistan Operator representation;
Operator, Farmer, and Deal assignment;
one financial workflow per Deal;
Estonia-layer crypto-conversion records;
fiat-only Operator transfer records;
financial evidence references;
immutable financial state events;
controlled financial-state transitions;
idempotency protections;
separation between instruction and authorization;
event-backed state projections.

The modeled workflow distinguishes Investor funding, crypto conversion where applicable, fiat clearing, Operator disbursement, Operator confirmation, Project expense recording, returned proceeds, reconciliation, and Investor settlement.

These are implemented database structures and constraints. They do not execute production conversion, banking, payments, custody, or settlement.

Project Expense Accounting Foundation

Stage 2 Slice 2 — Project Expense Accounting Foundation is completed and merged.

Migration 017 establishes database support for:

approved expense categories;
financial workflow budgets;
Project Expenses;
immutable Project Expense lifecycle events;
Project Expense evidence references;
expense states including REQUESTED, APPROVED, REJECTED, CANCELLED, and PAID;
requester, approver, and payer separation;
authoritative fiat-payment evidence requirements;
derived budget reservations;
budget capacity controls;
overspending protection;
concurrency-safe approval behavior;
linkage between paid Project Expenses and financial workflow events;
preservation of historical workflow records.

Project Expense reservations are derived rather than independently editable. Budget reductions cannot reduce available capacity below existing reservations. A paid Project Expense requires the relevant approved state and authoritative fiat-payment evidence reference.

This foundation is implemented and verified at the PostgreSQL layer. It is not yet exposed as a complete user-facing product workflow.

Testing and verification baseline

The repository contains executable backend tests using Jest and Supertest, together with migration-specific and PostgreSQL runtime verification.

Repository evidence includes tests for:

authentication;
wallet authentication;
Investor routes;
Farmer routes and reporting;
profiles and onboarding;
NEAR services;
financial workflow migration behavior;
Project Expense accounting migration behavior;
Project Expense runtime behavior;
concurrency and competing transitions;
budget reductions and overspending controls;
migration repeat-run behavior;
rollback and immutable history.

The Project Expense runtime tests use a disposable PostgreSQL verification harness with safeguards intended to prevent execution against production, staging, shared, or otherwise important databases.

The repository also contains a GitHub Actions workflow configured to run backend tests and build the frontend for pushes and pull requests targeting main.

This baseline review confirms the presence of the tests, verification harness, and CI configuration in the repository. It does not claim that the complete test suite was independently rerun as part of preparing this Funding Package section.

Repository and documentation baseline

The repository has reached Repository Documentation Ready v1.

The maintained documentation baseline includes:

a canonical Platform Model;
accepted high-level Architecture;
Product Book and documentation navigation;
approved operating and financial models;
documented Estonia-to-Uzbekistan fiat boundary;
software delivery roadmap;
release documentation;
pilot planning and readiness materials;
legal and contractual planning documents;
documentation authority and governance rules.

Current code, migrations, configuration, and executable tests remain authoritative for implemented behavior. Documentation defines approved architecture and operating boundaries but does not convert planned capabilities into implemented functionality.

The latest reviewed main commit contains the Repository Documentation Ready v1 merge. The canonical Platform Model retains the earlier Stage 2 implementation checkpoint as its technical evidence reference.

Planned but unimplemented capabilities

The following capabilities are not part of the current verified baseline:

Project Expense API;
application-level Project Expense authorization service;
Operator expense interface or dashboard;
complete evidence submission and review workflow;
complete Investor Project Expense transparency experience;
integrated expense reporting and export layer;
completed fiat-only Farmer and Operator product migration;
non-wallet production authentication for Uzbekistan-facing roles;
production-grade identity and authority controls;
dedicated contract registry;
dedicated verified legal-entity registry;
production KYC/KYB;
electronic-signature infrastructure;
bank or payment-provider integration;
live crypto-to-fiat conversion;
production fiat disbursement or repayment execution;
production reconciliation;
production investor settlement;
production custody;
stablecoin accounting;
audited Mainnet smart contracts;
Mainnet deployment;
production operational readiness;
live Feedlot or Hissar pilot operations.

These items must not be described as completed product capabilities.

The current product should therefore be represented as an implemented and demonstrable Alpha platform with verified financial and Project Expense database foundations. It should not be represented as a completed Beta, production platform, regulated investment platform, live payment system, or operational agricultural pilot.
