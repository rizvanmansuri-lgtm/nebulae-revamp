# PDF Specification Extraction Guide

This guide explains how to extract product specifications from PDF datasheets and brochures to populate the `data/products.js` file.

## 🔄 Extraction Process

### 1. Extract Text from PDF

```bash
pdftotext -layout "DATASHEET.pdf" output.txt
```

Open the resulting text file and look for these sections:

### 2. Key Sections to Extract

#### General Specifications
- Model number
- Dimensions (L × W × H mm)
- Weight
- Package type
- Antenna type

```
Example: NLN500a
Dimensions: 16.0 × 32.6 × 3.5 mm
Antenna: External (u.FL connector)
Package: Surface Mount Module
```

#### Wireless/RF Characteristics
- Frequency bands (EU, US, India regions)
- Protocol(s) supported
- TX Power (Transmit Power)
- RX Sensitivity (for different spreading factors)
- RF Range (Line-of-Sight)
- Data Rate

```
Example: LoRa Module
Frequency Band: EU 863-870, US 902-928, IN 865 MHz
TX Power: +21 dBm (max, programmable)
RX Sensitivity (SF7): −122 dBm (125 kHz BW)
RX Sensitivity (SF12): −136 dBm (125 kHz BW)
RF Range (LoS): ~10 km
Data Rate: 0.013 to 17.4 kbit/s
```

#### Memory & Processor
- CPU model and speed
- Flash memory size
- RAM size
- Clock sources

```
Example:
Core: STM32WLE5JC Arm® Cortex®-M4 (48 MHz)
Flash: 256 KB
RAM: 64 KB
Clock: 32 MHz TCXO + 32 kHz RTC oscillator
```

#### Power & Environment
- Supply voltage range
- Operating temperature range
- Standby current (if available)
- Active current modes

```
Example:
Supply Voltage: 1.8V to 3.6V DC
Temp Range: −20°C to +75°C
Operating: Industrial Grade
```

#### Interfaces & I/O
- Number of I/O pins
- Voltage tolerance
- Debug interfaces (SWD, JTAG)
- Peripheral interfaces (SPI, I2C, UART)
- RF shielding details

```
Example:
I/O Pins: Up to 43 I/Os (5V-tolerant)
Debug: SWD (Serial-Wire Debug), JTAG
Peripherals: SPI, I2C, UART, LPUART
RF Shield: Integrated EM protection
```

#### Security & Features
- Encryption standard
- OTA (Over-The-Air) capability
- Certifications/Approvals
- Regulatory compliance

```
Example:
Encryption: AES 256-bit
OTA: Supported (firmware updates)
Regulatory: EU, US, India frequency band certified
```

### 3. Extract Images from PDF

```bash
# List images in PDF
pdfimages -list "BROCHURE.pdf"

# Extract all images as PNG
pdfimages -png "BROCHURE.pdf" assets/images/products/productname

# Find largest image (usually the product hero shot)
ls -lhS assets/images/products/productname-*.png
```

The largest image is typically the best for the product hero section.

## 📋 LoRa Module Extraction Example

### NLN500a - Extracted Sections

**From: NLN500a_Module_Datasheet_V2.2.pdf**

```
GENERAL
-------
Model: NLN500a
Chip: STM32WLE5JC
Dimensions: 16.0 × 32.6 × 3.5 mm
Antenna: External

RF CHARACTERISTICS
------------------
Transmit Power: +21 dBm
RX Sensitivity (1% PER):
  - SF7: −122 dBm (125 kHz BW)
  - SF12: −136 dBm (125 kHz BW)
RF Range: 10 km (Line-of-Sight)*
Frequency Band: EU 863-870, US 902-928, IN 865
Data Rate: 0.013 to 17.4 kbit/s

FUNCTIONAL CHARACTERISTICS
--------------------------
CPU: STM32WLE5JC Arm® Cortex®-M4, 48 MHz
Memory:
  - Flash: 256 KB
  - RAM: 64 KB
Clock Sources:
  - External HSE: 32 MHz TCXO
  - External 32 kHz oscillator for RTC

ELECTRICAL CHARACTERISTICS
---------------------------
Supply Voltage: 1.8V to 3.6V
Operating Temp: −20°C to +75°C

PIN DETAILS
-----------
I/O: Up to 43 I/Os, mostly 5V-tolerant
Debug: SWD, JTAG

FEATURES
--------
✓ Frequency bands support
✓ RX sensitivity −122 dBm (SF7), −136 dBm (SF12)
✓ High TX power up to +21 dBm
✓ AES 256-bit hardware encryption
✓ OTA firmware update capable
✓ RF shield for EM protection
```

### NLN500b - Extracted Sections

**From: NLN500b LoRa Module Datasheet 2.0.pdf**

```
GENERAL
-------
Model: NLN500b
Chip: STM32WLE5CBU6
Dimensions: 26.68 × 16.0 × 3.6 mm
Antenna: External (multiple options: u.FL, Feedline, Spring)

RF CHARACTERISTICS
------------------
Transmit Power: +21 dBm (programmable)
RX Sensitivity:
  - SF7: −123 dBm (125 kHz BW)
  - SF12: −136 dBm (125 kHz BW)
Frequency Band: EU 863-870, IN 865
Protocols: LoRaWAN®, Sigfox™

GENERAL FEATURES
----------------
Power Supply: 1.8V to 3.6V DC
Operating Temperature: −20°C to +75°C
Core: 32-bit Arm® Cortex®-M4 CPU
Hardware Encryption: AES 256-bit
Memory: 256 KB Flash, 64 KB RAM
OTA: Firmware update capable

PERIPHERALS & I/O
-----------------
I/O Pins: Up to 21 I/Os
Voltage Tolerance: 5V DC
Debug: SWD, JTAG
Interfaces:
  - I2C (1, programmable up to 3)
  - SPI (1, programmable up to 2)
  - UART (1)
  - LPUART (1)

VARIANTS (from ordering info)
-----------------------------
PL1N500BUF100 - u.FL connector
PL1N500BFL100 - Feedline
PL1N500SGL100 - Spring antenna
```

## 📐 Creating specs Object

After extraction, structure the data in `data/products.js`:

```javascript
specs: {
  general: {
    'Core Processor': 'STM32WLE5JC Arm® Cortex®-M4 32-bit RISC (48 MHz)',
    'Dimensions (L×W×H)': '16.0 × 32.6 × 3.5 mm',
    'Antenna': 'External (u.FL connector)',
    'Package': 'Surface Mount Module'
  },
  
  wireless: {
    'Frequency Band': 'EU 863-870 MHz, US 902-928 MHz, IN 865 MHz',
    'Protocol': 'LoRaWAN®',
    'TX Power': '+21 dBm (max, programmable)',
    'RX Sensitivity (SF7)': '−122 dBm (125 kHz BW)',
    'RX Sensitivity (SF12)': '−136 dBm (125 kHz BW)',
    'RF Range (LoS)': '~10 km',
    'RF Data Rate': '0.013 to 17.4 kbit/s'
  },
  
  memory: {
    'Flash Memory': 'Up to 256 KB',
    'RAM': 'Up to 64 KB',
    'Clock Source': '32 MHz TCXO (external HSE), 32 kHz oscillator for RTC'
  },
  
  power: {
    'Supply Voltage': '1.8V to 3.6V DC',
    'Operating Temp Range': '−20°C to +75°C',
    'Hardware Encryption': 'AES 256-bit',
    'OTA Capable': 'Yes (over-the-air firmware update)'
  },
  
  interfaces: {
    'I/O Pins': 'Up to 43, most 5V-tolerant',
    'Available on Module': 'Edge plated holes for direct soldering',
    'Debug Interface': 'Serial-wire debug (SWD), JTAG',
    'RF Shield': 'Integrated protection from EM radiation'
  }
}
```

## 🎯 Formatting Tips

### Specifications
- Use consistent units (mm, MHz, dBm, mA, KB, etc.)
- Include full range values: "1.8V to 3.6V" not just "3.3V"
- Use proper symbols: "−" (minus) not "-", "®" for trademarked
- Group related specs in the same section

### Features & Applications
- Keep to bullet-point style
- Start each with action word: "Supports", "Offers", "Up to", "Programmable", etc.
- Avoid redundancy (don't repeat from specs)
- Focus on use-case benefits

Example:
```javascript
features: [
  'Frequency Band: Supports EU 863-870, US 902-928, IN 865 frequency bands',
  'RX sensitivity −122 dBm (SF7) and −136 dBm (SF12)',
  'High TX power up to +21 dBm',
  '1.8V to 3.6V power supply',
  '−20°C to +75°C operating temperature range',
  '32-bit Arm® Cortex®-M4 CPU',
  'Hardware AES 256-bit encryption',
  // ... more features
]
```

## 🔗 Document Cross-Reference

Ensure `documents` section references exact filenames in `data/docs.js`:

```javascript
documents: {
  cat: 'lora',              // Category in DOCS array
  subcat: 'module',         // Subcategory in DOCS array
  datasheets: [
    'NLN500a_Module_Datasheet_V2.2.pdf'  // Exact filename
  ],
  brochures: [
    'NLN500a LoRa Module Brochure.pdf'   // Exact filename
  ]
}
```

Then in `data/docs.js`:

```javascript
{
  filename: 'NLN500a_Module_Datasheet_V2.2.pdf',  // Matches above
  cat: 'lora',                                     // Matches cat
  subcat: 'module',                                // Matches subcat
  type: 'datasheet',
  // ... other fields
}
```

## 🖼️ Image Extraction Tips

### Find the Best Product Image

1. List all images: `pdfimages -list brochure.pdf`
2. Extract largest (usually hero image): `pdfimages -png brochure.pdf prefix`
3. Check file sizes: `ls -lh prefix-*.png`
4. Use the largest one (e.g., `prefix-002.png`)

### Image Placement

In `data/products.js`:

```javascript
image: '/assets/images/products/nln500a-002.png',      // Card thumbnail
heroImage: '/assets/images/products/nln500a-002.png'   // Hero section
```

Both can reference the same image or different ones.

## ✅ Validation Checklist

Before building, verify:

- [ ] Model number matches datasheet
- [ ] All frequency bands included (EU, US, IN)
- [ ] TX/RX power values correct
- [ ] Dimensions format: "L × W × H mm"
- [ ] Temp range uses "−" (minus sign) not "-"
- [ ] All referenced PDFs exist in `data/docs.js`
- [ ] Image paths are correct
- [ ] No inline styles (use CSS classes)
- [ ] Variants SKUs match datasheet
- [ ] Meta description under 160 chars
- [ ] Slug is kebab-case

## 🔄 Batch Processing Multiple PDFs

For extracting specs from multiple PDFs at once:

```bash
#!/bin/bash
# extract_all_specs.sh

for pdf in *.pdf; do
  echo "=== $pdf ===" >> specs.txt
  pdftotext -layout "$pdf" - | grep -A 50 "Specification\|Technical Data\|Overview" >> specs.txt
  echo "" >> specs.txt
done

# Review specs.txt in editor and copy-paste into data/products.js
```

---

**Remember**: The goal is clean, structured data in `data/products.js`. Once data is correct, the build script automatically generates beautiful, SEO-friendly HTML pages.
