# 📝 newBlog

newBlog — bu Django asosida yozilgan blog platformasi bo‘lib, foydalanuvchilar post yaratishi, izoh qoldirishi va ulardan foydalanishi mumkin.

---

## 🚀 Texnologiyalar

- **Backend**: Django 5+
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: PostgreSQL (Render uchun sozlangan)
- **Deployment**: Render
- **Storage**: Cloudinary (rasmlar va media fayllar uchun)

---

## ⚙️ O‘rnatish va ishga tushirish

### 1. Reponi klonlash
```bash
git clone https://github.com/<your-username>/newBlog.git
cd newBlog
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
DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
CLOUDINARY_URL=cloudinary://API_KEY:API_SECRET@CLOUD_NAME

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

## Fayl struktura
```bash

newBlog/
│── blog/             
│── users/          
│── static/       
│── media/          
│── templates/         
│── requirements.txt  
│── manage.py
│── README.md
│── LICENSE

```
## Xususiyatlar
- Post yaratish, tahrirlash va o‘chirish

- Postlarga izoh yozish

- Foydalanuvchi ro‘yxatdan o‘tishi va login qilish

- Admin panel orqali boshqaruv

- Cloudinary orqali rasm/media saqlash

- Render’da deploy qilish

## Litsenziya
Ushbu loyiha [MIT License](./LICENSE) asosida tarqatiladi.


