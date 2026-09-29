/**
 * PRODUCTS Data Array
 * Structured product data for Nebulae IoT products
 * Matches with DOCS array for downloads/datasheets
 */

const PRODUCTS = [
  {
    // LoRa Module - NLN500a
    id: 'nln500a',
    model: 'NLN500a',
    name: 'NebuLink Module NLN500a',
    category: 'Module',
    protocol: 'LoRa',
    description: 'The first and smallest STM32WL-based LoRa module, designed for long-range, low-power IoT applications. Built on the STM32WLE5JC SoC with embedded LoRaWAN transceiver, it offers secure data transmission for M2M and industrial IoT use cases.',
    shortDesc: 'Smallest STM32WL-based LoRa module for long-range IoT',
    image: './assets/images/products/nln500a-002.png',
    heroImage: './assets/images/products/nln500a-002.png',
    
    // Specifications
    specs: {
      general: {
        'Core Processor': 'STM32WLE5JC Arm® Cortex®-M4 32-bit RISC (48 MHz)',
        'Dimensions (L×W×H)': '16.0 × 32.6 × 3.5 mm',
        'Weight': 'TBD',
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
    },

    // Key Features (bullet-point summary)
    features: [
      'Supports EU 863-870, US 902-928, IN 865 frequency bands',
      'RX sensitivity −122 dBm (SF7) and −136 dBm (SF12)',
      'High TX power up to +21 dBm',
      '1.8V to 3.6V power supply',
      '−20°C to +75°C operating temperature range',
      '32-bit Arm® Cortex®-M4 CPU',
      'Hardware AES 256-bit encryption',
      'OTA firmware update capable',
      'Up to 256 KB Flash & 64 KB RAM',
      'Serial-wire debug (SWD) & JTAG support',
      'Up to 43 I/Os (5V-tolerant)',
      'Direct solder capability',
      'RF shield for EM protection'
    ],

    // Applications
    applications: [
      'Building automation & monitoring',
      'Lighting controls',
      'Inventory management',
      'Environmental monitoring',
      'Security systems',
      'Industrial monitoring & machinery condition tracking',
      'Plant system parameters monitoring (temperature, pressure, flow, tank level, humidity, vibration)',
      'Smart metering & lighting solutions',
      'Smart flood sensors',
      'Smart street lighting',
      'Smart city networks',
      'Smart waste management'
    ],

    // Documents (matching with DOCS array cat/subcat)
    documents: {
      cat: 'lora',
      subcat: 'module',
      datasheets: ['NLN500a_Module_Datasheet_V2.2.pdf'],
      brochures: ['NLN500a LoRa Module Brochure.pdf']
    },

    // Product variants/ordering info
    variants: [
      {
        sku: 'NLN500a-STD',
        name: 'Standard',
        description: 'Standard NLN500a module with external antenna connector'
      }
    ],

    // URLs & Meta
    slug: 'lora-module-nln500a',
    metaDescription: 'NLN500a LoRa module - smallest STM32WL based LoRa module for long-range IoT applications with −122 dBm RX sensitivity and +21 dBm TX power.',
    metaKeywords: 'LoRa module, STM32WL, IoT, LoRaWAN, low-power, Nebulae'
  },

  {
    // LoRa Module - NLN500b
    id: 'nln500b',
    model: 'NLN500b',
    name: 'NebuLink Module NLN500b',
    category: 'Module',
    protocol: 'LoRa',
    description: 'The compact STM32WL-based LoRa module supporting both LoRaWAN® and Sigfox™ protocols. Engineered for long-range, low-power M2M and IoT applications with enhanced features and regulatory certifications.',
    shortDesc: 'Dual-protocol LoRa/Sigfox module for industrial IoT',
    image: './assets/images/products/nln500b-000.png',
    heroImage: './assets/images/products/nln500b-000.png',

    // Specifications
    specs: {
      general: {
        'Core Processor': 'STM32WLE5CBU6 Arm® Cortex®-M4 32-bit RISC (48 MHz)',
        'Dimensions (L×W×H)': '26.68 × 16.0 × 3.6 mm',
        'Weight': 'TBD',
        'Antenna': 'External (multiple mounting options: u.FL, Feedline, Spring)',
        'Package': 'Surface Mount Module'
      },
      wireless: {
        'Frequency Band': 'EU 863-870 MHz, IN 865 MHz',
        'Protocols': 'LoRaWAN®, Sigfox™',
        'TX Power': '+21 dBm (max, programmable)',
        'RX Sensitivity (SF7)': '−123 dBm (125 kHz BW)',
        'RX Sensitivity (SF12)': '−136 dBm (125 kHz BW)',
        'RF Data Rate': 'Varies by protocol'
      },
      memory: {
        'Flash Memory': 'Up to 256 KB',
        'RAM': 'Up to 64 KB'
      },
      power: {
        'Supply Voltage': '1.8V to 3.6V DC',
        'Operating Temp Range': '−20°C to +75°C',
        'Hardware Encryption': 'AES 256-bit',
        'OTA Capable': 'Yes (over-the-air firmware update)'
      },
      interfaces: {
        'I/O Pins': 'Up to 21 I/Os',
        'I/O Voltage Tolerance': '5V DC',
        'Debug Interface': 'Serial-wire debug (SWD), JTAG',
        'Peripherals': 'I2C (1, up to 3 programmable), SPI (1, up to 2 programmable), UART (1), LPUART (1)',
        'RF Shield': 'Integrated EM radiation protection'
      }
    },

    // Key Features (bullet-point summary)
    features: [
      'Frequency Band: EU 863-870 MHz, IN 865 MHz',
      'RX Sensitivity −123 dBm (SF7) and −136 dBm (SF12)',
      'TX Output Power up to +21 dBm (programmable)',
      'Dual Protocol Support: LoRaWAN® and Sigfox™',
      'Power Supply: 1.8V to 3.6V DC',
      'Operating Temperature: −20°C to +75°C',
      'Core: 32-bit Arm® Cortex®-M4 CPU',
      'Hardware Encryption: AES 256-bit',
      'Memory: 256 KB Flash, 64 KB RAM',
      'OTA Firmware Update Capability',
      'Programming/Debug: SWD & JTAG',
      'Up to 21 I/Os with 5V tolerance',
      'Direct solder capability',
      'Integrated RF shield',
      'Multiple antenna mounting options'
    ],

    // Applications
    applications: [
      'Building automation & monitoring',
      'Lighting controls',
      'Inventory management',
      'Environmental monitoring',
      'Security systems',
      'Industrial monitoring',
      'Machinery condition and performance monitoring',
      'Plant system parameters monitoring (temperature, pressure, flow, tank level, humidity, vibration)',
      'Smart metering & lighting solutions',
      'Smart flood sensors',
      'Smart street lighting',
      'Smart city networks',
      'Smart waste management systems'
    ],

    // Documents (matching with DOCS array cat/subcat)
    documents: {
      cat: 'lora',
      subcat: 'module',
      datasheets: ['NLN500b LoRa Module Datasheet 2.0.pdf'],
      brochures: ['NLN500b Brochure.pdf']
    },

    // Product variants/ordering info
    variants: [
      {
        sku: 'PL1N500BUF100',
        name: 'u.FL Connector',
        description: 'NLN500b with u.FL connector for external antenna',
        antenna: 'u.FL'
      },
      {
        sku: 'PL1N500BFL100',
        name: 'Feedline',
        description: 'NLN500b with integrated feedline antenna',
        antenna: 'Feedline'
      },
      {
        sku: 'PL1N500SGL100',
        name: 'Spring Antenna',
        description: 'NLN500b with spring antenna',
        antenna: 'Spring'
      }
    ],

    // URLs & Meta
    slug: 'lora-module-nln500b',
    metaDescription: 'NLN500b LoRa module - dual-protocol LoRaWAN/Sigfox module with −123 dBm RX sensitivity, +21 dBm TX power, and multiple antenna options.',
    metaKeywords: 'LoRa module, Sigfox, STM32WL, IoT, LoRaWAN, low-power, Nebulae'
  }
];

// Export for Node.js environments
if (typeof module !== 'undefined' && module.exports) {
  module.exports = PRODUCTS;
}
