# Email Spoof Detector 

This Python tool analyzes email headers to detect **spoofing attempts** based on domain mismatches in `From`, `Reply-To`, and `Return-Path` fields.

## Features
- Extracts and compares header domains
- Flags domain mismatch or suspicious sender info
- Reads raw headers from a `.txt` file
- Can be extended for DKIM/SPF/DMARC checking(Challenge)

---

## How It Works

- Parses email headers using Python's built-in `email.parser`.
- Extracts sender domains from `From`, `Reply-To`, and `Return-Path`.
- Compares domains against trusted sources.
- Prints potential spoofing alerts if inconsistencies are found.

---

## Files
- `email_spoof_detector.py` → Main logic for spoof detection
- `sample_email_header.txt` → Example email header (for testing)

---

## Run the Script

```bash
python email_spoof_detector.py
