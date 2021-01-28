# source ~/.virtualenvs/djangodev/Scripts/activate
----------------------------------------------------------------

#start app
py manage.py startapp polls
-------------------------------------------

# py manage.py runserver
# Cross Site Request Forgeries {% csrf_token %} 

--------------------------------------------------


# py manage.py shell

b = Urlshort.objects.create(url='http://jawad.com', shortcode='shorti')

c = Urlshort.objects.get_or_create(url='http://farhad.com', shortcode='farhadi')


-------------------------------------------------------------------------------------------
# py manage.py test polls
---------------------------------------------------

# http://localhost:8000/polls/

-------------------------------------------------------------

# this was when makemigrations is not working after deleting the database and migrations folder. 
py manage.py migrate --run-syncdb
-----------------------------------------------------------------------------------


