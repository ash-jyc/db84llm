import os
import pyodbc, struct
from dotenv import load_dotenv
from azure import identity
from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

load_dotenv()
connection_string = os.environ['AZURE_SQL_CONNECTIONSTRING']

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get('/', response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get('/api/caselist')
def get_caselist():
    data = get_caselist_data()
    print("got data")
    return JSONResponse(content=jsonable_encoder(data))

def get_caselist_data():
    with get_conn() as conn:
        cursor = conn.cursor()
        print("cursor", cursor)
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

def get_conn():
    credential = identity.DefaultAzureCredential(exclude_interactive_browser_credential=False)
    token_bytes = credential.get_token("https://database.windows.net/.default").token.encode("UTF-16-LE")
    token_struct = struct.pack(f'<I{len(token_bytes)}s', len(token_bytes), token_bytes)
    SQL_COPT_SS_ACCESS_TOKEN = 1256  # This connection option is defined by microsoft in msodbcsql.h
    conn = pyodbc.connect(connection_string, attrs_before={SQL_COPT_SS_ACCESS_TOKEN: token_struct})
    return conn
