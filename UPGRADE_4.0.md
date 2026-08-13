# BruceIRF 4.0 Upgrade - Release Notes

## 🚀 What's New

- **Base**: Bruce 1.16.1 firmware
- **Version**: 4.0 (upgraded from 3.5)
- **Features Preserved**:
  - Universal IR Remote (829 signals)
  - Universal RF Remote (13.275 files + rebuilt database)
  - RF+IR Dual Detector
  - CRASH DIAG diagnostics
  - RCA IR protocol fixes
  
## 📋 Upgrade Checklist

- [x] Platform upgraded to Bruce 1.16.1
- [x] Version bumped to 4.0
- [x] build.py naming convention updated
- [ ] Full compilation test (lilygo-t-embed-cc1101, m5stack-sticks3, m5stack-cardputer)
- [ ] Binary release generation
- [ ] Database zip files (Full + Lite)
- [ ] GitHub Release creation

## 📦 Build Targets (Primary)

1. `lilygo-t-embed-cc1101` ⭐ Primary
2. `m5stack-sticks3`
3. `m5stack-cardputer`
4. `esp32-c5-tft` (experimental)

## 🔧 Configuration

All configuration inherited from Bruce 1.16.1 with IR/RF modules preserved from 3.5.

---

Generated: 2026-08-13
