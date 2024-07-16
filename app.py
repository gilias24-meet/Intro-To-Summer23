from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return'''<html>
    <h1>welcome!</h1>
    <p>this is a photo galry</p>
    <img src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJpaWTviBwKxlBCAQujz_Jr3Fb2baDw7eRrg&s">
    <img src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcREcUrcH8BpmbJ7JAN8h68R9CcGICB-hFnLPw&s">
    <img src = "https://hips.hearstapps.com/hmg-prod/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg?crop=0.752xw:1.00xh;0.175xw,0&resize=1200:*" >
    <a href = "/food1">this is a link</a>
    <a href = "/pet1">pet</a>
    <a href = "/space1">space</a>
    </html>'''


@app.route('/food1')
def food_1():
    return'''
    <html>
    <img src = "https://media-cdn.tripadvisor.com/media/photo-s/17/9b/5e/5c/soshi-rolls.jpg">
    <a href = "/home">home</a>
    <a href = "/food2">food</a>
    </html>'''

@app.route('/food2')
def food_2():
    return'''
    <html>
    <img src = "https://lh4.googleusercontent.com/proxy/_HzODjbuNXBo7kt-3hLsJ33bdT0zVv8CNvqLNxGZeJTr8ndE67KtspSURfD5scHzsuZV4zoJGCY4sBel3mTvmhjD37ZCYnehKhHd4P9V_BndaecnW_h0pgMY7Jf0judh6QU">
    <a href = "/food3">this is a link</a>
    </html>'''

@app.route('/food3')
def food_3():
    return'''
    <html>
    <img src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSFCEc2WjXiOu7vFWstwAG3rFLQlxF0FeFdVw&s">
    <a href = "/home">home</a>
    </html>'''

@app.route('/pet1')
def food_3():
    return'''
    <html>
    <img src = "https://www.humanesociety.org/sites/default/files/2019/03/rabbit-475261_0.jpg">
    <a href = "/pet2">this is a link</a>

    </html>'''

@app.route('/pet2')
def food_3():
    return'''
    <html>
    <img src = "https://cdn.britannica.com/70/234870-050-D4D024BB/Orange-colored-cat-yawns-displaying-teeth.jpg">
    <a href = "/home">home</a>
    <a href = "/pet3">this is a link</a>
    </html>'''

@app.route('/pet3')
def food_3():
    return'''
    <html>
    <img src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT98wK4vTKvIm3q3V50bAl81vALllriVOOjmg&s">
    </html>'''

@app.route('/space1')
def space1():
    return'''
    <html>
    <img src = "https://cdn.mos.cms.futurecdn.net/2oNNWzMiyntgoVjmedmpdn.jpg">
    <a href = "/home">home</a>
    <a href = "/space2">this is a link</a>
    </html>'''

    @app.route('/space2')
def space2():
    return'''
    <html>
    <img src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQPevZcapaw0UrpzSfbp6baVvcO2CFtGalb9w&s">
    <a href = "/space3">this is a link</a>
    </html>'''

    @app.route('/space3')
def space3():
    return'''
    <html>
    <img src = "https://i.guim.co.uk/img/media/89b64eb2db109a9e7d4f0050fea63dcdb71c9069/0_256_3840_2304/master/3840.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=f3485c5a6759de6a08b39ccd2304fdb0">
    <a href = "/space1">/space1</a>
    </html>'''









    
if __name__ == '__main__':
    app.run(debug=True)