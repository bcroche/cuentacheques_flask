from flask import *
from calculaSolucion import ChequesSolver
app = Flask(__name__)
""" @app.route('/')
def hello_world():
    return 'Hello world!' """

posts = []
@app.route("/", methods=["GET", "POST"])
def index():
    return show_calcula_form()


def safeInt(cadena):
    if cadena == "":
        return 0
    else:
        return int(cadena)

@app.route("/cuenta/", methods=["GET", "POST"])
def show_calcula_form():
    if request.method == 'POST':
        cantidad = int (safeInt(request.form['cantidad']))

        
        lista = []
        lista.append(safeInt(request.form['cheque1']))
        lista.append(safeInt(request.form['cheque2']))
        lista.append(safeInt(request.form['cheque3']))
        cheques = []
        for c in lista:
            num = int(c)
            if num > 0:
                cheques.append(num)
        print("tipos:", cheques)
        cs =  ChequesSolver(cheques)
        res = cs.calcula(cantidad=cantidad)

        elems2 = [x for x in res.elementos if x[0]>0]
        print (cantidad,res.peso(), ": ", res.elementos)
        print ("Soluciones analizadas: ", cs.soluciones_analizadas)
        
        return render_template("resultado.html", cantidad=cantidad, peso=res.peso(),resultado=elems2)
        


        
        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('resultado'), cantidad, )    
    return render_template("cuenta.html")