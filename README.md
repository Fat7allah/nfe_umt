# نظام إدارة الجامعة الوطنية للتعليم

## نظرة عامة
نظام إدارة متكامل للجامعة الوطنية للتعليم يتيح:
- تسيير الأعضاء وبطاقات انخراطهم
- إدارة الهيكل التنظيمي للجامعة
- إدارة هيكل التعاضدية
- تتبع المداخيل والمصاريف
- إدارة المعلومات حسب السنة الدراسية

## المتطلبات التقنية
- Python 3.10+
- Node.js 16+
- Redis
- MariaDB/MySQL
- Frappe Framework v14

## التثبيت

1. تثبيت Frappe Bench:
```bash
pip install frappe-bench
```

2. إنشاء موقع جديد:
```bash
bench init nfe-bench
cd nfe-bench
bench new-site nfe.local
```

3. الحصول على التطبيق:
```bash
bench get-app nfe_umt
bench --site nfe.local install-app nfe_umt
```

4. تشغيل التطبيق:
```bash
bench start
```

## الوصول
- افتح المتصفح على العنوان: http://nfe.local:8000
- سجل الدخول باستخدام حساب المشرف

## الميزات الرئيسية
1. إدارة الأعضاء
   - تسجيل وتحديث بيانات الأعضاء
   - إدارة بطاقات العضوية
   - تصنيف الأعضاء حسب المهنة والمؤسسة

2. الهيكل التنظيمي
   - إدارة المكتب التنفيذي
   - إدارة المكاتب الجهوية
   - إدارة المكاتب الإقليمية
   - إدارة المكاتب المحلية

3. هيكل التعاضدية
   - إدارة المكتب التنفيذي
   - إدارة المجلس الإداري
   - إدارة الجمع العام
   - إدارة لجنة المراقبة

4. الإدارة المالية
   - تتبع المداخيل
   - تتبع المصاريف
   - تقارير مالية

## الدعم
للمساعدة والدعم الفني، يرجى التواصل مع فريق الدعم على البريد الإلكتروني: support@nfe.ma

## الترخيص
هذا المشروع مرخص تحت رخصة MIT
