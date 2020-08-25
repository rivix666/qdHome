from wtforms import Form, StringField, TextAreaField, validators
from wtforms import IntegerField
from wtforms.widgets import HiddenInput


strip_filter = lambda x: x.strip() if x else None

class DbMgrForm(Form):
    first_url = StringField('First page url:', [validators.InputRequired(), validators.Length(min=1, max=255)],
                            filters=[strip_filter])
    range_from = IntegerField("Range from:", [validators.InputRequired(), validators.NumberRange(min=1, max=1000)])
    range_to = IntegerField("Range to:", [validators.NumberRange(min=0, max=1000)])

    # TODO write custom validators that would use od_scraper

