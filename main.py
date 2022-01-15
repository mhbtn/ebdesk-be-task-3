from flask import Flask, jsonify, request, make_response
import sqlite3
from model import Data
from formSubmission import FormSubmission
from searchYoutube import search_you

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/api', methods=['GET','POST', 'PUT', 'DELETE'])
def youtube():
    try:
        dt = Data()
        values = ()
        if request.method == 'GET':
            search_ = request.args.get("search")
            if search_:
                query = "SELECT * FROM trending_youtube WHERE channel_name LIKE \'%{}%\' OR channel_name LIKE \'%{}%\' OR title LIKE \'%{}%\' OR publish_date LIKE \'%{}%\' ORDER BY publish_date DESC".format(search_, search_, search_, search_)
                data = dt.get_data(query)
            else:
                id_ = request.args.get("id")
                if id_:
                    check_exist = "SELECT * FROM trending_youtube WHERE id = %s" % id_
                    if len(dt.get_data(check_exist)) == 0:
                        data = [{
                            "messgae": "id tidak ditemukan"
                        }]
                    else:
                        query = check_exist
                        data = dt.get_data(query)
                else:
                    query = "SELECT * FROM trending_youtube ORDER BY publish_date DESC"
                    data = dt.get_data(query)

        elif request.method == 'POST':
            validate = FormSubmission(request.form)
            if validate.validate() == False:
                data = validate.errors
            else:
                get_data_from_form = request.form.to_dict()
                query = "INSERT INTO trending_youtube(channel_id, channel_name, title, publish_date) VALUES('{}','{}','{}','{}')".format(get_data_from_form['channel_id'], get_data_from_form['channel_name'], get_data_from_form['title'], get_data_from_form['publish_date'])
                data = dt.insert_data(query)

        elif request.method == 'PUT':
            id_ = request.args.get("id")
            if id_:
                check_exist = "SELECT * FROM trending_youtube WHERE id = %s" % id_
                if len(dt.get_data(check_exist)) == 0:
                    data = [{
                        "messgae": "id tidak ditemukan"
                    }]
                else:
                    validate = FormSubmission(request.form)
                    if validate.validate() == False:
                        data = validate.errors
                    else:
                        get_data_from_form = request.form.to_dict()
                        query = "UPDATE trending_youtube SET channel_id = '{}', channel_name = '{}', title = '{}', publish_date = '{}' WHERE id = {}".format(get_data_from_form['channel_id'], get_data_from_form['channel_name'], get_data_from_form['title'], get_data_from_form['publish_date'], id_)
                        data = dt.update_data(query, id_, get_data_from_form)
            else:
                data = [{
                    "message": "belum memasukkan id"
                }]

        else:
            id_ = request.args.get("id")
            if id_:
                check_exist = "SELECT * FROM trending_youtube WHERE id = %s" % id_
                if len(dt.get_data(check_exist)) == 0:
                    data = [{
                        "messgae" : "id tidak ditemukan"
                    }]
                else:
                    query = "DELETE FROM trending_youtube WHERE id = {}".format(id_)
                    data = dt.delete_data(query, id_)

            else :
                data = [{
                    "message" : "belum memasukkan id"
                }]
    except Exception as e:
        return make_response(jsonify({'error' : str(e)}), 400)
    return make_response(jsonify({'data' : data}), 200)

@app.route('/search', methods=['GET'])
def search_youtube():
    search_ = request.args.get('search_query')
    if search_:
        data = search_you(search_)
    else:
        data = [{
            "message" : "anda belum memasukkan argumen search_query"
        }]
    return make_response(jsonify({
        "data": data
    }))

app.run(port=9999)