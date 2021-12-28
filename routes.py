# this file contains all route details
# this 1-page app routes all  get and post requests to '/'
from flask import render_template, request
from flask import current_app
from forms import SearchForm
from search import doc_path, search_doc

# application factory is implemented


@current_app.route("/", methods=['GET', 'POST'])
def keywordsearch():
    form = SearchForm(request.form)
    if request.method == 'POST' and form.validate():
        # get all form inputs and store into variables
        # process into the search function
        keyword = form.keyword.data
        matchcase = form.matchcase.data
        onlywhole = form.onlywhole.data
        result = search_doc(keyword=keyword, matchcase=matchcase,
                            onlywhole=onlywhole, doc_path=doc_path)
        return render_template(
            # template being rendered is a combination of a basic template and the results template
            "wordsearch.jinja2",
            form=form,
            result=result[0],
            cnt=result[1],
            str_cnt=result[2],
            title='Keyword Search | Results'
        )
    else:
        return render_template(
            "wordsearch.jinja2",
            form=form,
            title='Keyword Search'
        )
