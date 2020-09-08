from wtforms import Form, StringField, TextAreaField, BooleanField, validators
from wtforms import IntegerField
from wtforms.widgets import HiddenInput
from od_scraper import const


# Removes white spaces from strings
def strip_filter(x):
    return x.strip() if x else None


class AdminPanelForm(Form):
    # Scrap settings
    first_url = StringField('First page url', [validators.InputRequired(), validators.Length(min=1, max=255)],
                            filters=[strip_filter], default=const.MAIN_URL)
    range_from = IntegerField("Range from", [validators.InputRequired(), validators.NumberRange(min=1, max=1000)],
                              default=1)
    range_to = IntegerField("Range to", [validators.NumberRange(min=0, max=1000)],
                            default=0)

    # Email settings
    info_email = StringField('Email to inform', [validators.Email()], filters=[strip_filter])
    should_email = BooleanField('Inform about new offers', default=False)
    info_keywords = StringField('Inform offers keywords', filters=[strip_filter])

    # Custom validator of whole form
    def validate(self):
        res = super(AdminPanelForm, self).validate()

        # User needs to fill email field but only when 'should_email' is set to True
        if self.should_email.data and not self.info_email.data:
            msg = 'You need to fill email field if you want to enable this feature.'
            self.should_email.errors.append(msg)
            return False

        return res
