from typing import Optional, List, Dict

from pydantic import Field, BaseModel


class ProductBase(BaseModel):
	product_title: str = ""
	# product_url: str = ""
	# product_main_image_url: str = ""
	product_description: str = ""
	product_type: str = ""
	# product_sku: str = ""
	# google_product_category_id: str = ""
	# facebook_product_category_id: str = ""
	brand: str = ""
	product_id_in_platform: str = ""


class ShopifyProductModel(BaseModel):
	id: int = Field(...)
	title: str = Field(...)
	body_html: str = Field(...)
	vendor: str = Field(...)
	product_type: str = Field(...)
	created_at: str = Field(...)
	handle: str = Field(...)
	updated_at: str = Field(...)
	published_at: str = Field(...)
	template_suffix: str = Field(...)
	status: str = Field(...)
	published_scope: str = Field(...)
	tags: str = Field(...)
	admin_graphql_api_id: str = Field(...)


class VariantBase(BaseModel):
	variant_title: str = ""
	# condition: str = ""
	# variant_url: str = ""
	# variant_main_image_url: str = ""
	# variant_description: str = ""
	# short_description: str = ""
	item_group_id: str = ""
	variant_id_in_platform: str = ""
	variant_sku: str = ""
	availability: int = 1
	# tags: List[str] = []
	# colour: Optional[str] = ""
	# size: Optional[str] = ""
	# material: Optional[str] = ""
	barcode: Optional[str] = ""
	inventory_quantity: int = 0
	price: float = 0.0
	compare_at_price: float = 0.0
# additional_images: List[str] = []
# custom_properties: Dict = {}


class ShopifyVariantModel(BaseModel):
	id: str = Field(...)
	title: str = Field(...)
	price: str = Field(...)
	sku: str = Field(...)
	position: str = Field(...)
	inventory_policy: str = Field(...)
	compare_at_price: str = Field(...)
	fulfillment_service: str = Field(...)
	inventory_management: str = Field(...)
	option1: str = Field(...)
	option2: str = Field(...)
	option3: str = Field(...)
	created_at: str = Field(...)
	updated_at: str = Field(...)
	taxable: str = Field(...)
	barcode: str = Field(...)
	grams: str = Field(...)
	image_id: str = Field(...)
	weight: str = Field(...)
	weight_unit: str = Field(...)
	inventory_item_id: str = Field(...)
	inventory_quantity: str = Field(...)
	old_inventory_quantity: str = Field(...)
	requires_shipping: str = Field(...)
	admin_graphql_api_id: str = Field(...)


mapping = {
	"product": [
		{
			"db_key": "product_title",
			"external_platform_key": "title",
			"type": "string",
			"disabled": True,
		},
		{
			"db_key": "product_description",
			"external_platform_key": "body_html",
			"type": "string",
			"disabled": False,
		},
		{
			"db_key": "product_type",
			"external_platform_key": "product_type",
			"type": "string",
			"disabled": False,
		},
		{
			"db_key": "brand",
			"external_platform_key": "vendor",
			"type": "string",
			"disabled": False,
		},
		{
			"db_key": "product_id_in_platform",
			"external_platform_key": "admin_graphql_api_id",
			"type": "string",
			"disabled": False,
		},
	],
	"variant": [
		{
			"db_key": "item_group_id",
			"external_platform_key": "id",
			"type": "string",
			"disabled": False,
		},
		{
			"db_key": "variant_id_in_platform",
			"external_platform_key": "inventory_item_id",
			"type": "string",
			"disabled": False,
		},
		{
			"db_key": "variant_sku",
			"external_platform_key": "sku",
			"type": "string",
			"disabled": False,
		},
		{
			"db_key": "availability",
			"external_platform_key": "inventory_quantity",
			"type": "string",
			"disabled": False,
		},
		{
			"db_key": "barcode",
			"external_platform_key": "barcode",
			"type": "string",
			"disabled": True,
		},
		{
			"db_key": "inventory_quantity",
			"external_platform_key": "inventory_quantity",
			"type": "string",
			"disabled": False,
		},
		{
			"db_key": "price",
			"external_platform_key": "price",
			"type": "string",
			"disabled": False,
		},
		{
			"db_key": "compare_at_price",
			"external_platform_key": "compare_at_price",
			"type": "string",
			"disabled": False,
		},
	]
}
