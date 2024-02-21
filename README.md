# Insight Generator - FeelValeo
## 

Insight Generator is a gpt3.5 API based implementation of test results for various types of health and medical tests.

## Example

> test_results = {
    "Hba1c": 7.5,
    "HDL": 70,
    "LDL": 120,
    "Fasting Glucose": 90,
    "Total Testosterone": 1200
}

> Generated Insight: Based on the results, the customer's HbA1c levels are slightly elevated, indicating a risk for diabetes. It is important for the customer to maintain a healthy diet and exercise regularly to help manage their blood sugar levels. Additionally, the customer's LDL levels are slightly high, which could increase their risk for heart disease. Incorporating more fruits, vegetables, and whole grains into their diet, as well as potentially taking a cholesterol-lowering medication, may help lower their LDL levels. The customer's high total testosterone levels could also be a sign of an underlying health issue, and it is recommended for them to consult with a doctor for further evaluation and potential treatment. Overall, maintaining a healthy lifestyle and seeking medical advice for any concerning results can help prevent future health issues.


Once we change one of the test results "Total Testosterone" to "300" from "1200", we could see an updated insight generated.


> test_results = {
    "Hba1c": 7.5,
    "HDL": 70,
    "LDL": 120,
    "Fasting Glucose": 90,
    "Total Testosterone": 300
}

> Generated Insight: Based on the results, the customer's HbA1c level is slightly elevated, indicating a risk for diabetes. It is important to maintain a healthy diet and exercise regularly to manage blood sugar levels. Additionally, the customer's LDL level is slightly high, which may increase the risk for heart disease. It is recommended to incorporate more fruits, vegetables, and whole grains into their diet and to limit saturated and trans fats. The customer's total testosterone level is low, which may lead to symptoms such as fatigue and decreased libido. It is advised to consult with a doctor about potential testosterone replacement therapy. Overall, a healthy lifestyle and regular check-ups are important for maintaining optimal health.


## Run the Code

Insight Generator requires Python3 installed to run.

Install the dependencies and run the code.

```sh
cd feelvaleo
pip3 install openai
python3 insight_generator.py
```
