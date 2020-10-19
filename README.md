# django-meeting-planner

Project structure
* meeting_planner - django project directory 
    * meeting_planner - Core project folder containing settings and url mapping
    
    Two App folders
    
    * meetings - contains all code about meetings
        * models ( database models )
        * migrations - all migration database scripts
        * templates/meetings templates for detailed view
        * views
    * website - contains the views file (welcome, about, etc)
* db.sqlite3 - database
* manage.py - run all the amdin django scripts