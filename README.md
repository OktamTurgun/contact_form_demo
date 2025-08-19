#  Contact Form Demo

Contact Form Demo — bu **Django** asosida yozilgan oddiy kontakt forma loyihasi.  
Foydalanuvchilar ism, familiya, telefon raqam, email va xabarni yuborishlari mumkin. Yuborilgan xabarlar ma’lumotlar bazasiga saqlanadi va `/xabarlar/` sahifasida ko‘rinadi.

---

##  Texnologiyalar

- **Backend**: Django 5.x  
- **Frontend**: HTML, CSS, Bootstrap  
- **Database**: SQLite (odatdagi konfiguratsiya)  
- (Agar PostgreSQL/Render ishlatilsa, bu qismni kengaytiring)

---

##  O‘rnatish va ishga tushirish

### 1. Reponi klonlash
```bash
git clone https://github.com/OktamTurgun/contact_form_demo.git
cd contact_form_demo

```

### 2. Virtual environment yaratish
```bash

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```
### 3. Kerakli kutubxonalarni o‘rnatish
```bash

pip install -r requirements.txt
```
### 4. .env faylini yaratish

DEBUG=True
SECRET_KEY=your-secret-key

### 5. Migratsiyalarni qo‘llash
```bash

python manage.py migrate
```
### 6. Superuser yaratish
```bash

python manage.py createsuperuser
```
### 7. Serverni ishga tushirish
```bash

python manage.py runserver
```
## Deploy (Render)

1. Kodni GitHub’ga push qiling

2. Render’da New Web Service yarating

3. Environment Variables bo‘limiga .env dagi sozlamalarni qo‘shing

4. Deploy qiling 🎉

## URL’lar

- / → Kontakt forma (xabar yuborish)

- /xabarlar/ → Yuborilgan xabarlar ro‘yxati

## Fayl struktura
```bash

contact_form_demo/
│── contacts/
│── config/
│── templates/
│── .gitignore
│── LICENSE
│── README.md
│── requirements.txt
│── db.sqlite3
│── manage.py

```
## Xususiyatlar

- Kontakt forma orqali xabar yuborish

- Xabarlarni ma’lumotlar bazasida saqlash

- Yuborilgan xabarlarni jadval ko‘rinishida ko‘rsatish (Bootstrap bilan)

## Litsenziya
Ushbu loyiha [MIT License](./LICENSE) asosida tarqatiladi.


