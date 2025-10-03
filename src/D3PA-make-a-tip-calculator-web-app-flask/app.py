"""
Tip Calculator Web App
By https://github.com/D3PA
"""

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        bill = float(request.form['bill_amount'])
        tip = float(request.form['tip_percentage'])
        people = int(request.form.get('people_count', 1))
        
        tip_amount = (bill * tip) / 100
        total = bill + tip_amount
        
        return jsonify({
            'tip_amount': round(tip_amount, 2),
            'total': round(total, 2),
            'tip_per_person': round(tip_amount / people, 2),
            'total_per_person': round(total / people, 2)
        })
    except:
        return jsonify({'error': 'Please enter valid numbers'})

if __name__ == '__main__':
    app.run(debug=True)