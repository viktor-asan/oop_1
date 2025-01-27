from flask import Flask, render_template

#создать объект класса Flask
application = Flask(__name__)

@application.route('/',methods = ['POST','GET'])
def home():
 title = "Вход"
 #Проверка метода
 return render_template('login.html',title = title)


@application.route('/test')
def test():
   return "<h1>это тест</h1>"
@application.route('/param/<id>')
def admin():
    title='Панель Админа'

    return render_template ('admin.html',title=title)

 if __name__=="__main__":
   application.run(debug=True)
