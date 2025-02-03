from flask import Flask, render_template, request,redirect 

#создать объект класса Flask
application = Flask(__name__)

@application.route('/',methods = ['POST','GET'])
def home():
 title = "Вход"
 message =''
 login = request.form.get('login')
 password = request.form.get('password')

 if request.method =='POST':
     if UserController.auth(login,password):
         return redict('/admin')
     else:
         message= 'Не верный логин или пароль'


 return render_template('login.html',title = title,
                        message = message)


@application.route('/test')
def test():
   return "<h1>это тест</h1>"
@application.route('/param/<id>')
def admin():
    title='Панель Админа'

    return render_template ('admin.html',title=title)
if __name__=="__main__":
   application.run(debug=True, host = '0.0.0.0')
