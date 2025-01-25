# HashFlix

### Objective:

Recreate the old Netflix website with python.

### Method:

- Django library -> Python.
- Tailwind CSS -> Design Changes.
- HTML -> Websites Basics.

### Features:

User system, films recently watched by each user, featured films by view count and recently added films overall.

### Files Explanation:

- manage.py -> Main file, used to run the app/site.
- ./templates folder -> Basics for the frontend, navbar file for the navigation bar in all pages, and base.html for the basic html settings for head and body in all pages.
- static folder -> Static images along all website pages.
- media folder -> Folder for saving all movie/series thumbs and main images.
- hashflix folder -> Folder with the site's name for saving django settings and connections with it's extensions (filme folder).
- filme folder -> Folder utilized for creating the actual website with it's features.
    - migrations folder -> Django user authentication files.
    - ./filme/templates folder -> Folder with each HTML page in the website (frontend).
    - admin.py -> File created to add and edit, on django administrator page, the items (films, series and episodes) that will be available on the website and also to create the list of films seen by each user.
    - apps.py -> File created to make a superuser ready when deploying the site (backend).
    - forms.py -> File to create the login and account creation forms that must exist within the website for user control (backend). 
    - models.py -> File for creating models present on the website, products that will be consumed by users (films and episodes) and how they will be saved in the database (backend).
    - novos_context.py -> File to create lists of recent films, list of featured films and list of films with the most views present on each user's home page.
    - urls.py -> File to create the URL pages that will be used by the website, connecting with the HTML files present in the templates folder (frontend connection).
    - views.py -> File to create the necessary functions on each page and connect the urls.py file with their respective HTML pages, in addition to prohibiting access to non-logged in users (backend).