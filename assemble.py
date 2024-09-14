from Data_Preparation import prep_data
from cohere_ext import generate_code_snippets, select_relevant_images
from dummy_data import DUMMY_DATA_SUMMARY
from groq_helper import helper
import os

# TODO change this to Databricks FileStore
# TODO Save the results back to Databricks FileStore


def assemble_content(path_to_pdf = "lecture_slides.pdf", lecture_summary = DUMMY_DATA_SUMMARY):
    df, slide_images = prep_data(path_to_pdf, lecture_summary) 
    try:
        captions = helper(slide_images)
        selected = select_relevant_images(captions, lecture_summary)
    finally:
        for img in slide_images:
            if img not in selected: 
                os.remove(img)
                del captions[img]
        return captions

assemble_content() # TODO change this to Databricks FileStore
