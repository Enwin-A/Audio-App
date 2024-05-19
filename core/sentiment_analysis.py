"""
This module contains the main functions for processing transcription and generating response.
"""
from langchain.llms import OpenAI  
import spacy
import en_core_web_sm
import PyPDF2  

# Replace with your OpenAI API key
openai_api_key = "key"
model_name = "gpt-3.5-turbo-0125"  # Choose appropriate model (consider limitations)

llm = OpenAI(
    api_key=openai_api_key,
    model_name=model_name
)
# nlp = spacy.load("en_core_web_sm")
nlp = en_core_web_sm.load()
conversation_context = {}

def generate_response(llm_model, prompt):
    response = llm_model.generate(
        prompts=prompt,
        max_tokens=1024,  # Adjust maximum response length as needed
        n=1,
        stop=None,
        temperature=0.7  # Controls response randomness (0 - deterministic, 1 - random)
    )
    return response #.text.strip()



def main(transcript):
    # with open("core/output_transcript.txt", 'r') as file:
    #     text = file.read()
    user_question = """Based on this give me the sentiment analysis of the conversation. 
    and also analyze the conversation from the point of view of a psychologist and give me the Psychological analysis and Behavioral analysis of the conversation based 
    on the speakers and explain what the conversation is based on the speakers context.
    also from an output formating give me responses as technically formatted as possible.
    use the example below for reference of the structure of expected output.

    response: [Speaker_0] is helpful and friendly in assisting [Speaker_1] with updating payment information, showing a positive sentiment in the conversation.

    Psychological analysis:
    - [Speaker_0] displays empathy and attentiveness by verifying [Speaker_1]'s information and addressing their request promptly.
    - [Speaker_1] seems organized and prepared, providing accurate details and answering security questions confidently.
    - The conversation is transactional and focused on resolving the payment issue efficiently.

    Behavioral analysis:
    - [Speaker_0] demonstrates a customer service-oriented approach by guiding [Speaker_1] through the process and ensuring all necessary information is obtained.
    - [Speaker_1] appears cooperative and responsive, following instructions and providing the required payment details without hesitation.
    - The interaction between the speakers is professional and goal-oriented, with both parties working towards a common objective of updating payment information.

    """
    prompt = f"Here is a transcript of an exmaple audio clip: {transcript}. {user_question}"
    prompt = [prompt]
    response = generate_response(llm, prompt)
    response = response.generations[0]
    response = response[0].text 
    # response = response[0]
    print(response)
    return response
    print(f"{response}") #.text.strip()}")


if __name__ == "__main__":

    main()