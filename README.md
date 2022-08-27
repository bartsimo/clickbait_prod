# Clickbait
#### Video Demo:  <URL HERE>
#### Description:
Clickbait is a flask app that enables to check whether a headline (in English language) is clickbait. In the background a machine learning (ML) model is used to classify whether a headline is clickbait or not. The app is live on the web and can be found [here](http://bartsimo.pythonanywhere.com/).

#### Usage:
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

#### Content (Files and Folders)
The app is a flask app which implies the structure for the app's file organization. For instance, html pages are stored in a folder called ``templates``, CSS-styles are stored in a folder called ``static``. 

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