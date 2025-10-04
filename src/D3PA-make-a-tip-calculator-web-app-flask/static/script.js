// Simple Tip Calculator JavaScript
// By https://github.com/D3PA

document.getElementById('tipForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const formData = new FormData(this);
    
    try {
        const response = await fetch('/calculate', {
            method: 'POST',
            body: formData
        });
        
        const data = await response.json();
        
        if (data.error) {
            showError();
        } else {
            showResults(data);
        }
    } catch (error) {
        showError();
    }
});

function showResults(data) {
    document.getElementById('tipAmount').textContent = '$' + data.tip_amount;
    document.getElementById('tipPerPerson').textContent = '$' + data.tip_per_person;
    document.getElementById('totalAmount').textContent = '$' + data.total;
    document.getElementById('totalPerPerson').textContent = '$' + data.total_per_person;
    
    document.getElementById('results').classList.remove('hidden');
    document.getElementById('error').classList.add('hidden');
}

function showError() {
    document.getElementById('results').classList.add('hidden');
    document.getElementById('error').classList.remove('hidden');
}