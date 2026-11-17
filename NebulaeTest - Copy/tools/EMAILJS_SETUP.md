# EmailJS setup — Nebulae website forms

All forms use ONE file: `assets/js/nebulae-forms.js` (REST API, no SDK). Loaded on: index, contact, blog, events.

## 1. Edit CONFIG (top of assets/js/nebulae-forms.js)
| Key | Where to find it | Current value |
|---|---|---|
| `PUBLIC_KEY` | EmailJS → Account → General | `KMz0CeGkUnJobJMhK` ← **replace** |
| `SERVICE_ID` | EmailJS → Email Services | `service_5evtjim` (from earlier build — verify) |
| `TEMPLATES.contact` | EmailJS → Email Templates | `template_tdcdtb8` (from earlier build — verify) |
| `TEMPLATES.quote` | optional separate template for floating quote + Sample/EVK | `''` → reuses contact template |
| `TEMPLATES.newsletter` | optional separate template for newsletter | `''` → reuses contact template |
| `TO_EMAIL` | shown as `{{to_email}}` | `sales@nebulae.io` |

Until PUBLIC_KEY is replaced the forms show "This form is not connected yet — please email sales@nebulae.io" and send nothing.

## 2. Template variables (use in your EmailJS template, Subject and Body)
`{{form_type}}` `{{subject}}` `{{from_name}}` `{{from_email}}` `{{reply_to}}` `{{phone}}` `{{company}}` `{{quantity}}` `{{protocols}}` `{{product}}` `{{message}}` `{{page_url}}` `{{page_title}}` `{{submitted_at}}` `{{to_email}}`
Suggested Subject: `[Nebulae website] {{subject}}` · Reply-To: `{{reply_to}}` · To: `{{to_email}}`

## 3. Which form sends what
| Form | Page | template | form_type |
|---|---|---|---|
| Contact / quote form (+ pre-fill from `contact.html?product=..&qty=..&type=sample`) | contact.html | contact | "Contact form — <inquiry type>" |
| Floating "Get Quote" | index.html | quote | "Quick quote request (floating form)" |
| Request a Sample / EVK modal | index.html | quote | "Sample / EVK request" |
| Newsletter (3 boxes) | index.html, blog.html, events.html | newsletter | "Newsletter subscription" |

## 4. Built-in protection
Hidden honeypot field, 20 s cool-down per form+email (CONFIG.COOLDOWN_SEC), 15 s timeout, validation (name, email, phone 8–15 digits, company, subject, message ≥ 20 chars, consent tick on contact). In EmailJS also enable *Allowed domains* (Account → Security) for your live domain.

## 5. Adding a form later
Add `<script src="./assets/js/nebulae-forms.js"></script>` as the last script and either reuse an existing id pattern or call `NebulaeForms.send('contact', {form_type, from_name, from_email, message, ...})`.
