# 🚀 Flask Financial Data API

This Flask-based API provides historical financial data analysis and trend insights. The API supports caching for performance optimization and includes an interactive Swagger documentation interface.

---

## 📌 Features
- **Retrieve Historical Financial Data**
- **Analyze Trends** with percentage change and moving averages
- **Flask-Caching** to optimize performance
- **Swagger UI** (`/apidocs`) for interactive API documentation
- **Environment Variables Support** via `.env`
- **Logging** for debugging and monitoring

---

## 📖 Installation & Setup
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/Flask_Financial_API.git
cd Flask_Financial_API
```

### **2️⃣ Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate    # On Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Set Up Environment Variables**
Create a `.env` file in the project root and add:
```bash
FLASK_ENV=development
CACHE_TYPE=simple
CACHE_DEFAULT_TIMEOUT=300
```

### **5️⃣ Run the Flask App**
```bash
python app.py
```

---

## 📌 Endpoints

### **1️⃣ Retrieve Historical Data**
**URL:** `/data`
**Method:** `GET`

| Parameter | Type   | Default  | Description |
|-----------|--------|----------|-------------|
| `symbol`  | string | btc  | Asset ID (e.g., btc, eth) |
| `days`    | int    | 7        | Number of days of historical data |

**Example Request:**
```
GET /data?symbol=eth&days=10
```

**Response:**
```json
{
  "prices": [[1700000000000, 45000], [1700086400000, 45250]],
  "market_caps": [[1700000000000, 800000000000], [1700086400000, 810000000000]],
  "total_volumes": [[1700000000000, 35000000000], [1700086400000, 36000000000]]
}
```

### **2️⃣ Analyze Asset Trend**
**URL:** `/trend`
**Method:** `GET`

| Parameter | Type   | Default  | Description |
|-----------|--------|----------|-------------|
| `symbol`  | string | btc  | Asset ID |
| `days`    | int    | 7        | Number of days for analysis |

**Example Request:**
```
GET /trend?symbol=btc&days=10
```

**Response:**
```json
{
  "percent_change": -6.38,
  "trend": "Downtrend",
  "moving_average": 99959.49
}
```

---

## 📖 Documentation
After running the API, open your browser and go to:
```
http://127.0.0.1:5000/apidocs
```
This opens an **interactive Swagger UI** where you can test endpoints directly.

---

## 🚀 Future Improvements
- **📊 Volatility Analysis** (`/volatility`) to measure price swings.
- **📈 Exponential Moving Averages (EMA)** for better trend detection.
- **🛠 Rate Limiting** to prevent excessive API requests.
- **🔒 Authentication & API Keys** for secure access.

---

## 🤝 Contributing
1. Fork the repo.
2. Create a new branch (`feature-new`).
3. Commit changes and push to your branch.
4. Submit a Pull Request.

---

## 📜 License
This project is licensed under the MIT License.

---

## 💡 Questions or Issues?
Feel free to open an issue or reach out via [GitHub Issues](https://github.com/YOUR_GITHUB_USERNAME/Flask_Financial_API/issues). 🚀

