import logging
from flask import Flask, render_template, request,json, redirect,session,url_for
from flaskext.mysql import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.wsgi import LimitedStream
import os,uuid,bz2
app = Flask(__name__)

app.secret_key = 'why would I tell you my secret key?'
mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'bucketlist'
app.config['MYSQL_DATABASE_HOST'] = 'db'
#app.config['MYSQL_DATABASE_HOST'] = 'localhost'


mysql.init_app(app)

	
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['UPLOAD_FOLDER_USERPHOTO'] ='static/UserPhoto'
@app.route("/")
def main():
    return render_template('index.html')
 
@app.route("/showSignUp")
def showSignUp():
    return render_template('signup.html')
 
@app.route("/signUp",methods=['POST'])
def signUp():
    _name = request.form['inputName']
    _email= request.form['inputEmail']
    _password = request.form['inputPassword']    
    _hashed_password = generate_password_hash(_password)
    #_hashed_password = bz2.compress(bytes(_password))
    if request.form.get('filePath') is None:
        _photopath = ''
    else:
        _photopath = request.form.get('filePath')
        
    conn = mysql.connect()
    cursor = conn.cursor()
    if((_name and _email and _password) or _photopath ):
        print(_name , _email,_password)
        cursor.callproc('sp_createUser1',(_name,_email,_hashed_password,_photopath))
        data = cursor.fetchall()
        if len(data) is 0:
            conn.commit()
            return json.dumps({'message':'User created successfully !'})
        else:
            return json.dumps({'error':str(data[0])})
    else:
        return json.dumps({'html':'<span>Enter required fields</span>'})
    
@app.route("/showSignin")
def showSignin():
    return render_template('signin.html')

@app.route('/validateLogin',methods=['POST'])
def validateLogin():
    try:
        _username = request.form['inputEmail']
        _password = request.form['inputPassword']
    
        con = None
        cursor = None
        con = mysql.connect()
        cursor = con.cursor()
        cursor.callproc('sp_validateLogin',(_username,))

        data = cursor.fetchall()

        if(len(data)>0):
            #password = bz2.decompress(bytes(str(data[0][3])))
            #if password == _password:
            if check_password_hash(str(data[0][3]),_password):            
                session['user'] = data[0][0]
                session['username'] = data[0][1]
                session['user_username'] =data[0][2]
                session['password'] = data[0][3]
                session['user_photo'] = data[0][4]
                return redirect('/showDashboard1')
            else:
                return render_template('error.html',error= "Wrong User name or password")
        else:
            return render_template('error.html',error= "Wrong User name or password")
        
    except Exception as e:
        logging.error("Database error:%s",str(e))
        return render_template('error.html',error= str(e))
    finally:
        if cursor:
            cursor.close()
        if con:    
            con.close()
       

@app.route('/userHome')
def userHome():
    if session.get('user'):
        return render_template('userHome.html')
    else:
        return render_template('error.html',error = 'Unauthorized Access')

@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect('/')

@app.route('/showAddwish')
def showAddwish():
    return render_template('addwish.html')

@app.route('/addWish',methods=['POST'])
def addWish():
    try:
        if(session.get('user')):
            _title = request.form['inputTitle']
            _desc = request.form['inputDescription']
            _user_id = session.get('user')
            if request.form.get('filePath') is None:
                _filePath = ''
            else:
                 _filePath= request.form.get('filePath')

            if request.form.get('private') is None:
                _private = 0
            else:
                _private = 1

            if request.form.get('done') is None:
                _done = 0
            else:
                _done = 1    
            #connect to Database

            con = mysql.connect()
            cursor = con.cursor()
            cursor.callproc('sp_addWish',(_title,_desc,_user_id,_filePath,_private,_done))
            data = cursor.fetchall()

            if len(data) is 0:
                con.commit()
                return redirect('/userHome')
            else:
                return render_template('error.html',error='Error Occurred')
        else:
           return render_template('error.html',error='Unauthorized Access')
    except Exception as e:
        return render_template('error.html',error=str(e))
    finally:
        cursor.close()
        con.close()

@app.route('/getWish')
def getWish():
    try:
        if(session.get('user')):
            _user = session.get('user')
            con= mysql.connect()
            cursor = con.cursor()
            cursor.callproc('sp_getWishByUser',(_user,_user))
            wishes = cursor.fetchall()
            wishes_dict = []
            
            for wish in wishes:
                wish_dict ={
                    "Id": wish[0],
                    "Title": wish[1],
                    "Description": wish[2],
                    "Date": wish[4]}
                wishes_dict.append(wish_dict)

            return json.dumps(wishes_dict)
            
        else:
            return render_template('error.html',error= "Unauthorized Access")
    except Exception as e:
         return render_template('error.html',error=str(e))
    finally:
        cursor.close()
        con.close()
              
@app.route('/getWishById',methods=['POST'])
def getWishById():
    try:
        if session.get('user'):
 
           _id = request.form['id']
           _user = session.get('user')
 
           conn = mysql.connect()
           cursor = conn.cursor()
           cursor.callproc('sp_GetWishById',(_id,_user))
           result = cursor.fetchall()
 
           wish = []
           wish.append({'Id':result[0][0],'Title':result[0][1],'Description':result[0][2],'FilePath':result[0][3],'Private':result[0][4],'Done':result[0][5]})
 
           return json.dumps(wish)
        else:
            return render_template('error.html', error = 'Unauthorized Access')
    except Exception as e:
        return render_template('error.html',error = str(e))                                
 
@app.route('/updateWish',methods=['POST'])
def updateWish():
    try:
        
        if session.get('user'):
            _user = session.get('user')
            _title = request.form['title']            
            _description = request.form['description']            
            _id = request.form['id']            
            _filePath = request.form['filePath']
            _isPrivate = request.form['isPrivate']
            _isDone = request.form['isDone']
            conn = mysql.connect()
            cursor = conn.cursor()
            
            cursor.callproc('sp_updateWish',(_title,_description,_id,_user,_filePath,_isPrivate,_isDone))
            data = cursor.fetchall()
            
            if len(data) is 0:
                
                conn.commit()
                return json.dumps({'Status':'OK'}) 
            else:
                
                return json.dumps({'Status':'error'})
            
        else:
            return render_template('error.html', error = 'Unauthorized Access')
    except Exception as e:
        return render_template('error.html',error = str(e))
    finally:
        cursor.close()
        conn.close()

#Update User
@app.route('/updateUser',methods=['POST'])
def updateUser():
    try:
        
        if session.get('user'):
            _user_id = session.get('user')
            _name = request.form['name']            
            _username = request.form['username']            
            _password = request.form['password']           
            _userPhotoPath = request.form['userphoto']
          
            conn = mysql.connect()
            cursor = conn.cursor()
            
            cursor.callproc('sp_updateUser',(_name,_username,_password,_userPhotoPath,_user_id))
            data = cursor.fetchall()
            
            if len(data) is 0:
                
                conn.commit()
                return json.dumps({'Status':'OK'}) 
            else:
                
                return json.dumps({'Status':'error'})
            
        else:
            return render_template('error.html', error = 'Unauthorized Access')
    except Exception as e:
        return render_template('error.html',error = str(e))
    finally:
        cursor.close()
        conn.close()        
        

@app.route('/deleteWish',methods=["POST"])
def deleteWish():
    try:
        
        if session.get('user'):
            _user = session.get('user')
            _id = request.form['id']
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.callproc('sp_deleteWish',(_id,_user))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return json.dumps({'Status':'OK'})
            else:
                return json.dumps({'Status':'error'})
            
        else:
            return render_template('error.html',error ='Unauthorized Access')
    except Exception as e:
        return render_template('error.html',error=str(e))
    finally:
        cursor.close()
        conn.close()

# -- File upload --
@app.route('/upload',methods=['GET','POST'])
def upload():
    if request.method == "POST":
        file =  request.files['file']
        
        #extension = os.path.splitext(file.filename)[1]
        #f_name = str(uuid.uuid4()) + extension

        file.save(os.path.join(app.config['UPLOAD_FOLDER'],file.filename))
        print(file.filename)
        return json.dumps({'filename':file.filename})

# -- File upload User photos --
@app.route('/uploadUserPhoto',methods=['GET','POST'])
def uploadUserPhoto():
    if request.method == "POST":
        file =  request.files['file']
        
        #extension = os.path.splitext(file.filename)[1]
        #f_name = str(uuid.uuid4()) + extension

        file.save(os.path.join(app.config['UPLOAD_FOLDER_USERPHOTO'],file.filename))
        print(file.filename)
        return json.dumps({'filename':file.filename})    

#-- DashBoard---
@app.route('/showDashboard')
def showDashboard():
    return render_template('dashboard.html')

#-- DashBoard updated--- currently in use
@app.route('/showDashboard1')
def showDashboard1():    
    return render_template('Dashboard1.html', userid =session['user'],  username=session['username'],user_username= session['user_username']
                           ,pwd =session['password'],userphoto=session['user_photo'] )


#-- Get All wishes --
@app.route('/getAllWishes')
def getAllWishes():
    try:
        if session.get('user'):
        
            conn = mysql.connect()
            cursor = conn.cursor()
            _user= session.get('user')
            cursor.callproc('sp_GetAllWishes',(_user,))
            result = cursor.fetchall()

            wishes_dict=[]
            for wish in result:
                wish_dict={ 'Id': wish[0],
                        'Title': wish[1],
                        'Description':wish[2],
                        'FilePath': wish[3],
                        'Like':wish[4],
                        'HasLiked':wish[5]}
                wishes_dict.append(wish_dict)
        
            return json.dumps(wishes_dict)
        else:
            return render_template('error.html',error ='Unauthorized Access')
    except Exception as e:
        return render_template('error.html',error=str(e))
    finally:
        cursor.close()
        conn.close()

@app.route('/getAllWishesByUser',methods=['POST'])
def getAllWishesByUser():
    #print("hi hi out ")
    try:
        if session.get('user'):
            
            conn = mysql.connect()
            cursor = conn.cursor()
            _selecteduser =  request.form['id1']
            _user = session.get('user')
            #print(_user)
            cursor.callproc('sp_getWishByUser',(_user,_selecteduser))
            result = cursor.fetchall()

            wishes_dict=[]
            for wish in result:
                wish_dict={ 'Id': wish[0],
                        'Title': wish[1],
                        'Description':wish[2],
                        'FilePath': wish[3],
                        'Like':wish[4],
                        'HasLiked':wish[5]}
                wishes_dict.append(wish_dict)
            #print(wishes_dict)
            return json.dumps(wishes_dict)
        else:
            return render_template('error.html',error ='Unauthorized Access')
    except Exception as e:
        return render_template('error.html',error=str(e))
    finally:
        cursor.close()
        conn.close()
        
#-- Add / Update Likes ---
@app.route('/addUpdateLike',methods=['POST' ])
def addUpdateLike():
    try:
        if session.get('user'):
            
            _wishId = request.form["wish"]
            _like = request.form["like"]
            _user = session.get('user')

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_AddUpdateLikes',(_wishId,_user,_like))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                cursor.close()
                conn.close()               
            else:
                return render_template('error.html',error="An error ocurred")

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_getLikeStatus',(_wishId,_user))
            result = cursor.fetchall()
            return json.dumps({'status':'OK','total':result[0][0],'likeStatus':result[0][1]})
        else:
            return render_template('error.html',error="Unauthorized access") 
                               
    except Exception as e:
        return render_template( 'error.html',error= str(e))              
    finally:
        cursor.close()
        conn.close()

#-- Get All User --
@app.route('/getAllUsers')
def getAllUsers():
    try:
        if session.get('user'):
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_GetAllUsers')
            result= cursor.fetchall()

            users_list =[]
            for user in result:
                user_dict={"Id":user[0],
                           "UserName":user[1],
                           "UserPhoto":user[2]}
                if session.get('user') != user[0]:
                    users_list.append(user_dict)
                
            
            print(result)
            return json.dumps(users_list)
        else:
            return render_template('error.html',error="Unauthorized access")
    except Exception as e:
        return render_template('error.html',error=str(e))
    finally:
        cursor.close()
        conn.close()
        
        
    
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5001)
    #app.run(port=5001)
  