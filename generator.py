from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="Salesforce/codegen-350M-mono"
)

def generate_code(prompt):
    result = generator(
        prompt,
        max_length=80,
        num_return_sequences=1,
        do_sample=False
    )
    return result[0]["generated_text"]