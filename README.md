
# Auslanderina

Auslanderina is a personal blog that shows the gallery of the artworks. There is a possibility for the users to add their own artwork’s names into the list of works in the about page. However, in order to do that, the user needs to be registered. After adding the work, there is a possibility to update or delete it. 

## The project

 The project includes 7 HTML pages, variety of CSS styles and responsiveness (very well observed in the gallery of the artworks). There is a client-side JavaScript on the registration page that guides the user through the process of entering the right information to be able to register.

  The backend is done using Flask, having 6 different routes, with an attempt to have a dynamic render. The content is rendered using a jinja2. 

The database includes 2 working models and is rendered dynamically from the database. 

 There is CRUD, the users can create, update and delete the records. It is done on the about page, where there are forms to create a new work, that is added into the list, and later, there is a possibility to change or delete that work. 

  The website is deployed and can be viewed here: https://auslanderina.onrender.com/  

 To set up the code on your local machine, download the project and run the app write python app.py in the terminal.   
