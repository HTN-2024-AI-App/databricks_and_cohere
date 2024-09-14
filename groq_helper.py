from groq import Groq
import concurrent.futures
import base64
import cv2
from openai import OpenAI
import os

client = Groq()


def encode_image(image_array):
    _, buffer = cv2.imencode(".jpg", image_array)
    return base64.b64encode(buffer).decode("utf-8")

def generate_caption(image):
    completion = client.chat.completions.create(
        model="llava-v1.5-7b-4096-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Describe the image in one line."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image}",
                        }
                    }
                ]
            }
        ],
        temperature=0,
        max_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )

    return completion.choices[0].message.content

def helper(images):
    captions = {}
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {executor.submit(generate_caption, encode_image(cv2.imread(image))): image for image in images}
        for future in concurrent.futures.as_completed(futures):
            image = futures[future]
            captions[image] = future.result()
    return captions
