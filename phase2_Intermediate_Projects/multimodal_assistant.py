from PIL import Image
from utils.llama3_utils import query_llama3
from transformers import BlipProcessor, BlipForConditionalGeneration

# Load BLIP large model for better detection
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")

def analyze_image_and_answer(image: Image.Image, question: str):
    """Analyze image using BLIP-2 Large + LLaMA3 reasoning."""

    # BLIP captioning - safest call (no custom text here)
    inputs = processor(image, return_tensors="pt")
    output = model.generate(**inputs, max_new_tokens=100)
    caption = processor.decode(output[0], skip_special_tokens=True)

    # Debug: Ensure caption is captured
    if not caption.strip():
        caption = "An image of various objects."

    # Pass caption + question to LLaMA3
    prompt = f"""
Image description: {caption}
User question: {question}
Answer the question based on the image description.
"""
    return f"Caption: {caption}\n\n" + query_llama3(prompt)

