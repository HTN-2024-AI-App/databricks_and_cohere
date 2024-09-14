from Data_Preparation import prep_data
from cohere_ext import call_cohere, generate_code_snippets
from dummy_data import DUMMY_DATA_SUMMARY

def assemble_content(row):
    content = f"Lecture Summary:\n{row.summary}\n\n"
    content += f"Code Snippets:\n{row.code_snippets}\n\n"
    content += f"Relevant Images:\n{row.image_descriptions}"
    return content


print(generate_code_snippets(DUMMY_DATA_SUMMARY))

# TODO change this to Databricks FileStore
# df, slide_images = prep_data("lecture_slides.pdf", DUMMY_DATA_SUMMARY)
# df = call_cohere(df, slide_images)

# df = df.withColumn("final_content", assemble_content(df))

# # TODO Save the results back to Databricks FileStore
# output_path = "enhanced_lecture_summary.txt"
# df.select("final_content").write.text(output_path)

# # Save images
# for i, img in enumerate(slide_images):
#     with open(f"lecture_image_{i}.png", "wb") as f:
#         f.write(img)

# print(df)