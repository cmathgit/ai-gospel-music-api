import json
import random
import getpass
import os
import controlflow as cf
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# GET GOOGLE API KEY
api_key = os.getenv("GOOGLE_API_KEY")

# Initialize Google Generative AI and configure transport as rest (suppresses gRPC logging output warnings)
genai.configure(api_key=api_key, transport='rest')

# Ensure your Google AI API key is configured
if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google AI API key: ")

# Get the model from the environment variable
model = os.getenv('MODEL_NAME')

# set the default model
cf.defaults.model = ChatGoogleGenerativeAI(
    model=model, 
    temperature=0.5,
)

controlflow_context = os.getenv('CONTROL_FLOW_CONTEXT_LYRICIST')

base_lib_file_path = 'datasets/'

def revise_prompt_with_control_flow_mnemonic(lyrics_prompt):
    lyrics_prompt_revised = cf.run(controlflow_context,
        context=dict(prompt=lyrics_prompt),
    )

    return lyrics_prompt_revised

def get_random_mnemonic_topic():
    with open(f'{base_lib_file_path}random_mnemonic_topics_dict.json') as f:
        random_mnemonic_topics = json.load(f)

    return random.choice(random_mnemonic_topics)

def generate_mnemonic_topic_prompt():
    mnemonic_topic = get_random_mnemonic_topic()
    # Generate text using the Gemini model(s)
    print(f"Generate a mnemonic topic based on the following topic: {mnemonic_topic}")
    prompt = f"Act as a genius in {mnemonic_topic}, write a brief summary for a student learning about {mnemonic_topic} in 2900 words or less while being as concise, efficient, and direct as possible."
    print(f"Prompt: {prompt}")

    # Get the model from the environment variable
    model = os.getenv('MODEL_NAME')
    llm = genai.GenerativeModel(model)
    llm_response = llm.generate_content(prompt)
    print("LLM Response:", llm_response.text)
    mnemonic_topic_prompt = llm_response.text
    revised_mnemonic_topic_prompt = revise_prompt_with_control_flow_mnemonic(mnemonic_topic_prompt)

    return mnemonic_topic, prompt, revised_mnemonic_topic_prompt, mnemonic_topic_prompt

# test the function
if __name__ == "__main__":

    #Topic Provided
    mnemonic_topic_10 = "Consider this analogy of Einstein's General Theory of Relativity. When you shoot a basket ball, you perceive an arc, but the ball is actually moving in a straight vector. You, the hoop, and the floor are moving up. The net rises to meet the basketball while the basketball moves in a straight line to the hoop. The general definition of straight and the contiguous line segments. The notion of distance between two points is ambiguous in curved space. By definition, a curve between two points is straight if the tangent vector at point A remains tangent as the vector is parallel transported to point B. Recall that two topological spaces X and Y are said to be topologically equivalent (or homeomorphic), if there exists a homeomorphism, continuous map between the spaces, H∈C(X,Y) which has a continuous inverse H−∈C(Y,X). Exploring Gravity, Relativity, and Spring Dynamics Through Einstein’s Analogies. Einstein’s theories of relativity revolutionized our understanding of gravity, motion, and spacetime. By combining thought experiments like the relativity of simultaneity in trains with realworld phenomena such as the behavior of a falling spring, we can illuminate the principles underlying these theories. This report synthesizes insights from Einstein’s analogies, spring dynamics, and geometric interpretations of gravity to explain why the bottom of a dropped spring remains stationary until the collapsing top reaches it. Einstein’s Train Analogy and the Equivalence Principle: Einstein’s trainandplatform thought experiment illustrates the relativity of simultaneity in special relativity. Observers in different inertial frames (e.g., on a moving train versus a stationary platform) disagree on whether spatially separated events occur simultaneously. While this experiment primarily addresses simultaneity, it also hints at the broader principle that motion and perspective shape physical reality.  The equivalence principle—a cornerstone of general relativity—extends this idea by equating gravitational effects with acceleration. Einstein posited that an observer in free fall (e.g., inside a plummeting elevator) experiences locally gravityfree conditions, akin to floating in deep space. Conversely, an accelerating observer in space perceives forces indistinguishable from gravity. This equivalence underpins the geometric interpretation of gravity as spacetime curvature."  

    revised_mnemonic_topic_10 = revise_prompt_with_control_flow_mnemonic(mnemonic_topic_10)
    print(f"Revised Mnemonic Topic Prompt in Song Form: {revised_mnemonic_topic_10}")

    # Generate a random mnemonic topic
    mnemonic_topic_11, prompt_11, revised_mnemonic_topic_prompt_11, mnemonic_topic_prompt_11 = generate_mnemonic_topic_prompt()
    print(f"Mnemonic Topic: {mnemonic_topic_11}")
    print(f"Prompt: {prompt_11}")
    print(f"Revised Mnemonic Topic Prompt: {revised_mnemonic_topic_prompt_11}")
    print(f"Mnemonic Topic Prompt: {mnemonic_topic_prompt_11}")