# Clickbait
#### Video Demo:  <URL HERE>
#### Description:
Clickbait is a flask app that enables to check whether a headline (in English language) is clickbait. In the background a machine learning (ML) model is used to classify whether a headline is clickbait or not. The app is live on the web and can be found [here](http://bartsimo.pythonanywhere.com/).

#### Usage:
Navigate to http://bartsimo.pythonanywhere.com/.
Users can enter or copy text in a text box and click a button to check whether the text is clickbait. The design was chosen to be clean and focused on the functionality in order to facilitate usage.

#### ML model:
The model (in model.py) consists of a Naive Bayes classifier. It was trained on approx. 22.000 headlines from various news outlets (mostly newspapers). Subsequently, the model was tested on another approx. 11.000 headlines. The data can be obtained from [Kaggle](https://www.kaggle.com/datasets/amananandrai/clickbait-dataset). For performance reasons in the app, the trained model as well as the sparse matrix of token counts from the clickbait dataset were dumped in .pkl files. In the app, these .pkl files are loaded statically once vs. building the model and token matrix with each request.

#### Database:
The app contains a SQL database that stores each posted request together with the respective result from the model as well as the date and time of the request for potential later use. It stores nothing else.

#### Technologies used:
+ Python (see requirements.txt for additional packages)
+ Flask
+ Jinja
+ HTML
+ CSS
  + Bootstrap (5.1)
+ SQL (SQLite3)
+ Deployment on pythonanywhere.com

#### Content (Files and Folders)
The app is a flask app which implies the structure for the app's file organization. For instance, html pages are stored in a folder called ``templates``, CSS-styles are stored in a folder called ``static``. 

#### [Naive Bayes](https://en.wikipedia.org/wiki/Naive_Bayes_spam_filtering)
Relies on Bayes' Theorem and is commonly used in text classification due to its good relation between prediction accuracy and computational performance. sklearn's representation of the Multinomial Naive Bayes classifier deals with the "zero probability" problem (user may input word that was not present in the test/training data) by employing LaPlace smoothing. 

#### pythonanywhere.com
The app is live on pythonanywhere.com. Pythonanywhere enables hosting of python web apps. The service needs a requirements.txt file to recreate the environment on its server for the flask app (pip freeze > requirements.txt). GitHub repo (https://github.com/bartsimo/clickbait_prod) was cloned to pythonanywhere. On pythonanywhere a virtual environment needs to be created such that the app can be served. In this environment the requirements.txt need to be installed. The WSGI config file needed to be customized, specifying the path where the app is saved and specifying Flask.

##### templates
Contains the HTML files for the app:
+ about.html
+ home.html
+ layout.html
+ result.html
All html files extend layout.html using jinja syntax.

**about.html** Contains links to CS50, the README and the YouTube documentation. 
**home.html** Contains landing page, brief introduction of the app and a text area in which users can enter headlines that they would like to have checked for clickbait.
**layout.html** Provides a template for the other html-pages. Makes extensive use of Bootstrap 5. Defines a navbar and footer that is identical for all pages. Pages that "inherit" from layout.html can define own titel and main.
**result.html** Displays the result of the clickbait check from the user's input as returned by the ML model. Lets you return to home for repeated clickbait checks.

##### static
In addition to styling the html sites with Bootstrap, custom CSS is used. 
**styles.css** contains custom color and margin settings. Most importantly, it defines the responsiveness of the appearance. Based on width of the viewport, margins and text alignment is set here.

##### app.py
Contains backend of the app. Comments of specific features:
+ By using the path() method, ROOT was initialized to declare a path database path that works when developing locally as well as when the files are accessed on the production server of pythonanywhere.com.
+ The app operates such that templates are automatically reloaded and no cookies are used.
+ Furthermore, server-side responses are not cached.
+ On home.html ("/"), once the button is clicked, the route ("/predict") is called. Here,
  + a db connection is established
  + the user input is retrieved and put into a vector-like format (necessary format for model prediction)
  + also, the token matrix and the ml model are loaded, the token matrix is put into an array format **with the newly added user input**.
  + based on the user input and the trained model, the prediction is retrived
  + data is sent to result.html for the user to see
  + data is sent to db for storage

##### clickbait_data.csv
Data from [Kaggle](https://www.kaggle.com/datasets/amananandrai/clickbait-dataset) for reproduction.

##### clickbait_model.pkl and cv_vocab.pkl
Contains the trained Naive Bayes ML model with the data it was trained and tested on. Output from model.py that is used in app.py.

##### clickbait.db
The database. Stored data can be infered from the commands executed to set up db:
CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE entries (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, headline TEXT, time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, prediction INTEGER NOT NULL);

##### model.py
Parses the kaggle data into dataframes. After that it uses several methods from Pythons sklearn library. Please refer to the comments in model.py to see which methods were used and what these methods do.

##### requirements.txt
Summarizes the necessary packages that need to be installed (e.g. via pip install package from the Terminal) for the app to run. Initially produced automatically from VS Code but needed to be customized to meet requirements on pythonanywhere.com.

