#!/usr/bin/env node

/**
 * Nebulae Products Build Script
 * Generates static HTML files from templates and product data
 */

const fs = require('fs');
const path = require('path');

// Load data
const PRODUCTS = require('./data/products.js');
const DOCS = require('./data/docs.js');

// Configuration
const OUTPUT_DIR = path.join(__dirname, 'dist');
const TEMPLATES_DIR = path.join(__dirname, 'templates');
const ASSETS_DIR = path.join(__dirname, 'assets');

// Ensure output directory exists
if (!fs.existsSync(OUTPUT_DIR)) {
  fs.mkdirSync(OUTPUT_DIR, { recursive: true });
}

/**
 * Copy assets to output directory
 */
function copyAssets() {
  console.log('📦 Copying assets...');
  
  function copyDir(src, dest) {
    if (!fs.existsSync(dest)) {
      fs.mkdirSync(dest, { recursive: true });
    }
    
    const files = fs.readdirSync(src);
    files.forEach(file => {
      const srcFile = path.join(src, file);
      const destFile = path.join(dest, file);
      
      if (fs.statSync(srcFile).isDirectory()) {
        copyDir(srcFile, destFile);
      } else {
        fs.copyFileSync(srcFile, destFile);
      }
    });
  }
  
  copyDir(ASSETS_DIR, path.join(OUTPUT_DIR, 'assets'));
  copyDir(path.join(__dirname, 'data'), path.join(OUTPUT_DIR, 'data'));
  console.log('✓ Assets copied');
}

/**
 * Generate all-products grid page
 */
function generateAllProductsPage() {
  console.log('📄 Generating all-products page...');
  
  let template = fs.readFileSync(path.join(TEMPLATES_DIR, 'products-all.html'), 'utf8');
  
  const output = path.join(OUTPUT_DIR, 'products.html');
  fs.writeFileSync(output, template);
  
  console.log(`✓ Generated: ${output}`);
}

/**
 * Generate category listing pages
 */
function generateCategoryPages() {
  console.log('📄 Generating category listing pages...');
  
  // Group products by category + protocol
  const categories = {};
  PRODUCTS.forEach(product => {
    const key = `${product.category}-${product.protocol}`;
    if (!categories[key]) {
      categories[key] = {
        category: product.category,
        protocol: product.protocol,
        products: []
      };
    }
    categories[key].products.push(product);
  });

  // Category descriptions and configs
  const categoryConfig = {
    'Module-LoRa': {
      title: 'LoRa Modules',
      breadcrumb: 'LoRa Modules',
      heroDesc: 'Compact, surface-mount LoRa modules with embedded STM32WL transceivers for rapid IoT development.',
      overview: 'Our LoRa module lineup features the latest STM32WL SoC technology, offering long-range communication, low power consumption, and industrial-grade reliability. Perfect for embedded systems, wearables, and IoT nodes.',
      selectionGuide: 'Choose NLN500a for minimal footprint and cost-effective deployments. Select NLN500b for dual-protocol support (LoRaWAN/Sigfox) and enhanced I/O capabilities.',
      commonFreq: 'EU 863-870, US 902-928, IN 865 MHz',
      commonProtocol: 'LoRaWAN®',
      commonRange: '~10 km (LoS)',
      commonVoltage: '1.8V - 3.6V DC',
      commonTemp: '−20°C to +75°C'
    }
    // Add more categories as needed
  };

  Object.entries(categories).forEach(([key, catData]) => {
    const config = categoryConfig[key] || {
      title: `${catData.protocol} ${catData.category}`,
      breadcrumb: `${catData.protocol} ${catData.category}`,
      heroDesc: `Explore our range of ${catData.protocol} ${catData.category} products.`,
      overview: `Our ${catData.protocol} ${catData.category} products are designed for IoT applications requiring long-range communication and low power consumption.`,
      selectionGuide: 'Contact our sales team for help choosing the right product for your application.',
      commonFreq: 'Multiple bands supported',
      commonProtocol: catData.protocol,
      commonRange: 'Up to 10+ km',
      commonVoltage: '1.8V - 3.6V DC',
      commonTemp: '−20°C to +75°C'
    };

    let template = fs.readFileSync(path.join(TEMPLATES_DIR, 'products-category.html'), 'utf8');

    // Replace placeholders
    const slug = `${key.toLowerCase().replace(/\s+/g, '-')}`;
    template = template.replace(/{{CATEGORY_TITLE}}/g, config.title);
    template = template.replace(/{{CATEGORY_BREADCRUMB}}/g, config.breadcrumb);
    template = template.replace(/{{CATEGORY_DESC}}/g, config.title);
    template = template.replace(/{{CATEGORY_HERO_DESC}}/g, config.heroDesc);
    template = template.replace(/{{CATEGORY_NAME}}/g, catData.category);
    template = template.replace(/{{CATEGORY_PROTOCOL}}/g, catData.protocol);
    template = template.replace(/{{CATEGORY_OVERVIEW}}/g, config.overview);
    template = template.replace(/{{CATEGORY_FILTER}}/g, catData.category);
    template = template.replace(/{{PROTOCOL_FILTER}}/g, catData.protocol);
    template = template.replace(/{{COMMON_FREQ}}/g, config.commonFreq);
    template = template.replace(/{{COMMON_PROTOCOL}}/g, config.commonProtocol);
    template = template.replace(/{{COMMON_RANGE}}/g, config.commonRange);
    template = template.replace(/{{COMMON_VOLTAGE}}/g, config.commonVoltage);
    template = template.replace(/{{COMMON_TEMP}}/g, config.commonTemp);
    template = template.replace(/{{SELECTION_GUIDE}}/g, config.selectionGuide);

    const dir = path.join(OUTPUT_DIR, 'products');
    if (!fs.existsSync(dir)) {
      fs.mkdirSync(dir, { recursive: true });
    }

    const output = path.join(dir, `${slug}.html`);
    fs.writeFileSync(output, template);

    console.log(`✓ Generated: ${output}`);
  });
}

/**
 * Generate individual product detail pages
 */
function generateDetailPages() {
  console.log('📄 Generating product detail pages...');

  PRODUCTS.forEach(product => {
    let template = fs.readFileSync(path.join(TEMPLATES_DIR, 'products-detail.html'), 'utf8');

    // Build features HTML
    const featuresHtml = product.features.map(feature => `
      <div class="feature-item">
        <span class="feature-icon">✓</span>
        <span class="feature-text">${feature}</span>
      </div>
    `).join('');

    // Build specifications HTML
    let specsHtml = '';
    Object.entries(product.specs).forEach(([groupName, specs]) => {
      const groupTitle = groupName.split(/(?=[A-Z])/).map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ');
      specsHtml += `
        <div class="spec-group">
          <div class="spec-group-title">${groupTitle}</div>
          ${Object.entries(specs).map(([label, value]) => `
            <div class="spec-item">
              <span class="spec-label">${label}</span>
              <span class="spec-value">${value}</span>
            </div>
          `).join('')}
        </div>
      `;
    });

    // Build applications HTML
    const applicationsHtml = product.applications.map(app => `
      <div>
        <h4 style="color: var(--primary-color); margin-bottom: var(--spacing-4); font-size: 1rem;">✓ ${app}</h4>
      </div>
    `).join('');

    // Build documents HTML
    const documentsHtml = product.documents.datasheets.concat(product.documents.brochures).map(filename => {
      const doc = DOCS.find(d => d.filename === filename);
      if (!doc) return '';

      return `
        <div class="download-item">
          <div class="download-type">${doc.type}</div>
          <div class="download-title">${doc.title}</div>
          <div class="download-meta">Version ${doc.version} • ${doc.date}</div>
          <p>${doc.description}</p>
          <a href="${doc.url}" class="download-link">Download PDF →</a>
        </div>
      `;
    }).join('');

    // Build variants section
    let variantsSection = '';
    if (product.variants && product.variants.length > 0) {
      variantsSection = `
        <div style="background: var(--gray-50); padding: var(--spacing-8); border-radius: var(--border-radius-lg); margin-bottom: var(--spacing-16);">
          <h3>Available Variants</h3>
          <div class="grid grid-2">
            ${product.variants.map(v => `
              <div class="product-card">
                <h4 style="margin-bottom: var(--spacing-4); color: var(--primary-color);">${v.name}</h4>
                <p style="margin-bottom: var(--spacing-4);">${v.description}</p>
                <div style="background: var(--white); padding: var(--spacing-4); border-radius: var(--border-radius-md); font-family: monospace; font-size: 0.85rem; color: var(--primary-color); font-weight: 600;">
                  SKU: ${v.sku}
                </div>
              </div>
            `).join('')}
          </div>
        </div>
      `;
    }

    // Replace all placeholders
    template = template.replace(/{{PRODUCT_NAME}}/g, product.name);
    template = template.replace(/{{PRODUCT_MODEL}}/g, product.model);
    template = template.replace(/{{PRODUCT_META_DESCRIPTION}}/g, product.metaDescription);
    template = template.replace(/{{PRODUCT_META_KEYWORDS}}/g, product.metaKeywords);
    template = template.replace(/{{PRODUCT_SHORT_DESC}}/g, product.shortDesc);
    template = template.replace(/{{PRODUCT_DESCRIPTION}}/g, product.description);
    template = template.replace(/{{PRODUCT_PROTOCOL}}/g, product.protocol);
    template = template.replace(/{{PRODUCT_HERO_IMAGE}}/g, product.heroImage);
    template = template.replace(/{{PRODUCT_TX_POWER}}/g, product.specs.wireless['TX Power']);
    template = template.replace(/{{PRODUCT_DIMENSIONS}}/g, product.specs.general['Dimensions (L×W×H)']);
    template = template.replace(/{{PRODUCT_RF_RANGE}}/g, product.specs.wireless['RF Range (LoS)']);
    template = template.replace(/{{PRODUCT_FEATURES_HTML}}/g, featuresHtml);
    template = template.replace(/{{PRODUCT_SPECS_HTML}}/g, specsHtml);
    template = template.replace(/{{PRODUCT_APPLICATIONS_HTML}}/g, applicationsHtml);
    template = template.replace(/{{PRODUCT_DOCUMENTS_HTML}}/g, documentsHtml);
    template = template.replace(/{{PRODUCT_VARIANTS_SECTION}}/g, variantsSection);
    template = template.replace(/{{PRODUCT_ID}}/g, product.id);
    template = template.replace(/{{PRODUCT_CATEGORY}}/g, product.category);
    template = template.replace(/{{PRODUCT_PROTOCOL}}/g, product.protocol);
    template = template.replace(/{{CATEGORY_SLUG}}/g, product.category.toLowerCase().replace(/\s+/g, '-'));
    template = template.replace(/{{PROTOCOL_SLUG}}/g, product.protocol.toLowerCase().replace(/\s+/g, '-'));

    const dir = path.join(OUTPUT_DIR, 'products');
    if (!fs.existsSync(dir)) {
      fs.mkdirSync(dir, { recursive: true });
    }

    const output = path.join(dir, `${product.slug}.html`);
    fs.writeFileSync(output, template);

    console.log(`✓ Generated: ${output}`);
  });
}

/**
 * Main build function
 */
function build() {
  console.log('\n🚀 Starting Nebulae Products Build...\n');

  try {
    copyAssets();
    generateAllProductsPage();
    generateCategoryPages();
    generateDetailPages();

    console.log('\n✅ Build completed successfully!\n');
    console.log(`Output directory: ${OUTPUT_DIR}`);
    console.log(`Total products: ${PRODUCTS.length}`);
    console.log(`Total pages generated: ${PRODUCTS.length + 2 + new Set(PRODUCTS.map(p => `${p.category}-${p.protocol}`)).size}\n`);
  } catch (error) {
    console.error('\n❌ Build failed:', error);
    process.exit(1);
  }
}

// Run build
build();
