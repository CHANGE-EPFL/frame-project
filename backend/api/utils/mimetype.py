# verify extension/content-type is valid
pdf_mimetypes = [
    "application/acrobat", "application/pdf", "application/x-pdf", "text/pdf",
    "text/x-pdf"
]
png_mimetypes = ["image/png", "application/png", "application/x-png"]
jpg_mimetypes = [
    "image/jpg", "application/jpg", "application/x-jpg", "image/jpeg",
    "application/jpeg"
]
gif_mimetypes = ["image/gif"]
binary_mimetypes = ["application/octet-stream"]
text_mimetypes = ["text/plain", "text/csv"]
other_images: list[str] = ["image/bmp", "image/webp"]
image_mimetypes: list[str] = png_mimetypes + \
    jpg_mimetypes + gif_mimetypes + other_images
zip_mimetypes: list[str] = ["application/zip", "application/x-zip-compressed"]
