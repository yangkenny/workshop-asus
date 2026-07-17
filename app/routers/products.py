from typing import Literal

from fastapi import APIRouter, HTTPException, Query, status

from app.models import Product, ProductPage
from app.repository import get_product, search_products

router = APIRouter(prefix="/products", tags=["products"])


@router.get("", response_model=ProductPage)
def read_products(
    q: str | None = Query(None, description="Search query"),
    sort: str | None = Query(
        None, description="Field to sort by", pattern="^price$"
    ),
    order: Literal["asc", "desc"] = Query("asc", description="Sort order"),
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(20, ge=1, le=20, description="Items per page"),
) -> ProductPage:
    # Get filtered and sorted products
    products = search_products(query=q, sort_by=sort, order=order)
    
    # Calculate pagination
    total = len(products)
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    paginated_items = products[start_idx:end_idx]
    
    return ProductPage(
        items=paginated_items,
        total=total,
        page=page,
        page_size=page_size,
    )


@router.get("/{product_id}", response_model=Product)
def read_product(product_id: int) -> Product:
    product = get_product(product_id)
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )
    return product
