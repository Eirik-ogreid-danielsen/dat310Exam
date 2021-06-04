How to run:
    First setup the database:
        -navigate to  the application folder VueBrew and run the setup_DB.py file. this will create the database and create all the tables.
        -then run the init_data.py file. This wil create some ingredients and populate the database with them.
    Then start the backend server
        - from the application folder VueBrew run the app.py file
    Finally start the frontend client
        -from the application folder VueBrew navigate to the frontend server.
        -then enter the command npm run serve to start the vue application
        -you can now enter the application by connecting to http://localhost:8080/

Features:
    -register user
    -log in user
    -add all the nessescary ingredients to brew beer to a recipe
    -save the recipe
    -watch saved recipes

Comments:
    I think i bit over a bit more than i could chew with the original plan. 
    The plan was to create a homebrewing calculator which would calculate important information about the recipe,
    like Gravity points, ABV and IBU. all vital information while designing a recipe. To do this quite a few attributes were required for each ingredient.
    This made the backend quite complicated with many different tables being required. And a similar amount of States in the vuex store, for the information displayed right now both the database backend and vuex store is quite overkill.
    Both the store and the database store many atributes that are never used in the current application.  But with some more methods could be accessed and used to display the desired calculations. 
    In the brewformulas.js there is a mockuo off all the nessescary functions that would be required. they would have to be modified quite  abit to be uses with vue and vuex, but they make a decent framework to start with. Currently nothing from brewFormulas.js is used.

    The vuex store is also a bit overill for the application in its current form, as plenty of attributes are stored and are reachable troughout the app that are never used. On the positive side this means that the app is very reactive, with inputs being updated quickly and staying persistent trough the app.  Allowing the app to be easily be separated into components with all the core data being fetched from the store. and changes being stored in the store.

    There is also a problem with Sessions, i got stuck with implementing sessions with flask and the vue application being run separately. So right now the vue application simply sends the username and password in plaintext to the server, the server then validates the username and password and returns the username to the vue client. The username is then  stored as the currentuser in the vue app. it is this currentUser state that functions as a sort of "session" for the client. This is not at all secure and if i had the time i would implement a session state on the server aswell and send the username and password as encryopted cookies. Since there is no serverside session, my logout function simply sets the current user back to the default "Not logged in" state.

    Due to the complexity of the database with recipes being stored in 3 different tables i did not have time to implement a remove function in the api. this complexity is  to allow for differing amounts of fermentables and hops being used in each recipe. each recipe gets an id and hops and fermentables gets are stored in their own tables with a foreignkey referencing the recipe id. 
    my plan was to display a remove button in the recipe route if the recipe author parameter matches the currentUser state. This button would on click send the currentUser and the recipe id to the api, and if the recipe id and user id was correct for the recipe remove it from the database.

    I also never got around to implementing client side validation, such that all validation of forms happen on the server, it does therfore hinder the user experience quite  a bit, and it allows the user to make some silly mistakes like entering amounts and time as strings, this would not be allowed by the database and the recipe would not be stored, but no error message would reach the user. ideally this would have been sorted by client side validation, and any errors that made it trough should also be sent back to the user from the database.

    I oviously also had little time for the css, and implemented a few borders and some styling on the list otherwise the css is the default from the vue cli.