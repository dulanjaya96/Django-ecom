A Django 4.2 e-commerce app with product browsing, cart, checkout, order management, coupons, refunds, and user profiles. Uses SQLite for development and Bootstrap 4 (via crispy-forms) for the UI.

Main Features

Products & Orders: Models for items, orders, billing addresses, payments, coupons, refunds, and profiles. Includes checkout, coupon use, and refund requests.

Admin Tools: Date range filtering, export orders to CSV, and mark refunds as granted.

User Accounts: Standard Django auth + django-allauth for account & social login.

Forms/UI: django-crispy-forms with crispy-bootstrap4 for consistent styling.

Addresses: Country fields with django-countries.

Debugging: django-debug-toolbar in development.

Implemented with django-two-factor-auth & django-otp.

Stripe Payments

Integrated via Stripe Python SDK.

