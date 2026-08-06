![Bruce Main Menu](./media/pictures/bruce_banner.jpg)

# :shark: BruceIRF — Universal IR + RF firmware

**BruceIRF** is a fork of the official [Bruce](https://github.com/BruceDevices/firmware) ESP32 firmware focused on **Infrared (IR)** and **Sub-GHz RF**. It keeps the full standard Bruce 1.16 feature set and adds two complete modules — **UniversalIR** and **UniversalRF** — plus a rebuilt RF database.

> Based on the official **Bruce 1.16** release. All credit for the base firmware goes to the Bruce team. This fork only adds the IR/RF functionality described below.

---

## :sparkles: What's new in BruceIRF

- :satellite: **Univ. RF Remote** — a complete Sub-GHz browser: categories → brands → signals. Reads Flipper Zero `.sub` files (RAW + BinRAW Key format) through the standard Bruce RF pipeline.
- :bulb: **Univ. IR Remote** — the Universal IR browser (categories, brands, signal grids, spam replay).
- :wrench: Built-in **Generic test category** (no database required) — Carrier 433 / 315 / 868 MHz, OOK Keyfob (Princeton), Doorbell 433 MHz — to verify your RF module in seconds.
- :label: **Brands flow + readable labels** — raw names like `RAW-RECORDING-0001` show as "Recording 0001", underscores/dashes become spaces.
- :card_file_box: **Rebuilt RF Full database** — every useful source category restored, brute-force families reorganized under the category they attack (CAME / NICE / Chamberlain / Linear → Garages, OOK / deBruijn → Gates, Holtek, Tesla → Vehicles...).
- :zap: **RF+IR Dual Detector** — captures on the first band that fires, external RF (CC1101 / M5 RF433) and IR module selectors, SD-gated Save, replay loop.
- :hammer: **RCA IR protocol fix** (TCL & compatible TVs), crash fixes (heap exhaustion on huge RAW files, shared-SPI mutex between CC1101 and display), onboard **CRASH DIAG** diagnostic screen.

---

## :computer: Supported boards

| Board | File |
|---|---|
| **LilyGO T-Embed CC1101** :star: (primary, validated) | `BruceIRF3.0-lilygo-t-embed-cc1101.bin` |
| **M5StickS3** :new: (first release) | `BruceIRF3.0-m5stack-sticks3.bin` |

The firmware `.bin` files are **merged full images** (bootloader + partitions + firmware) — ready to flash as-is.

---

## :rocket: Install — flashing

Flashing is done with **M5Launcher** or **ESP Web Tool** (EspWebTool). There is no need for anything else.

### M5StickS3 — M5Launcher
1. Copy `BruceIRF3.0-m5stack-sticks3.bin` to your M5StickS3's SD card (or load it over WiFi in M5Launcher).
2. Boot the device into **M5Launcher** and select the `BruceIRF3.0-m5stack-sticks3.bin` file to flash.
3. The device reboots straight into BruceIRF.

### Any ESP32-S3 board — ESP Web Tool (EspWebTool)
1. Connect the board via USB.
2. Open the ESP Web Tool (EspWebTool) in Chrome/Edge.
3. Select the matching `BruceIRF3.0-<board>.bin`, set the flash address to `0x0`, and flash.
4. Done — no extra drivers, works on Windows / Linux / macOS.

> The official Bruce Web Flasher (https://bruce.computer/flasher) works too.

---

## :open_file_folder: Install — IR + RF database

The database ships as two archives (IR + RF together):

| Archive | Content | Use for |
|---|---|---|
| `BruceIR3.0-UniversalIR-RF-Full.zip` | IR 829 + RF 13.275 files (~156 MB) | **SD card** users (T-Embed) |
| `BruceIR3.0-UniversalIR-RF-Lite.zip` | IR 7 + RF 103 files | **LittleFS** (no-SD boards, M5StickS3) |

- **SD card:** extract the archive onto your SD card so you get the folders `UniversalIR` and `UniversalRF`.
- **LittleFS:** upload the archive contents into LittleFS using Bruce's Web UI → File Manager.

The modules find the folders **both at the storage root and inside a single wrapper folder** (some file managers extract the archive into a folder named after the `.zip`) — no manual moving needed.

---

## :video_game: Usage

- **IR → Univ. IR Remote** — browse IR categories/brands, open a signal grid, SEL sends.
- **RF → Univ. RF Remote** — browse RF categories/brands (`.sub` files), SEL sends.
- **RF → Generic** (first entry, always present) — built-in test signals: Carrier 433/315/868 MHz, OOK Keyfob, Doorbell 433 MHz.
- **RF+IR Dual** (Main Menu) — capture RF and IR at the same time; options to pick the RF module (CC1101 / M5 RF433) and the external IR receiver pin.

Navigation: Prev/Next wrap, Up/Down move by column, SEL selects/sends (debounced), ESC backs out, "Back" / "Main Menu" entries.

---

## :hammer_and_wrench: Building from source

```bash
pio run -e lilygo-t-embed-cc1101 -t build-firmware
pio run -e m5stack-sticks3 -t build-firmware
```

Build outputs (merged bins) are written to the project root. See `AGENTS.md` (kept out of this repo) for the full build/development notes.

---

## :pushpin: Notes / status

- **T-Embed** is the primary, validated target.
- **M5StickS3** is a first release awaiting real-hardware validation (UI + external CC1101/IR capture).
- Report issues with the on-screen **CRASH DIAG** task + backtrace — it makes debugging much faster.

## :scroll: License

The base firmware is licensed by the Bruce team — see the upstream [Bruce repository](https://github.com/BruceDevices/firmware). This fork inherits the same licensing for the base code; the additions are provided as-is.
