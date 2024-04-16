from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def scabies_diagnosis(symptoms):
    # Rule-based diagnosis
    common_symptoms = ['rash','skin burrows','intense itching','pimple-like rash between the fingers', 'pimple-like rash on the wrist',
                       'pimple-like rash on the elbows', 'pimple-like rash on the waist',
                       'pimple-like rash on the arpit area', 'pimple-like rash on the genital area',
                       'pimple-like rash on the buttocks', 'pimple-like rash on the knee',
                       'itching worsened by warmth', 'worsened itching at night', 'irritation', 'redness']

    if any(symptom in symptoms for symptom in common_symptoms):
        return "Likely scabies."
    else:
        return "Scabies is unlikely, but consult a doctor for further evaluation."

def atopic_dermatitis_diagnosis(symptoms):
    if 'redness' in symptoms and 'intense itching' in symptoms and 'irritation' in symptoms and len(symptoms) == 3:
        return True
    else:
        return False

def contact_dermatitis_diagnosis(symptoms):
    if 'rash' in symptoms and 'intense itching' in symptoms and 'irritation' in symptoms and len(symptoms) == 3:
        return True
    else:
        return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/diagnose', methods=['POST'])
def diagnose():
    symptoms_input = request.form.getlist('symptoms')
    if len(symptoms_input) < 3:
        return render_template('select_more_symptoms.html')
    elif contact_dermatitis_diagnosis(symptoms_input):
        symptom_image = 'contact_dermatitis_image.jpg'  # URL or path to the image
        return render_template('contact_dermatitis_result.html', diagnosis="Contact dermatitis", symptom_image=symptom_image)
    elif atopic_dermatitis_diagnosis(symptoms_input):
        return render_template('atopic_dermatitis_result.html', diagnosis="Atopic dermatitis")
    else:
        diagnosis = scabies_diagnosis(symptoms_input)
        if diagnosis == "Likely scabies.":
            symptom_images = {
                'pimple-like rash between the fingers': 'image_url1.jpg',
                'pimple-like rash on the wrist': 'image_url2.jpg',
                'rash': 'https://raw.githubusercontent.com/facebook-voting-system/rash/332a0fd59a572644c31e7e57d5bc842113922b9e/rash.png',
                'skin burrows': 'image_url2.jpg',
                'pimple-like rash on the elbows': 'image_url2.jpg',
                'pimple-like rash on the arpit area': 'image_url2.jpg',
                'pimple-like rash on the genital area': 'image_url2.jpg',
                'pimple-like rash on the buttocks': 'image_url2.jpg',
                'pimple-like rash on the knee': 'image_url2.jpg',
                'irritation': 'image_url2.jpg',
                'redness': 'image_url2.jpg',
                
            }
            return render_template('result.html', diagnosis=diagnosis, symptoms=symptoms_input, image_urls=symptom_images)
        else:
            return render_template('result.html', diagnosis=diagnosis)



if __name__ == '__main__':
    app.run(debug=True)
