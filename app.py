from flask import Flask,request,render_template,send_file
from pytube import YouTube
from io import BytesIO


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index2.html')

@app.route('/home')
def goback():
    return render_template('index2.html')

@app.route("/download",methods=['GET','POST'])
def download():
    if(request.method=='POST'):
        link = request.form['url']
        try:
            if link == '':
                 return render_template('error.html') 
            else:
                buffer = BytesIO()
                #link = request.form.get('url')
                yt = YouTube(link)
                ys = yt.streams.get_highest_resolution()
                ys.stream_to_buffer(buffer)
                buffer.seek(0)
                return send_file(buffer, as_attachment=True, download_name="video.mp4", mimetype="video/mp4")
        except:
            return render_template('error.html')  
    return render_template('index2.html')


if __name__ == "__main__":
    app.run(debug=True)
