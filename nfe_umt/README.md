# NFE UMT - نظام إدارة الجامعة الوطنية للتعليم

## Overview - نظرة عامة

NFE UMT is a comprehensive member management system built for the National Federation of Education. The system manages member information, organizational structures, membership cards, and financial transactions.

نظام إدارة شامل للأعضاء تم تطويره للجامعة الوطنية للتعليم. يقوم النظام بإدارة معلومات الأعضاء والهياكل التنظيمية وبطاقات العضوية والمعاملات المالية.

## Features - المميزات

- Member Management (إدارة الأعضاء)
- Membership Cards (بطاقات الإنخراط)
- Federation Structure (هيكلة الجامعة)
- Mutual Structure (هيكلة التعاضدية)
- Financial Management (الإدارة المالية)
- Reports and Analytics (التقارير والتحليلات)

## Installation - التثبيت

1. Install Frappe Bench:
```bash
pip install frappe-bench
```

2. Create a new site:
```bash
bench new-site nfe-site
```

3. Get the NFE UMT app:
```bash
bench get-app nfe_umt https://github.com/your-repository/nfe_umt
```

4. Install the app on your site:
```bash
bench --site nfe-site install-app nfe_umt
```

## Configuration - الإعداد

1. Create a new user with the "System Manager" role
2. Configure basic settings in NFE UMT Settings
3. Set up your organizational structure
4. Start adding members and issuing membership cards

## Usage - الاستخدام

1. Member Management:
   - Add new members
   - Issue membership cards
   - Track member status

2. Organizational Structure:
   - Define federation structure
   - Manage mutual structure
   - Assign roles and positions

3. Financial Management:
   - Record income and expenses
   - Track membership payments
   - Generate financial reports

## Support - الدعم

For support and questions, please contact:
- Email: support@nfe.ma
- Phone: +212-XXXXXXXXX

## License - الترخيص

This project is licensed under the MIT License - see the LICENSE file for details.
