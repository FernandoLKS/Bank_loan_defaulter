const form = document.getElementById('predictForm');
const output = document.getElementById('output');

form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const data = {
        Age: Number(document.getElementById('Age').value),
        Income: Number(document.getElementById('Income').value),
        Family: Number(document.getElementById('Family').value),
        CCAvg: Number(document.getElementById('CCAvg').value),
        Education: Number(document.getElementById('Education').value),
        Mortgage: Number(document.getElementById('Mortgage').value),
        SecuritiesAccount: Number(document.getElementById('Securities').value),
        CDAccount: Number(document.getElementById('CD').value),
        Online: Number(document.getElementById('Online').value),
        CreditCard: Number(document.getElementById('CreditCard').value)
    };

    try {
        const response = await fetch('http://127.0.0.1:8000/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (result.propicio) {
            output.innerText = "Propício ✅";
            output.style.color = "green";
        } else {
            output.innerText = "Não Propício ❌";
            output.style.color = "red";
        }
    } catch (error) {
        output.innerText = "Erro na predição.";
        output.style.color = "orange";
        console.error(error);
    }
});
