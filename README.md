# Keyword Search Web Application 

This is a Keyword Search Web Application built with Flask

## Description

This flask web application is structured into the following files:
 - a __init__.py file that initializes the application
 - a routes.py file to map out all the routes/views
 - a search.py file which contains the file path and keyword search function
 - a forms.py which contains the forms built using wtforms

 For styling, bootstrap was used overall with some custom changes. Datatables.js was used to style the results table of the search. 
 Boostrap files were pulled via CDN and would need an internet connection to reflect.
 Templates are in jinja.

 The document ```Test File.txt``` is placed inside the static directory.

```
wordsearch-app
│   README.md
│   requirements.txt   
│   __init__.py
│   forms.py
│   routes.py
│   search.py 
└───static
│   │   custom.css
│   └───doc
│       │   Test File.txt
└───templates
    │   base.jinja2
    │   result.jinja2
    │   wordsearch.jinja2
```

## How Keyword Search Works

On runtime, the user can input a keyword to search the provided file. The file is then opened and the search function is applied.

Keyword search utilizes built-in python modules since they are all built on C and would be much faster than using loops to implement known algorithms. 
The IN Operator delivers the fastest substring search. To count the total occurences of a word/character/phrase, regex was used.

This is only a simple flask application and the file provided is just a small file with 33 lines.  If this were to scale, improvements can be made by:

- using flask blueprints for additional routes
- creating a database for the files/data to search on


