# Nebulae Product Pages System

A static site generator for Nebulae IoT product documentation and specifications. Generates SEO-friendly HTML pages from structured product data.

## 📋 Overview

This system creates a complete product catalog website with three tiers of pages:

1. **All Products Grid** (`products.html`) - Browse all products across all categories
2. **Category Listings** (`products/lora-module.html`) - List products by category + protocol combination with comparison tables
3. **Product Details** (`products/lora-module-nln500a.html`) - Individual product pages with full specs, features, applications, and downloads

### Generated Structure

```
dist/
├── products.html                    # All products grid
├── products/
│   ├── module-lora.html            # LoRa Module listing (NLN500a, NLN500b)
│   ├── lora-module-nln500a.html    # NLN500a detail page
│   ├── lora-module-nln500b.html    # NLN500b detail page
│   └── [other category pages...]
├── assets/
│   ├── css/
│   │   └── products.css            # Global stylesheet (Poppins, light theme)
│   └── images/
│       └── products/               # Product images extracted from PDFs
├── data/
│   ├── products.js                 # Product data array
│   └── docs.js                     # Documents/datasheets array
└── [other pages...]
```

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd product-pages
npm install  # (currently no external npm deps required - vanilla JS + Node.js)
```

### 2. Prepare Product Data

Edit `data/products.js` to add/update products:

```javascript
const PRODUCTS = [
  {
    id: 'nln500a',                    // Unique ID
    model: 'NLN500a',                 // Model number
    name: 'NebuLink Module NLN500a',   // Display name
    category: 'Module',               // Category (Module, Gateway, etc.)
    protocol: 'LoRa',                 // Protocol (LoRa, Wi-SUN, etc.)
    description: '...',               // Full description
    shortDesc: '...',                 // One-line summary
    image: '/assets/images/products/nln500a-002.png',  // Product image
    heroImage: '/assets/images/products/nln500a-002.png', // Hero section image
    
    // Structured specifications
    specs: {
      general: {
        'Dimensions': '16.0 × 32.6 × 3.5 mm',
        // ...
      },
      wireless: {
        'TX Power': '+21 dBm',
        'RX Sensitivity (SF7)': '−122 dBm',
        // ...
      },
      // ... more spec groups
    },
    
    // Key features as bullet list
    features: [
      'Frequency Band: Supports EU 863-870...',
      // ...
    ],
    
    // Applications
    applications: [
      'Building automation & monitoring',
      // ...
    ],
    
    // Document references (matched with DOCS array)
    documents: {
      cat: 'lora',
      subcat: 'module',
      datasheets: ['NLN500a_Module_Datasheet_V2.2.pdf'],
      brochures: ['NLN500a LoRa Module Brochure.pdf']
    },
    
    // SKU variants
    variants: [
      {
        sku: 'NLN500a-STD',
        name: 'Standard',
        description: 'Standard NLN500a module'
      }
    ],
    
    // SEO
    slug: 'lora-module-nln500a',
    metaDescription: '...',
    metaKeywords: '...'
  }
];
```

### 3. Update Documents Array

Edit `data/docs.js` to add datasheets and brochures referenced in PRODUCTS:

```javascript
const DOCS = [
  {
    title: 'NLN500a Module Datasheet',
    filename: 'NLN500a_Module_Datasheet_V2.2.pdf',
    cat: 'lora',           // Matches products' document.cat
    subcat: 'module',      // Matches products' document.subcat
    type: 'datasheet',     // Or 'brochure'
    version: '2.2',
    date: 'March 2022',
    description: '...',
    url: '/docs/datasheets/lora/NLN500a_Module_Datasheet_V2.2.pdf',
    size: '500 KB'
  }
];
```

### 4. Add Product Images

Place product images in `assets/images/products/`:

```bash
assets/images/products/
├── nln500a-002.png      # Product images
├── nln500b-000.png
└── [other images...]
```

### 5. Build Static HTML

```bash
node build.js
```

The script will:
- Copy all assets to `dist/`
- Generate the all-products grid page
- Create category listing pages (one per category+protocol combination)
- Create individual product detail pages for each product
- Output structured, SEO-friendly HTML

### 6. Deploy

Copy the entire `dist/` directory to your web server:

```bash
cp -r dist/* /var/www/nebulae.io/products/
```

Or upload via FTP/git:

```bash
git add dist/
git commit -m "Update product pages"
git push
```

## 🎨 Design System

- **Font**: Poppins (Google Fonts)
- **Color Palette**: Light, professional theme with no dark sections
- **Primary Color**: `#1e40af` (Nebulae blue)
- **Responsive**: Mobile-first, works on all screen sizes
- **CSS**: Custom, no framework dependencies (no Bootstrap/Tailwind)

### CSS Variables

All colors and spacing use CSS custom properties defined in `assets/css/products.css`:

```css
:root {
  --primary-color: #1e40af;      /* Brand blue */
  --primary-light: #3b82f6;
  --success-color: #10b981;      /* Green for specs */
  --gray-50 through --gray-900;  /* Neutral palette */
  --spacing-2 through --spacing-16; /* Spacing scale */
}
```

Modify these to customize the entire site's appearance.

## 📝 Adding More Products

### 1. Add to data/products.js

Add a new entry to the `PRODUCTS` array following the structure above.

### 2. Add to data/docs.js

Add associated datasheets/brochures to the `DOCS` array, ensuring `cat` and `subcat` match the product's `documents.cat` and `documents.subcat`.

### 3. Add Category Configuration (if new category+protocol)

In `build.js`, add category-specific config to `categoryConfig`:

```javascript
const categoryConfig = {
  'Module-LoRa': { ... },  // Existing
  'Gateway-LoRa': {        // New
    title: 'LoRa Gateways',
    breadcrumb: 'LoRa Gateways',
    heroDesc: '...',
    overview: '...',
    selectionGuide: '...',
    commonFreq: '...',
    // ...
  }
};
```

### 4. Add Product Images

Place images in `assets/images/products/` and reference in the product's `image` and `heroImage` fields.

### 5. Rebuild

```bash
node build.js
```

## 🔄 Updating Products

### Change Specs

Edit the product entry in `data/products.js` and rebuild:

```bash
node build.js
```

New pages will overwrite the old ones.

### Update Product Images

Replace images in `assets/images/products/` and rebuild (images are copied during build).

### Update Documents

Add/remove entries in `data/docs.js` and rebuild. The listing and detail pages will automatically update.

## 🌐 Integration with Nebulae.io

### File Paths

If hosted at `nebulae.io/products/`:
- All products grid: `/products/products.html` → `/products.html`
- Category listing: `/products/products/module-lora.html` → `/products/lora-module.html`
- Product detail: `/products/products/lora-module-nln500a.html` → `/products/lora-module-nln500a.html`

**In build.js or manually adjust post-build paths as needed.**

### Asset Paths

- CSS: `/assets/css/products.css`
- Images: `/assets/images/products/[name].png`
- Data: `/data/products.js`, `/data/docs.js`

Update these in templates if your file structure differs.

### Linking from Other Pages

- All products: `<a href="/products.html">`
- Category: `<a href="/products/lora-module.html">`
- Product: `<a href="/products/lora-module-nln500a.html">`

## 📦 Contents

### Files Included

- `data/products.js` - Product specifications (NLN500a, NLN500b pilot)
- `data/docs.js` - Document references (datasheets, brochures)
- `templates/products-all.html` - All products grid template
- `templates/products-category.html` - Category listing template
- `templates/products-detail.html` - Product detail template
- `assets/css/products.css` - Global stylesheet (Poppins, light theme, ~600 lines)
- `assets/images/products/` - Product images (extracted from PDFs)
- `build.js` - Build script (generates static HTML)
- `README.md` - This file

### Generated Files (in dist/)

- `products.html` - All products grid (dynamically rendered with JS)
- `products/module-lora.html` - LoRa Module category listing
- `products/lora-module-nln500a.html` - NLN500a detail page
- `products/lora-module-nln500b.html` - NLN500b detail page
- `assets/` - Copied from source
- `data/` - Copied from source

## 🛠️ Extending the System

### Add New Product Line

**Pilot (LoRa Module) includes:**
- 2 products (NLN500a, NLN500b) ✓
- 1 category listing ✓
- 2 detail pages ✓
- 4 PDFs (2 datasheets, 2 brochures) ✓
- 8+ extracted images ✓

**To expand to all ~20 product lines:**

1. Extract specs from all remaining PDFs using the same process:
   ```bash
   pdftotext -layout "PDF_FILE.pdf" - | grep -A20 "Specification"
   ```

2. Add entries to `data/products.js` following the LoRa Module pattern

3. Extract images from brochures:
   ```bash
   pdfimages -png "BROCHURE.pdf" assets/images/products/[product-name]
   ```

4. Add document entries to `data/docs.js`

5. Add category config to `build.js` (if new category+protocol combo)

6. Rebuild: `node build.js`

### Customize Styling

All styling uses CSS variables in `assets/css/products.css`. Modify:

```css
:root {
  --primary-color: #YOUR_BLUE;
  --gray-50: #YOUR_LIGHT_GRAY;
  /* ... etc ... */
}
```

### Change Product Template Structure

Edit `templates/products-detail.html` to modify the product detail page layout. The build script injects data using `{{PLACEHOLDER}}` syntax.

## 🔍 SEO & Meta Tags

Each page includes:
- Unique `<title>` tags
- `<meta name="description">`
- `<meta name="keywords">`
- Structured breadcrumbs (for schema.org)
- Semantic HTML5 (`<article>`, `<section>`, `<header>`, `<footer>`)

All derived from product data in `data/products.js`.

## 📱 Responsive Design

All pages are mobile-first responsive:

- **Desktop**: 1200px max container, multi-column layouts
- **Tablet**: 768px breakpoint, 2-column grids
- **Mobile**: 480px breakpoint, single-column layouts
- **Touch-friendly**: Large tap targets, readable font sizes

Tested on Chrome, Safari, Firefox, and mobile browsers.

## ⚙️ Requirements

- Node.js 12+ (for build script)
- No external dependencies required
- Client-side: Modern browser (ES6 JavaScript)

## 📄 License

Copyright © 2024 Nebulae (System Level Solutions). All rights reserved.

---

## 🚀 Next Steps

1. ✅ Pilot complete with LoRa Module (NLN500a, NLN500b)
2. **Add remaining product lines** using the same process
3. **Deploy to nebulae.io/products/**
4. **Update navigation** on main site to link to product pages
5. **Monitor analytics** for engagement by product category
6. **Iterate** on design/copy based on user feedback

## 📞 Support

For questions or issues:
- Email: `sales@nebulae.io`
- Check `build.js` comments for build process details
- Ensure product data structure matches `data/products.js` format
