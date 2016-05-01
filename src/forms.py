from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, IntegerField, SelectField, RadioField
 
class ServiceRequestForm(Form):
  uid = IntegerField("User ID")
  types = [(1,'Personal Attendant Help'),(2,'Rental'),(3,'Repair Service'),(4,'Transports')]
  service_type = SelectField(u'Type', choices = types)
  urgency = SelectField(u'Urgency Level', choices = [(1,'Emergency'),(2,'Urgent'),(3,'Not Urgent')])
  location = TextAreaField("Address")

  gender_choices = [('male', 'Male'), ('female', 'Female'), ('any','No Preference')]
  gender = RadioField(u'Radio Preference', choices = gender_choices)
  submit = SubmitField("Send")

  #gender preference, crisis level, type, cid, address  

class ClientRegistrationForm(Form):
  first_name = TextAreaField("First Name")
  last_name = TextAreaField("Last Name")
  home_address = TextAreaField("Home Address")
  gender = RadioField(u'Gender', choices = [('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
  ec_first_name = TextAreaField("First Name")
  ec_last_name = TextAreaField("Last Name")
  submit = SubmitField("Register")

