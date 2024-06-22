import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
	return [1,2,3,4,]

@app.get('/contact')
def get_list():
	return {"name": "Platzi"}

@app.get('/page', response_class=HTMLResponse)
def get_page():
	return """
		<h1>Pagina desde Python</h1>
		<p>Parrafo</p>
	"""

def run():
	store.get_categories()

if __name__ == '__main__':
	run()
