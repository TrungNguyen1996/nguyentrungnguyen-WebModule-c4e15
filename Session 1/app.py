from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html') #Hello world

@app.route('/Hello')
def hello():
    return "hello C4E 15"

@app.route('/sayhi/<name>')
def sayhi(name):
    return "Hello" + name

@app.route('/sum/<int:a>/<int:b>')
def sum(a, b):
    return str(a + b)

@app.route('/html')
def heading():
    return "<h1>Gì cũng được</h1>"
############################################################################
@app.route('/blog')
def blog():

    article_name = 'Thơ con cóc'
    posts = [
    {
        "Content" : "Phấn khởi",
        "author" : "Nguyên"
    },
    {
        "Content" : "Len",
        "author" : "Anh"
    },
    {
        "Content" : "Xuong",
        "author" : "Quang"
    },
    {
        "Content" : "Nam",
        "author" : "Tuan"
    }

    # "Phấm khởi",
    # "Táp bao tử",
    # "Tứ bao tải",
    # "Gái bao tử",
    ]
# goi ten file torng temple
    return render_template('blog.html',
                        article_title=article_name,
                        posts=posts)
###################################################
@app.route('/user/<user_name>')
def showlentatca(user_name): #Ham
    user_list= [
    {"username" : "Trung Nguyen", "name" : "Nguyen Trung Nguyen", "Age" :"22", "Gender" : "male", "Like" : "keo"},
    {"username" : "Trung Nguyen", "name" : "Nguyen Nhat Quang", "Age" : "27", "Gender" : "male", "Like" : "keo"},
    {"username" : "Trung Nguyen", "name" : "Nguyen Quang Nguyen", "Age" : "20", "Gender" : "male", "Like" : "keo"},
    {"username" : "Trung Nguyen", "name" : "Nguyen Nhat Nguyen", "Age" : "18", "Gender" : "male", "Like" : "keo"},
    {"username" : "Trung Nguyen", "name" : "Nguyen Trung Quang", "Age" : "38", "Gender" : "male", "Like" : "keo"},
    {"username" : "Trung Nguyen", "name" : "Nguyen Trung Tuan", "Age" : "22", "Gender" : "male", "Like" : "keo"},

    ]

    return render_template ( 'Nguyen.html',
                        user_name)



if __name__ == '__main__':
  app.run(debug=True)


# def khong dau cach
#
