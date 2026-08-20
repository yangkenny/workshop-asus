from typing import Annotated

from fastapi import APIRouter, HTTPException, Path, status

from app.models import Product, ProductPage
from app.repository import get_product, list_products

router = APIRouter(prefix="/products", tags=["products"])


@router.get("")
def read_products() -> ProductPage:
    products = list_products()
    return ProductPage(
        items=products,
        total=len(products),
        page=1,
        page_size=20,
    )


@router.get("/{product_id}")
def read_product(product_id: Annotated[int, Path(gt=0)]) -> Product:
    product = get_product(product_id)
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )
    return product
