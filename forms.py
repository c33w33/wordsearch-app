# wtforms used to utilize built-in validators and enables markupsafe
from wtforms import Form, BooleanField, StringField, validators, SubmitField
from wtforms.validators import InputRequired

# contains class searchform which shows all the fields provided for user input


class SearchForm(Form):
    keyword = StringField("Keyword", validators=[InputRequired(message=("Please enter keyword to proceed."))], render_kw={
                          "type": "text", "placeholder": "keywords", "class": "form-control", "id": "floatingInput"})
    search = SubmitField('Search')
    matchcase = BooleanField("Match cases", false_values=(0, False))
    onlywhole = BooleanField("Find exact word/phrase matches", render_kw={
                             "data-toggle": "tooltip", "data-placement": "below", "title": "matches are preceded and followed by a space"}, false_values=(0, False))
