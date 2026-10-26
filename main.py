from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Real-Time Sign Language Translator")

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Sign Language Translator</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 40px 20px;
                background: #f2f5f9;
            }
            .card {
                background: white;
                max-width: 500px;
                margin: auto;
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 4px 15px #0001;
            }
            h1 { color: #234; }
            p { color: #555; line-height: 1.6; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Sign Language Translator</h1>
            <p>Welcome to our Real-Time Sign Language Translator project!</p>
            <p>The web application is running successfully.</p>
            <p>Camera access and sign recognition will be added in later stages.</p>
        </div>
    </body>
    </html>
    """

@app.get("/health")
def health():
    return {"status": "running"}