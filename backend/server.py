import sys
import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

# Add project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.main import run_pipeline
from src.semantic.semantic_errors import SemanticError

app = FastAPI()

# Enable CORS for frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CompileRequest(BaseModel):
    code: str
    geometry_mode: Optional[str] = "segmented"

@app.post("/compile")
async def compile_code(request: CompileRequest):
    try:
        gcode = run_pipeline(request.code, request.geometry_mode)
        return {"gcode": gcode}
    except SyntaxError as e:
        raise HTTPException(status_code=400, detail=f"Syntax Error: {str(e)}")
    except SemanticError as e:
        raise HTTPException(status_code=400, detail=f"Semantic Error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    return {"content": content.decode("utf-8"), "filename": file.filename}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
