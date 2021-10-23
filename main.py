from flask import Flask, render_template, request, redirect, flash
from werkzeug.utils import redirect
from controllers import bases



app = Flask(__name__)


@app.get('/')
def info():
     
     return render_template('index.html')
 
 
@app.post('/guardar')
def createBase():
    data = request.form
      
    if (data.getlist("check")):
        bases.creteBase(
        host=data["host"],
        user=data["usuario"],
        contra=data["contrasenia"],
        pueto=data["puerto"], 
        base=data["base"],
                    )
        
    else:
        datos=bases.getAllBases(
        host=data["host"],
        user=data["usuario"],
        contra=data["contrasenia"],
        pueto=data["puerto"], 
                    )
        return render_template('index.html', users = datos)
      
    
    
    return redirect('/')
 


 
app.run(debug=True)  
 









'''if (data['check']):
    retorno a platilla de mostrar info
else:
    return ren-....(/)'''