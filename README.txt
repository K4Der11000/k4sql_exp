# SQLi Scanner Web App by kader11000

واجهة ويب احترافية لفحص واستغلال ثغرات SQLi باستخدام sqlmap.

## المتطلبات

- Python 3.x
- Flask
- requests
- sqlmap (يجب أن يكون مثبتًا ومتاحًا في PATH)

## التثبيت والتشغيل

1. تثبيت الحزم:
```
pip install -r requirements.txt
```

2. تأكد أن أداة sqlmap تعمل:
```
sqlmap --version
```

3. تشغيل التطبيق:
```
python app.py
```

أو باستخدام السكربت:
```
chmod +x start.sh
./start.sh
```

4. افتح المتصفح على:
```
http://localhost:5000
```

## بيانات الدخول

- كلمة المرور: `kader11000`

## المميزات

- فحص متعدد الروابط
- خيارات sqlmap المتقدمة
- استخراج التقارير بصيغة HTML
- زر تشغيل/إيقاف
- واجهة ملونة ومجدولة
- زر تسجيل خروج
- حماية من التخمين