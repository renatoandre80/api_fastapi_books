from pydantic import BaseModel, HttpUrl
from typing import List, Optional

class IndustryIdentifier(BaseModel):
    type: str
    identifier: str

class ImageLinks(BaseModel):
    smallThumbnail: Optional[HttpUrl] = None
    thumbnail: Optional[HttpUrl] = None

class VolumeInfo(BaseModel):
    title: str
    subtitle: Optional[str] = None
    authors: Optional[List[str]] = None
    publisher: Optional[str] = None
    description: Optional[str] = None
    industryIdentifiers: Optional[List[IndustryIdentifier]] = None
    pageCount: Optional[int] = None
    categories: Optional[List[str]] = None
    imageLinks: Optional[ImageLinks] = None
    language: Optional[str] = None

class SaleInfo(BaseModel):
    country: str
    saleability: str
    isEbook: bool

class AccessInfo(BaseModel):
    country: str
    viewability: str
    embeddable: bool
    publicDomain: bool
    textToSpeechPermission: str

class SearchInfo(BaseModel):
    textSnippet: Optional[str] = None

class Volume(BaseModel):
    kind: str
    id: str
    etag: str
    selfLink: HttpUrl
    volumeInfo: VolumeInfo
    saleInfo: SaleInfo
    accessInfo: AccessInfo
    searchInfo: Optional[SearchInfo] = None

class GoogleBooksResponse(BaseModel):
    kind: str
    totalItems: int
    items: List[Volume]