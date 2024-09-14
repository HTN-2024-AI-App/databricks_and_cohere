from pyspark.sql import SparkSession
import fitz  # pip install PyMuPDF

spark = SparkSession.builder.appName("LectureSummaryEnhancement").getOrCreate()

def extract_text_and_images(pdf_path):
    doc = fitz.open(pdf_path)
    text_content = []
    images = {}
    paths = []
    for page in doc:
        text_content.append(page.get_text())
        for img in page.get_images(full=True):
            xref = img[0]
            base_image = doc.extract_image(xref)
            images[xref] = base_image["image"]

    for key in images.keys():
        # save the image
        with open(f"image_{key}.png", "wb") as img_file:
            img_file.write(images[key])
            paths.append(f"image_{key}.png")
    return "\n".join(text_content), paths

def prep_data(pdf_path, lecture_summary):
    slide_text, slide_images = extract_text_and_images(pdf_path)
    df = spark.createDataFrame([(lecture_summary, slide_text, slide_images)], ["summary", "slide_content", "slide_images"])
    return df, slide_images