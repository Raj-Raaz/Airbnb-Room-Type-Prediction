from pydantic import BaseModel, Field



class Features(BaseModel):
    latitude: float = Field(..., ge= -90, le=90, description = 'Latitude must be between -90 and 90')
    longitude: float = Field(..., ge= -180, le=180, description='Longitude must be between -180 and 180')
    price: float =Field(..., ge = 0, description='Price per neight, must be positive')
    minimum_nights: int = Field( ... , ge=1, le=365, description="Minimum nights required for booking")
    number_of_reviews: int = Field( ... , ge=0, description="Total number of reviews")
    reviews_per_month: float = Field( ... , ge=0, description="Average reviews per month")
    calculated_host_listings_count: int = Field(... , ge=0, description="Number of listings by this host")
    availability_365: int = Field( ... , ge=0, le=365, description="Days available out of 365")
    neighbourhood_group: str = Field( ... , min_length=1, description="Borough or neighbourhood group")
    neighbourhood: str = Field( ... , min_length=1, description="Specific neighbourhood name")
