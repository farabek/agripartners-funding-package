# Canonical PDF Generation Record — v1.0 R1

- Publication: AgriPartners Development Round Funding Package
- Edition: Authoritative Master Edition
- Version: v1.0 R1
- Generation tool: LibreOffice Writer, headless PDF export
- Tool version: 25.8.7.3
- Build: 30742500f2d3eb4366ac312fa33d3dcabdb3eba5
- Source DOCX: `Master/AgriPartners_Development_Round_Funding_Package_AME_v1.0.docx`
- Source DOCX SHA-256: `1D1E8FC92D1BB2064C8B2B54EE8FF15AE06FBF3F0F8597B797CD57C58AED943A`
- Canonical PDF: `Master/AgriPartners_Development_Round_Funding_Package_AME_v1.0.pdf`
- Canonical PDF SHA-256: `0A4C194F7363E4F0D36B0BF028E89073D8F9A5B0ACBA386EDAA1D2A6D5B38030`
- Page count: 186
- Page size: US Letter

## Procedure

Run LibreOffice with a fresh isolated user profile:

```powershell
& 'C:\Program Files\LibreOffice\program\soffice.com' `
  '-env:UserInstallation=file:///C:/Temp/agripartners_r1_lo_profile' `
  --headless --convert-to pdf `
  --outdir '<repository>\Master' `
  '<repository>\Master\AgriPartners_Development_Round_Funding_Package_AME_v1.0.docx'
```

## Reproducibility Verification

A second export was generated with a separate fresh user profile. Both outputs contained 186 pages. Raster comparison at 110 DPI found zero differing pages across all 186 pages. The regenerated file is therefore content- and layout-equivalent to the packaged canonical PDF. Raw PDF bytes are not asserted to be deterministic because LibreOffice embeds generation metadata.

This v1.0 R1 record supersedes AP-FP-006 only for release-specific source and output hashes; AP-FP-006 remains an unchanged historical remediation control.
