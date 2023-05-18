from flask import Flask, render_template, request
from PIL import Image
from rembg import remove

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/remove_background', methods=['POST'])
def remove_background():
    if 'image' not in request.files:
        return render_template('index.html', error='No image selected.')

    image = request.files['image']
    if image.filename == '':
        return render_template('index.html', error='No image selected.')

    try:
        input_img = Image.open(image)
    except:
        return render_template('index.html', error='Invalid image file.')

    try:
        output_img = remove(input_img)
        output_path = 'static/output.png'  # Menyimpan gambar di dalam direktori "static"
        output_img.save(output_path)
        return render_template('result.html', output_path=output_path)
    except Exception as e:
        return render_template('index.html', error='An error occurred while processing the image.')

if __name__ == '__main__':
    app.run(debug=True)