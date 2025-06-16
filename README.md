<!-- install virtual environment -->
pip install virtualenv

<!-- create virtual environment -->
virtualenv env_name(env or venv)
(or)
python -m venv env_name

<!-- activate virtual environment -->
env\Scripts\activate(windows)
source env/Scripts/activate(linux)
source my_env/bin/activate(mac)

<!-- install django -->
pip install django

<!-- start project -->
django-admin startproject project_name . ('.' is optional)

<!-- start server -->
python manage.py runserver

<!-- create app  -->
python manage.py startapp app_name

<!-- create migratioin file -->
python manage.py makemigrations

<!-- changes in database using makemigration file -->
python manage.py migrate

<!-- open shell -->
python manage.py shell

<!-- list of objects of class/models -->
Class_model_name.objects.all()

<!-- create object/data -->
model_name.objects.create
(title="dndnn"descriptioin="....",...)

<!--to show values  -->
Class_model_name.objects.all().values()

<!-- represrnt obj into string -->
defining function return self.title

<!-- single data fetch -->
a= model_name.objects.get(id=1..)

<!-- update -->
a.title = "new data"
a.save()

<!-- delete -->
a.delete()

<!-- to filter the objects -->
class_model_name.objects.filter(field="data",field="data",title="second")