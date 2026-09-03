# How the USD 40,000 Development Budget Works

Language: **English** · [Русский](BUDGET_EXPLAINED_RU.md) ·
[Corporate Setup costs](CORPORATE_SETUP_BUDGET.md) ·
[Feedlot Pilot](FEEDLOT_PILOT_EXPLAINED.md) · [Hissar Pilot](HISSAR_PILOT_EXPLAINED.md) ·
[Funding sources and status](FUNDING_SOURCES_AND_STATUS.md) ·
[Funding Package home](../README.md) ·
[Official budget](../releases/v1.0-R1/Sections/10_Development_Budget.md) ·
[Permitted use of funds](../releases/v1.0-R1/Sections/11_Use_of_Funds.md)

## The short explanation

AgriPartners already has a working Alpha prototype. The USD 40,000 Development
Round finances the work required to turn it into one complete, testable, and
reviewable **Pilot Operations & Investor Evidence Beta Candidate**.

It does not finance livestock, farm construction, agricultural operations,
company formation, banking infrastructure, or either physical pilot.

## What will be built

This simplified view combines related official Work Packages into outcomes that
are easier to understand. It does not replace or change the official budget.

| Product outcome | Amount | What it means in practice |
| --- | ---: | --- |
| Expense system and financial controls | $11,000 | An Operator can record expenses; the system checks permissions, lifecycle rules, and budget limits |
| Operator workspace | $6,500 | An authorized Operator can manage the supported workflow in one coherent interface |
| Expense documents and evidence | $4,000 | Receipts and supporting evidence can be connected to the correct expense and protected by access rules |
| Investor transparency and reporting | $6,500 | An Investor can review permitted project activity, expenses, evidence availability, and reports |
| Demonstration environment | $2,500 | Reviewers can see the complete workflow with controlled demonstration data |
| Quality, security, and delivery documentation | $6,500 | The result is tested, security-checked, documented, and supported by completion evidence |
| Controlled contingency | $3,000 | Reserved only for approved unforeseen work required to complete mandatory scope |
| **Total** | **$40,000** | **A complete and reviewable Beta Candidate** |

The amounts above are a plain-language grouping of the official Work Package
allocations:

- Expense system and controls: BA-01 ($6,500) + BA-02 ($4,500).
- Investor transparency and reporting: BA-05 ($4,000) + BA-06 ($2,500).
- Quality, security, and documentation: BA-08 ($4,500) + BA-09 ($2,000).
- All other rows correspond directly to BA-03, BA-04, BA-07, and BA-10.

## Why the official package has two budget tables

They are two views of the **same USD 40,000**, not two budgets.

### Table 1: product results

The Work Package table answers:

> What must be built and verified with the money?

It connects every allocation to a product component, deliverable, and
milestone. A funder can use it to decide whether promised value was delivered.

### Table 2: cost categories

The internal cost-category table answers:

> What kinds of work and resources are paid for while building it?

Those categories include backend engineering, frontend work, integration, QA,
security, documentation, specialists, and development infrastructure.

### How the two views connect

```text
Product result: Expense Platform
             ↓
Work required: backend + frontend + integration + QA + documentation
             ↓
Evidence: working functionality + tests + records + acceptance
```

One product result may require several cost categories. One cost category may
support several product results. Every actual expense must therefore be tagged
to both one approved Work Package and one approved cost category.

## The five completion stages

1. **Expense Platform Complete** — expense lifecycle, authorization, and
   financial controls work correctly.
2. **Operator Workspace Complete** — the Operator can use that capability
   through an integrated workspace.
3. **Evidence Layer Complete** — evidence is connected to expenses and governed
   by access and disclosure rules.
4. **Investor Transparency Complete** — permitted information and reporting are
   available to the Investor without exposing restricted data.
5. **Beta Candidate Complete** — the complete scenario is integrated, tested,
   security-checked, deployed, documented, and reviewable.

Spending money, writing code, or presenting a demo does not by itself complete
a stage. The required deliverables, tests, evidence, exit criteria, and formal
acceptance must all exist.

## What the USD 40,000 cannot pay for

- livestock, feed, farm construction, or agricultural working capital;
- the USD 50,000 Feedlot Pilot or USD 50,000 Hissar Sheep Pilot;
- incorporation of AgriPartners OÜ;
- general legal, accounting, regulatory, or banking readiness;
- production custody, settlement, Mainnet deployment, or live investments;
- unrelated business expenses or unapproved scope expansion.

## What the funder receives

The funder receives a measurable product-development outcome with traceability
from budget to Work Packages, deliverables, milestones, tests, deployment, and
completion evidence. The result is a Beta Candidate ready for a separate
Operational Readiness Review—not a claim that live investment or a physical
pilot has already been authorized.

## Which document is authoritative?

This guide is explanatory. If wording here conflicts with the frozen Funding
Package, the official v1.0 R1 sections control, especially:

- [Section 10 — Development Budget](../releases/v1.0-R1/Sections/10_Development_Budget.md)
- [Section 11 — Use of Funds](../releases/v1.0-R1/Sections/11_Use_of_Funds.md)
- [Section 13 — Development Milestones](../releases/v1.0-R1/Sections/13_Development_Milestones.md)
