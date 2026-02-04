import time
import logging
from fastapi import FastAPI, Request, Query, status, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from Maths.mathematics import summation, subtraction, multiplication, division

# --- 1. LOGGING CONFIGURATION ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

# --- 2. APP INITIALIZATION ---
app = FastAPI(
    title="MathOps Enterprise API",
    description="A robust, production-ready REST API for mathematical operations.",
    version="1.0.0",
    contact={
        "name": "Denis Naumov",
        "url": "https://github.com/DenisNaumov7777",
        "email": "denis@example.com",
    },
)

# --- 3. MIDDLEWARE CONFIGURATION ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """Middleware to log request duration and add X-Process-Time header."""
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    logger.info(f"Path: {request.url.path} | Method: {request.method} | Duration: {process_time:.4f}s")
    return response

# --- 4. TEMPLATES SETUP ---
templates = Jinja2Templates(directory="templates")

# --- 5. EXCEPTION HANDLERS ---
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Custom handler for 422 errors to provide user-friendly messages."""
    logger.warning(f"Validation error: {exc}")
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"message": "Invalid Input: Please ensure you entered valid numbers, not text."}
    )

# --- 6. HELPER FUNCTIONS ---
def process_result(val: float) -> str:
    """Formats float to string, removing trailing .0 if integer."""
    if val.is_integer():
        return str(int(val))
    return str(val)

# --- 7. ROUTES ---

@app.get("/health", tags=["System"])
def health_check():
    """System health check endpoint for monitoring tools."""
    return {"status": "ok", "service": "MathOps API", "version": "1.0.0"}

@app.get("/sum", tags=["Math Operations"])
def sum_route(
    num1: float = Query(..., description="First operand"),
    num2: float = Query(..., description="Second operand")
):
    """Calculate the sum of two numbers."""
    logger.info(f"OP: SUM | {num1} + {num2}")
    return process_result(summation(num1, num2))

@app.get("/sub", tags=["Math Operations"])
def sub_route(
    num1: float = Query(..., description="First operand"),
    num2: float = Query(..., description="Second operand")
):
    """Calculate the difference."""
    logger.info(f"OP: SUB | {num1} - {num2}")
    return process_result(subtraction(num1, num2))

@app.get("/mul", tags=["Math Operations"])
def mul_route(
    num1: float = Query(..., description="First operand"),
    num2: float = Query(..., description="Second operand")
):
    """Calculate the product."""
    logger.info(f"OP: MUL | {num1} * {num2}")
    return process_result(multiplication(num1, num2))

@app.get("/div", tags=["Math Operations"])
def div_route(
    num1: float = Query(..., description="Dividend"),
    num2: float = Query(..., description="Divisor")
):
    """
    Calculate the quotient. 
    Handles division by zero by returning a 400 Bad Request.
    """
    logger.info(f"OP: DIV | {num1} / {num2}")
    try:
        result = division(num1, num2)
        return process_result(result)
    except ValueError as e:
        logger.warning(f"Math Error: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e) # Sends "Cannot divide by zero" to frontend
        )

@app.get("/", response_class=HTMLResponse, tags=["Frontend"])
def render_index_page(request: Request):
    """Serves the interactive web interface."""
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    import uvicorn
    # Configuration for direct execution (e.g. inside Theia lab)
    uvicorn.run(app, host="0.0.0.0", port=8080)