/**
 * DOCS Data Array
 * Documents (datasheets, brochures, technical guides) for Nebulae products
 * Matches with PRODUCTS array via cat/subcat
 */

const DOCS = [
  // LoRa Module Documents
  {
    title: 'NLN500a Module Datasheet',
    filename: 'NLN500a_Module_Datasheet_V2.2.pdf',
    cat: 'lora',
    subcat: 'module',
    type: 'datasheet',
    version: '2.2',
    date: 'March 2022',
    description: 'Technical specifications for NLN500a LoRa module including RF characteristics, electrical specifications, pinout details, and regulatory approvals.',
    url: '/docs/datasheets/lora/NLN500a_Module_Datasheet_V2.2.pdf',
    size: 'TBD KB'
  },
  {
    title: 'NLN500a LoRa Module Brochure',
    filename: 'NLN500a LoRa Module Brochure.pdf',
    cat: 'lora',
    subcat: 'module',
    type: 'brochure',
    version: '1.0',
    date: 'TBD',
    description: 'Product overview and features brochure for NLN500a LoRa module.',
    url: '/docs/brochures/lora/NLN500a_LoRa_Module_Brochure.pdf',
    size: 'TBD KB'
  },
  {
    title: 'NLN500b LoRa Module Datasheet',
    filename: 'NLN500b LoRa Module Datasheet 2.0.pdf',
    cat: 'lora',
    subcat: 'module',
    type: 'datasheet',
    version: '2.0',
    date: 'November 2023',
    description: 'Technical specifications for NLN500b dual-protocol (LoRaWAN/Sigfox) module including pin details, operating characteristics, RF specifications, and regulatory approvals.',
    url: '/docs/datasheets/lora/NLN500b_LoRa_Module_Datasheet_2.0.pdf',
    size: 'TBD KB'
  },
  {
    title: 'NLN500b LoRa Module Brochure',
    filename: 'NLN500b Brochure.pdf',
    cat: 'lora',
    subcat: 'module',
    type: 'brochure',
    version: '1.0',
    date: 'TBD',
    description: 'Product overview, features, and specifications brochure for NLN500b LoRa module.',
    url: '/docs/brochures/lora/NLN500b_LoRa_Module_Brochure.pdf',
    size: 'TBD KB'
  }
];

// Export for Node.js environments
if (typeof module !== 'undefined' && module.exports) {
  module.exports = DOCS;
}
