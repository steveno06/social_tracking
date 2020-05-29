# social_tracking
Instructions on how to run the application:
 
Once the project is downloaded using the requirements.txt file make sure that all of the libraries are installed.
 
Using the terminal cd into the directory of the project and simply run the application using the command 'python run.py'
Once that is done the terminal should show lines simalar to this ---> """
 
 * Serving Flask app "socialtracking" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat

"""

Using the link 'http://127.0.0.1:5000/' provided on line 15 we can access a live demo on our local machine using the 
web browser.
 
CTRL+C will stop the live demo in the terminal.
 
From there the user can register for an account. Then log in. Once logged in entries can be created, deleted, modified, 
and searched for. It's important to note that clicking on the name on a post will redirect to a new page will all of the 
post information and the ability to modify and delete the post.
 
One feature that may not be seen when looking at the website in the demo is while browsing all of the entries each page has a 
max of 4 entries. Additional pages get created when there are more entries added by the user.
 
Struggles:
 
When coding the application one hurdle that I had to overcome was adding the search bar to my app, allowing users to search 
for a specific entry that they added. Throughout the project, I changed how the entries would be displayed, and when I did 
that it affected how the search bar would work.
 
Changing the code to become more modular was also difficult as things throughout the code had to be changed. 
An example being implementing the flask blueprint feature. Also separating all of the imports to there respective file.
 
Lastly and as explained in further detail in the reflection essay, I was not able to deploy my application.
