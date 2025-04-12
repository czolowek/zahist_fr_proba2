from flask_wtf import FlaskForm
import wtforms


class ReviewForm(FlaskForm):
    text = wtforms.StringField("введить свiй вiдгук про данний товар", validators=[wtforms.validators.length(5, message="вiдгук повинен бути не менше 5 символiв")])
    name = wtforms.StringField("введить своє iм'я", validators=[wtforms.validators.DataRequired()])
    submit = wtforms.SubmitField("додати вiдгук")
