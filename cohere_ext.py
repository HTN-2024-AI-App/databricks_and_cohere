import cohere
co = cohere.Client('')

def generate_code_snippets(text):
    response = co.generate(
        model='command-nightly',
        prompt=f"Based on the following lecture content, generate relevant code snippets that will help reader understand the content in explained in the lecture content as given:\n{text}. If possible, provide code snippets in Python. ONLY OUTPUT THE CODE in markdown formating. If not possible to provide code snippets, return ' '.",
        max_tokens=500,
        temperature=0.7
    )
    return response.generations[0].text

def select_relevant_images(text, image_count):
    response = co.generate(
        model='command-nightly',
        prompt=f"Given the following lecture content, describe {image_count} relevant images that should be included:\n{text}",
        max_tokens=200,
        temperature=0.7
    )
    print(response)
    return response.generations[0].text.split('\n')