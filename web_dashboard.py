from flask import Flask, render_template_string
from api import fetch_prices
from config import COINS, CURRENCY

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Crypto Dashboard</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #121212;
            color: #f1f1f1;
            padding: 20px;
        }
        h1 {
            color: #00ffc6;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            max-width: 500px;
        }
        th, td {
            border: 1px solid #444;
            padding: 10px;
            text-align: left;
        }
        th {
            background: #1e1e1e;
        }
        tr:nth-child(even) {
            background: #1a1a1a;
        }
    </style>
</head>
<body>
    <h1>🚀 Crypto Dashboard</h1>
    <table>
        <tr>
            <th>Coin</th>
            <th>Preis (EUR)</th>
        </tr>
        {% for coin, data in prices.items() %}
        <tr>
            <td>{{ coin.capitalize() }}</td>
            <td>{{ data["eur"] }} €</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""

@app.route("/")
def home():
    prices = fetch_prices(COINS, CURRENCY)
    if not prices:
        prices = {coin: "N/A" for coin in COINS}
    return render_template_string(TEMPLATE, prices=prices)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3997, debug=True)
