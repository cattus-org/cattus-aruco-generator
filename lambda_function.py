import io
import base64
from PIL import Image
from mangum import Mangum
from pydantic import BaseModel, Field
from fastapi import FastAPI, HTTPException, Query, Depends

from aruco_generator import ArucoGenerator

class MarkerRequest(BaseModel):
    id: int = Field(..., ge=0, le=1023, description="ID do marcador ArUco (0-1024)")
    size: int = Field(35, ge=10, le=100, description="Tamanho do marcador em pixels")
    margin_size: int = Field(10, ge=0, le=100, description="Margem do marcador")
    border_bits: int = Field(1, ge=1, le=4, description="Bits da borda do marcador")

class MarkerResponse(BaseModel):
    id: int
    image_base64: str

class MarkerRowRequest(MarkerRequest):
    count: int = Query(10, ge=2, le=10, description="Número de marcadores na linha")


def create_app() -> FastAPI:
    app = FastAPI()

    def image_to_base64(img) -> str:
        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
        return img_str

    @app.get("/generate", response_model=MarkerResponse, summary="Gera um marcador ArUco", description="Gera um marcador ArUco com os parâmetros fornecidos.")
    def generate_marker_get(request: MarkerRequest = Depends()):
        try:
            generator = ArucoGenerator()
            img = generator.generate_single_marker(
                marker_id=request.id,
                size=request.size,
                margin_size=request.margin_size,
                border_bits=request.border_bits,
            )
            img_pil = Image.fromarray(img)
            img_base64 = image_to_base64(img_pil)
            return MarkerResponse(id=request.id, image_base64=img_base64)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erro ao gerar marcador: {str(e)}")

    @app.get("/generate_row", summary="Gera uma linha de marcadores ArUco", description="Gera uma linha de marcadores ArUco com os parâmetros fornecidos.")
    def generate_marker_row_get(request: MarkerRowRequest = Depends()):
        try:
            generator = ArucoGenerator()
            img = generator.generate_marker_row(
                marker_id=request.id,
                count=request.count,
                size=request.size,
                margin_size=request.margin_size,
                border_bits=request.border_bits,
            )
            img_pil = Image.fromarray(img)
            img_base64 = image_to_base64(img_pil)
            return {"id": request.id, "count": request.count, "image_base64": img_base64}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erro ao gerar linha de marcadores: {str(e)}")

    @app.get("/health", summary="Checagem de saúde da API", description="Retorna o status da API para checagem de saúde.")
    def health_check():
        return {"status": "ok"}

    @app.get("/", summary="Raiz da API", description="Mensagem de boas-vindas da API ArUco Generator.")
    def root():
        return {"message": "ArUco Generator API - Use /generate endpoint to get markers."}

    return app


app = create_app()
handler = Mangum(app)
