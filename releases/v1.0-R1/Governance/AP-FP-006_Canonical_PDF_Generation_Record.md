# Canonical PDF Generation Record

**Edition:** 1.0-R1  
**Generation date:** 5 August 2026  
**Source DOCX:** `Master/AgriPartners_Development_Round_Funding_Package_AME_v1.0.docx`  
**Generation tool:** LibreOffice Writer headless PDF export  
**Tool version:** LibreOffice 25.8.7.3, build `30742500f2d3eb4366ac312fa33d3dcabdb3eba5`  
**Output PDF:** `Master/AgriPartners_Development_Round_Funding_Package_AME_v1.0.pdf`  
**Page count:** 186 US-Letter pages  
**Canonical PDF SHA-256:** `028c3d45b17ecfc262acc291c9b589980da2971055b5afd020a315ac66e5d034`

## Canonical procedure

Use a new, empty LibreOffice user profile for every export:

```powershell
& 'C:\Program Files\LibreOffice\program\soffice.com' `
  --headless `
  '-env:UserInstallation=file:///C:/Temp/agripartners_canonical_profile' `
  --convert-to pdf `
  --outdir '<output-directory>' `
  'Master\AgriPartners_Development_Round_Funding_Package_AME_v1.0.docx'
```

The generated PDF is then copied byte-for-byte into the `Master` directory and its SHA-256 value is recorded in the Manifest and checksum list.

## Reproducibility verification

A second export from the same DOCX, using the same LibreOffice build and a separate empty profile, produced:

- 186 US-Letter pages;
- zero differing page raster hashes across all 186 pages at 72 DPI; and
- identical extracted content and layout expectations.

The two raw PDF file hashes differ because LibreOffice writes the export timestamp into PDF metadata. The canonical release byte sequence is the PDF identified by the SHA-256 value above. Visual/layout reproducibility is established by zero page-raster differences, not by expecting timestamp-bearing PDF containers to be byte-identical.
