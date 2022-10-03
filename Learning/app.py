from flask import*
import pyshorteners
app=Flask(__name__)

@app.route('/',methods=["GET","POST"])
def student():
    if request.method == 'POST':
        link = request.form.get('name')
        ct=pyshorteners.Shortener()
        fi=ct.tinyurl.short(link)
        return str(fi)
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True,port=3445)
#HTML(file)
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="'UTF-8">
    <title>link Shortener</title>
</head>
<body>
    <h1>*Hi,welcome to the website*</h1>
    <form action="/" method="POST">
    <input type="text" name="name" placeholder="Enter ur URL">
    <input type="submit">
    </form>
</body>
</html>
