import web
from web import form
from random import randint

otp_number = randint(10000,99999)
print otp_number

urls = (
  '/', 'hello')

app = web.application(urls, globals())
render = web.template.render('templates/')

number_form = form.Form( 
    form.Textbox('number',
                 form.notnull,
                 form.regexp('^-?\d+$', 'Not a number.'),
                 form.Validator('Not greater 10.', lambda x: int(x)>0),
                 description='OTP:'
                 ))

class hello:
    def GET(self):
        my_form = number_form()
        return render.hello(my_form)

    def POST(self): 
        my_form = number_form() 
        if not my_form.validates(): 
            return render.hello(my_form)
        else:
            number = my_form['number'].value
            print number
            if int(number) == otp_number:
                return 'otp verified'
            else:
                return "wrong otp"

if __name__ == "__main__":
    app.run()