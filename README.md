# Clickbait
#### Video Demo:  <URL HERE>
#### Description:
Clickbait is a flask app that enables to check whether a headline is clickbait. In the background a machine learning model is used to classify whether a headline is clickbait or not.

#### Usage:
Users can enter or copy text in a text box and click a button to check whether the text is clickbait. The design was chosen to be clean and focused on the functionality in order to facilitate usage.

#### Technologies used:
+ Python (see requirements.txt for additional packages)
+ Flask
+ Jinja
+ HTML
+ CSS
  + Bootstrap (5.1)

#### Content (Files and Folders)
The app is a flask app which implies the structure for the app's file organization. For instance, html pages are stored in a folder called ``templates``, CSS-styles are stored in a folder called ``static``.

##### templates
Contains the HTML files for the app:
+ about.html
+ home.html
+ layout.html
+ result.html

**about.html** Consists of a html version of this README.md. It extends layout.html using jinja syntax.
**home.html** 