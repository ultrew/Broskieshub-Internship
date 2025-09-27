# Task 7 — Static Malware Analysis
## Internship: Broskieshub.com 
## Overview
I performed a static analysis of the provided sample ( which I created using ai ) without executing it. All work was done on my Kali host using `strings`, `hexdump`, Ghidra, and VirusTotal (hash lookup only). This README explains what I checked, what I found, and how to reproduce my steps.
 
---

## Files I included
- `Evidence/malware` — the ELF sample I analyzed
- `Evidence/malware.c` — source used to build the sample
- `Evidence/hashes.txt` — recorded SHA256 / SHA1 / MD5
- `Evidence/strings_output.txt` — `strings` output
- `Evidence/hexdump_head.txt` — hexdump excerpt showing embedded marker
- `Evidence/file_type.txt`, `Evidence/readelf_header.txt`, `Evidence/objdump_full.txt` — file metadata
- `Malware_project.zip` - ghidra malware project in zip format
- `Screenshots/` — minimal screenshots: hashes, key strings, hexdump MZ offset, Ghidra strings, Ghidra decompile, VirusTotal lookup

---

## Summary of findings
- **File type:** ELF 64-bit LSB PIE executable, x86-64, stripped.
- **Hashes:**  
  - SHA256: `70daf232c4baa313714d241fb5e8adc2458d34f94a895757379a915ab6c497e3`  
  - SHA1: `ae6c836e8a68f77eac712f08d81d0fced006cbc9`  
  - MD5: `79463907f988db78e7f383669cc422e7`
- **Key indicators:**  
  - I found an ASCII `MZ` sequence inside the ELF (suggests an embedded PE-like blob).  
  - Found suspicious literal strings `ThisLooksLikePE|cmd.exe /c whoami /all|CONNECT_BACK` and a base64-like fragment `UEsDBBQAAAAI`.  
  - Ghidra shows these strings in the Defined Strings pane and they are referenced by `main()`; the ELF binary itself contains no obvious socket or process-launching imports.

---

## How I reproduced (commands I ran)
> Run these in a controlled environment.

```bash
# go to the folder containing the extracted Task7 files
cd ./Task7/Evidence

# compute hashes
sha256sum malware | tee hashes.txt
sha1sum malware >> hashes.txt
md5sum malware  >> hashes.txt
cat hashes.txt

# extract readable strings
strings -a -n 4 malware | tee strings_output.txt

# hexdump to inspect bytes and find embedded MZ
hexdump -C malware | less
# quick locate MZ occurrences (prints byte offsets in decimal)
grep -b -a -o $'\x4d\x5a' malware

# file metadata / headers
file malware > file_type.txt
readelf -h malware > readelf_header.txt
objdump -x malware > objdump_full.txt

# manually inspect in Ghidra:
# - ghidraRun
# - File -> New Project -> Import ./malware -> run auto-analysis
# - Window -> Defined Strings (look for MZ/cmd/CONNECT_BACK)
# - Open main() and press F for decompiled pseudocode
````
---

## Screenshots I included

I included only the essential screenshots in `Screenshots/`:

0. `00_listing_after_compile.png` - Compilation of binary
1. `01_hashes.png` — hash outputs
2. `02_strings.png` — `strings` output with the suspicious literals
3. `03_hexdump.png` — hexdump showing `MZ` offset `0x2008`
4. `04_file_info.png` - file info
5. `05_defined_strings.png` — Ghidra defined strings pane
6. `06_function_and_imports.png` — Ghidra decompiled `main()` and imports
7. `07_virus_total.png` — VirusTotal hash lookup result


## Safety note

I did **not** execute the sample. I only performed static inspection. I recommend doing any dynamic or hostile-sample work inside isolated VMs or dedicated sandbox infrastructure.

---

1. **What is malware analysis?**
   The process of examining malicious software to understand its functionality, origin, and potential impact.

2. **What is static vs dynamic analysis?**

   * **Static analysis**: Examining malware without executing it (e.g., strings, disassembly).
   * **Dynamic analysis**: Observing malware behavior while executing in a controlled environment.

3. **How can you identify malicious strings in a file?**
   By extracting and analyzing readable strings (e.g., suspicious URLs, IPs, API calls) that may indicate malicious intent.

4. **What does VirusTotal do?**
   It scans files and URLs with multiple antivirus engines and provides detection results and threat intelligence.

5. **What are file hashes used for?**
   To uniquely identify files, verify integrity, and detect known malware samples.

6. **What is reverse engineering?**
   The process of deconstructing a program to understand its structure, functionality, and behavior.

7. **What are IOCs (Indicators of Compromise)?**
   Artifacts such as IPs, domains, file hashes, or registry keys that indicate malicious activity.

8. **What is Ghidra and how is it used?**
   Ghidra is an open-source reverse engineering tool used for analyzing compiled code through disassembly and decompilation.

9. **How can you tell if a file is obfuscated?**
   Indicators include unreadable strings, junk code, unusual control flow, or encryption of code/data.

10. **What is the danger of opening unknown files?**
    They may execute malicious code, leading to system compromise or data theft.


---

End of report.
