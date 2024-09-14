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
        select_relevant_images(helper(slide_images), lecture_summary)
    finally:
        for img in slide_images:
            os.remove(img)
    

assemble_content() # TODO change this to Databricks FileStore
