rm db.sqlite3 
rm -rf api/migrations/ 
python manage.py makemigrations 
python manage.py migrate 
python manage.py makemigrations api 
python manage.py migrate api 
python manage.py createsuperuser &&
http --json POST http://127.0.0.1:8000/api-token-auth/ username="admin" password="password123"
