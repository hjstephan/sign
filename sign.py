import pymupdf


def cm_to_pt(cm):
    """Converts centimeters to PDF points."""
    return cm * (72 / 2.54)

def place_image_exact(input_pdf, output_pdf, image_path, page_num, x_cm, y_cm, width_cm):
    doc = pymupdf.open(input_pdf)
    
    # Check if page exists
    if page_num >= len(doc):
        print(f"Error: Document only has {len(doc)} pages.")
        return

    page = doc[page_num]
    
    # Convert CM to Points
    x = cm_to_pt(x_cm)
    y = cm_to_pt(y_cm)
    width = cm_to_pt(width_cm)
    
    # Calculate height automatically to preserve aspect ratio
    # We open the image briefly to get its dimensions
    img = pymupdf.Pixmap(image_path)
    aspect_ratio = img.height / img.width
    height = width * aspect_ratio
    
    # Define placement (x0, y0, x1, y1)
    rect = pymupdf.Rect(x, y, x + width, y + height)
    
    # Insert image
    page.insert_image(rect, filename=image_path)
    
    doc.save(output_pdf)
    doc.close()
    print(f"Done! Image placed on page {page_num + 1} at {x_cm}cm, {y_cm}cm.")

# --- Settings ---
# Note: page_num 0 is Page 1, page_num 1 is Page 2, etc.
place_image_exact(
    input_pdf="Lebenslauf.pdf",
    output_pdf="Lebenslauf-sign.pdf",
    image_path="Unterschrift.png",
    page_num=2,      # This targets the THIRD page
    x_cm=1.5,        # 15 cm from the left
    y_cm=23.6,       # 25 cm from the top
    width_cm=3.5     # Image width of 4.5 cm
)
