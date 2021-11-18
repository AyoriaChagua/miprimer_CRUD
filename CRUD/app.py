from flask import Flask, render_template, request,redirect, url_for, flash
from controller import *
from werkzeug.utils import redirect
import os 


app = Flask(__name__, template_folder = 'templates')

CARPETA = os.path.join('uploads')
app.config['CARPETA'] = CARPETA

app.secret_key = 'mysecretkey'



@app.route('/')
def index():
    shoes = get_shoes()
    return render_template('index.html', shoes = shoes)
    
@app.route('/insert')
def create():
    return render_template('insert.html',)


@app.route('/add', methods=['POST'])
def add_shoes():
    if request.method == 'POST':
        id = request.form['id']
        model = request.form['model']
        price = request.form['price']
        brand = request.form['brand']
        size = request.form['size'] 
        image = request.files['image']
        nuevoNombreImagen = format_an_image(image)
        insert_shoes(id, model, price,brand , size, nuevoNombreImagen)
        flash('Shoes addes successfully')
        return redirect('/insert')


@app.route('/delete/<string:id>')
def delete_shoes(id):
    fila = delete_an_image(id)
    os.remove(os.path.join(app.config['CARPETA'], fila[0][0]))
    delete_shoe(id)
    flash('Shoes removed successfully')
    return redirect('/')



@app.route('/edit/<id>')
def edit_shoes(id):
    data = get_shoe_edit(id)
    return render_template('edit_shoes.html', data = data[0] )



@app.route('/update/<id>', methods=['POST'])
def update_shoes(id):
    if request.method == 'POST':
        model = request.form['model']
        price = request.form['price']
        brand = request.form['brand']
        size = request.form['size']
        image = request.files['image']
        image_ant = request.form['image_ant']
        fila = upload_an_image(image, id)
        if fila != None:
            os.remove(os.path.join(app.config['CARPETA'], image_ant))
            nuevonombre_img = format_an_image(image)
            update_shoe(id, model, price, brand, size,nuevonombre_img)
        else:
            
            update_shoe(id, model, price, brand, size,image_ant)
        flash('Shoes updated Successfully')
        return redirect(url_for('edit_shoes', id = id))



if __name__ == '__main__':
    app.run(port=3000, debug=True)