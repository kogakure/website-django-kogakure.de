Licence
-------

(ɔ) Copyleft 2007-2008 Stefan Imhoff
Licensed under the GNU General Public License, version 3.
[http://www.gnu.org/copyleft/gpl.txt](http://www.gnu.org/copyleft/gpl.txt)

This is the source code of [http://kogakure.de/](http://kogakure.de/ "kogakure.de – Ninja, Ninjutsu und Kampfkunst"). 
Created by [Stefan Imhoff](http://stefanimhoff.de/).

About
-----

kogakure.de is a german martial arts magazine founded in 1999. The topic of
this website are the Ninja and their martial art Ninjutsu.

Find out more about Ninjutsu today on [http://bujinkan.com/](http://bujinkan.com/ "Bujinkan Dojo - Soke Masaaki Hatsumi").
Visit your local dôjô. You won’t regret.

Information & Requirements
--------------------------

It’s my first Django-Projekt. You may use the code and templates for 
educational purposes or your own projects.

This site uses the Subversion-Trunk at *Django 1.0 Alpha*.

Installation
------------

This project has sample data. To install do:

    python manage.py syncdb

This creates all database tables in an SQLite database and dumps some data in
the tables. It also creates a superuser:

* **User**: test
* **Password**: test

Syncdb will ask if you would like to create a superuser, choose (no) as the
fixture will create a superuser.

Language for the site is german, if you would like to have an english
interface change `LANGUAGE_CODE = 'de-de'` to `LANGUAGE_CODE = 'en'`
in settings.py. To start the server do:

    python manage.py runserver

This starts the development server on [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

You can visit the website in your browser. To log into the admin interface
point your browser to [http://127.0.0.1/admin/](http://127.0.0.1/admin/) and log in with the test user.

* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 

> „Understand? Good. Play!“

– *Masaaki Hatsumi*, Grandmaster of 9 Ryûha (schools) and Soke (head) 
of the Bujinkan Budô Dôjô.