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

def select_relevant_images(captions, lecture_summary):
    response = co.generate(
        model='command-nightly',
        prompt=f"Given the following lecture content, {lecture_summary}, and the following image captions, {captions}, select the most relevant images that will help the reader understand the content in the lecture. Only return the relevant image captions and discard the rest.",
        max_tokens=200,
        temperature=0.7
    )
    print(response)
    return response.generations[0].text.split('\n')