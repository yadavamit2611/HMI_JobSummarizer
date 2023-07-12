import Categorisation
from flask import Flask, render_template, request
import requests
app = Flask(__name__)

@app.route('/')
def index():
    images2 = {
        "Government Public Admin": "govtPublicAdmin.jpg",
        "Engineering": "Engineering.jpg",
        "Manufacturing": "Manufacturing.jpg",
        "Retail": "retail.jpg",
        "Real Estate": "RealEstate.jpg",
        "Law Enforcement": "Law Enforcement.jpg",
        "Information Technology": "IT.jpg",
        "Hospitality Tourism": "Hospitality.jpg",
        "Healthcare": "Healthcare.jpg",
        "Financial": "Financial.jpg",
        "Telecommunication": "Telecommunications.jpg",
        "Automotive": "Automotive.jpg",
        "Transportation Logistics": "Logistics.jpg",
        "Media": "media.jpg",
        "Education": "Education.jpg",
        "Fashion": "Fashion.jpg",
        "Food and Beverages": "Food.jpg",
        "Construction": "Construction.jpg",
        "Sports & Fitness": "Sports.png",
        "Consulting": "Consulting.jpg",
        "Agriculture": "Agriculture.jpg"
    }
    return render_template('index.html', sectors=Categorisation.sectorData, images=images2)


@app.route('/sector/<int:sector_id>')
def sector(sector_id):
    sector = Categorisation.sectorData[sector_id]
    jobs = sector['jobs']
    return render_template('sector.html', sector=sector, jobs=jobs)

@app.route('/jsb')
def jsb():
    return render_template('JobSearchBeta.html')

@app.route('/search', methods=['GET'])
def search():
    keyword = request.args.get('keyword')
    if keyword:
        uri = "https://ec.europa.eu/esco/api/search?language=en&type=skill&text="
        keyword = keyword.replace(" ", "+")
        response = requests.get(uri + keyword)
        if response.status_code == 200:
            try:
                data = response.json()
                titles = [result['title'] for result in data['_embedded']['results']]
                return render_template('results.html', titles=titles)
            except ValueError:
                return "Error: Invalid response from the API."
        else:
            return f"Error: {response.status_code} - Failed to fetch data from the API."
    else:
        return ""

if __name__ == '__main__':
    app.run()
