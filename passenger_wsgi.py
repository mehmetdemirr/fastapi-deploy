from a2wsgi import ASGIMiddleware
from app.main import app  # Import your FastAPI app.

application = ASGIMiddleware(app)