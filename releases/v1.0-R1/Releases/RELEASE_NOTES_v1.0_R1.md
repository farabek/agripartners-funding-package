# Release Notes — v1.0 R1

## Release Summary

AgriPartners Development Round Funding Package, Authoritative Master Edition, Version v1.0 R1 is the administratively finalized publication release following the successful CTO Final Review.

Release status: **RELEASE AUTHORIZED**  
QA disposition: **PASS WITH NON-BLOCKING WARNING — RELEASE AUTHORIZED**

## Publication Scope

The release contains the Master Markdown, DOCX, and PDF; Sections 1–21; Appendices A–J; governance and publication-control documents; QA evidence; release controls; manifests; and SHA-256 checksums.

Version v1.0 R1 introduces release metadata and archival controls only. Approved substantive content—including budget, Milestones, governance, funding strategy, and Acceptance Criteria—has not changed.

## Completed QA

The complete publication QA covered archive structure, section and appendix completeness, terminology, cross-references, Milestone and budget consistency, DOCX and PDF rendering, canonical PDF reproducibility, manifest and checksum integrity, placeholder detection, and publication-status accuracy.

Sections 1–21 and Appendices A–J in this repository are byte-identical to the successfully reviewed remediation package. Governance controls AP-FP-001 through AP-FP-006 are also byte-identical; AP-FP-007 is a new publication-style control.

## Remediation Summary

The preceding controlled remediation corrected severe table-rendering failures, established a canonical PDF-generation procedure, aligned Appendix C with authoritative Section 13, and corrected premature publication-status claims. The CTO Final Review subsequently authorized release with one non-blocking monetary-notation warning.

AP-FP-007 records `USD 40,000` and `$40,000` as approved equivalent representations unless a future publication style explicitly standardizes one notation. This closes the remaining warning administratively without changing approved content.

## Canonical PDF Generation

- Tool: LibreOffice Writer headless export
- Version: 25.8.7.3 (build 30742500f2d3eb4366ac312fa33d3dcabdb3eba5)
- Source DOCX: `Master/AgriPartners_Development_Round_Funding_Package_AME_v1.0.docx`
- Procedure: isolated user profile; `soffice.com --headless --convert-to pdf --outdir <Master> <source-docx>`
- Result: 186 pages, US Letter
- Canonical PDF SHA-256: `0A4C194F7363E4F0D36B0BF028E89073D8F9A5B0ACBA386EDAA1D2A6D5B38030`
- Reproducibility result: 186 of 186 pages raster-equivalent; zero page-level pixel differences at 110 DPI. Raw PDF hashes may differ because the renderer embeds generation metadata.

## Appendix C Correction

Appendix C remains the corrected derived matrix and conforms to Section 13’s five mandatory Milestones: Expense Platform Complete, Operator Workspace Complete, Evidence Layer Complete, Investor Transparency Complete, and Beta Candidate Complete. It does not redefine the Milestone framework.

## SHA Verification

- Master Markdown SHA-256: `5DDFD25AE44E5E15EBAE2C67EEC8B5AF455898A108F173D08D8D06D81DA130D6`
- Master DOCX SHA-256: `1D1E8FC92D1BB2064C8B2B54EE8FF15AE06FBF3F0F8597B797CD57C58AED943A`
- Master PDF SHA-256: `0A4C194F7363E4F0D36B0BF028E89073D8F9A5B0ACBA386EDAA1D2A6D5B38030`

The release payload manifest and checksum file are stored under `Manifest/`. Archive-specific integrity metadata is stored under `Archive/`.

## Repository Boundary

This release was prepared only in the standalone `agripartners-funding-package` documentation repository. The product repository `farabek/agripartners` was not modified.
