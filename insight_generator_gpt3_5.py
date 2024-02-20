import openai

# Set your OpenAI API key here
openai.api_key = "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"

def generate_insight(test_results):
    # Extract test results
    hba1c = test_results["Hba1c"]
    hdl = test_results["HDL"]
    ldl = test_results["LDL"]
    glucose = test_results["Fasting Glucose"]
    testosterone = test_results["Total Testosterone"]

    # Define prompt format for ChatGPT
    prompt = f"Customer's health test results:\nHbA1c: {hba1c}\nHDL: {hdl}\nLDL: {ldl}\nFasting Glucose: {glucose}\nTotal Testosterone: {testosterone}\nPlease provide short and concise health advice based on these results as a specialist doctor who understands everything about the tests and suggests what medication or supplements to take alonside with it. Output format should be like - Based on the results, that customer is prone to diabetes :"

    # Request completion from the API
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",  # Using ChatGPT-3.5 model
        prompt=prompt,
        max_tokens=500,  # Adjust the max_tokens parameter for desired length
        temperature=0.3,  # Adjust the temperature parameter for creativity
    )

    # Extract and return the generated insight from the response
    return response.choices[0].text.strip()


# Example usage
test_results = {
    "Hba1c": 7.5,
    "HDL": 70,
    "LDL": 120,
    "Fasting Glucose": 90,
    "Total Testosterone": 300
}

insight = generate_insight(test_results)
print("Generated Insight:", insight)

