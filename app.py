import os
import pyodbc
from dotenv import load_dotenv
from flask import Flask, render_template, jsonify
from flask_cors import CORS
# connect to t-sql server

load_dotenv()
AZURE_SQL_CONNECTIONSTRING = os.environ['AZURE_SQL_CONNECTIONSTRING']

app = Flask(__name__)
CORS(app)

def get_caselist_data():
    connection = pyodbc.connect(AZURE_SQL_CONNECTIONSTRING)
    cursor = connection.cursor()
    cursor.execute("""
        SELECT c.tournament_name, c.round_name, 
               t1.team_school AS aff_school, t1.team_code4 AS aff_code,
               t2.team_school AS neg_school, t2.team_code4 AS neg_code,
               c.aff_doc, c.neg_doc, c.yt_link
        FROM caselist c
        JOIN teams t1 ON c.aff_team = t1.team_id
        JOIN teams t2 ON c.neg_team = t2.team_id
        WHERE c.aff_team IS NOT NULL AND c.neg_team IS NOT NULL
    """)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    
    # Convert the data to a list of dictionaries
    data = [
        {
            'tournament_name': row[0],
            'round_name': row[1],
            'aff_school': row[2],
            'aff_code': row[3],
            'neg_school': row[4],
            'neg_code': row[5],
            'aff_doc': row[6],
            'neg_doc': row[7],
            'yt_link': row[8]
        }
        for row in data
    ]
    
    return data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/caselist')
def caselist_api():
    caselist_data = get_caselist_data()
    return jsonify(caselist_data)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(port)
    app.run(host="0.0.0.0", port=port, debug=True)
