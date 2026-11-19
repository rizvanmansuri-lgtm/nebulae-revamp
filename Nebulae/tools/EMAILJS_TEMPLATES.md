# EmailJS templates (contact form) — paste into EmailJS → Email Templates

Variables sent by the site: {{form_type}} {{subject}} {{from_name}} {{from_email}} {{phone}} {{company}} {{product}} {{quantity}} {{timeline}} {{solution}} {{protocols}} {{details}} {{message}} {{page_url}} {{submitted_at}} {{to_email}}
({{details}} is a ready-made multi-line summary of the subject-specific fields, so one template works for every subject.)

## 1. ADMIN template (already used: template_tdcdtb8)
Settings: To = `{{to_email}}` · Reply-To = `{{from_email}}` · From name = `Nebulae Website` · Subject = `[Website] {{subject}}`

HTML body:
```html
<div style="font-family:Arial,Helvetica,sans-serif;max-width:620px;margin:auto;border:1px solid #e5e7eb;border-radius:10px;overflow:hidden">
  <div style="background:#25238a;color:#fff;padding:16px 22px"><b style="font-size:16px">New website inquiry</b><br><span style="font-size:13px;opacity:.85">{{form_type}}</span></div>
  <div style="padding:22px;color:#111827;font-size:14px;line-height:1.6">
    <p style="margin:0 0 4px"><b>Subject:</b> {{subject}}</p>
    <table style="width:100%;border-collapse:collapse;margin:12px 0;font-size:14px">
      <tr><td style="padding:6px 0;color:#6b7280;width:120px">Name</td><td>{{from_name}}</td></tr>
      <tr><td style="padding:6px 0;color:#6b7280">Email</td><td><a href="mailto:{{from_email}}">{{from_email}}</a></td></tr>
      <tr><td style="padding:6px 0;color:#6b7280">Phone</td><td>{{phone}}</td></tr>
      <tr><td style="padding:6px 0;color:#6b7280">Company</td><td>{{company}}</td></tr>
    </table>
    <p style="margin:14px 0 4px"><b>Request details</b></p>
    <div style="white-space:pre-line;background:#f4f6fb;border-radius:8px;padding:12px 14px">{{details}}</div>
    <p style="margin:14px 0 4px"><b>Message</b></p>
    <div style="white-space:pre-line;background:#f4f6fb;border-radius:8px;padding:12px 14px">{{message}}</div>
    <p style="margin:16px 0 0;font-size:12px;color:#6b7280">Received {{submitted_at}} · from {{page_url}}<br>Reply directly to this email to answer the customer.</p>
  </div>
</div>
```

## 2. CUSTOMER auto-reply template (create new, then paste its ID in nebulae-forms.js → TEMPLATES.autoreply)
Settings: To = `{{from_email}}` · Reply-To = `sales@nebulae.io` · From name = `Nebulae` · Subject = `We received your request — Nebulae`

HTML body:
```html
<div style="font-family:Arial,Helvetica,sans-serif;max-width:620px;margin:auto;border:1px solid #e5e7eb;border-radius:10px;overflow:hidden">
  <div style="background:#25238a;color:#fff;padding:18px 22px"><b style="font-size:18px">NEBULAE</b><br><span style="font-size:12px;opacity:.85">Design to Connect</span></div>
  <div style="padding:24px 22px;color:#111827;font-size:14px;line-height:1.65">
    <p>Dear {{from_name}},</p>
    <p>Thank you for contacting Nebulae. We have received your request and our team will get back to you within one working day.</p>
    <p style="margin:18px 0 4px"><b>Your request</b></p>
    <div style="white-space:pre-line;background:#f4f6fb;border-radius:8px;padding:12px 14px"><b>{{subject}}</b>
{{details}}</div>
    <p style="margin:14px 0 4px"><b>Your message</b></p>
    <div style="white-space:pre-line;background:#f4f6fb;border-radius:8px;padding:12px 14px">{{message}}</div>
    <p style="margin-top:18px">If anything is urgent, reach us at <a href="tel:+919898042339">+91 9898042339</a> or reply to this email.</p>
    <p>Regards,<br><b>Team Nebulae</b><br>System Level Solutions (India) Pvt. Ltd.<br>Plot#32, Zone-D/4, Phase-1, GIDC Estate, V.U.Nagar - 388121, Gujarat, India<br><a href="https://www.nebulae.io">www.nebulae.io</a> · sales@nebulae.io</p>
  </div>
</div>
```
