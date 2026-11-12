
# Tourism Impact Analytics

> A data analysis and visualization pipeline for evaluating tourism traffic patterns, seasonal trends, environmental impacts ($CO_2$ emissions), and social media engagement drivers.
> 

## 📖 Table of Contents

- About The Project
- ✨ Key Features
- 🛠️ Built With
- 📁 Project Structure
- 🚀 Getting Started
    - Prerequisites
    - Installation
- 💻 Usage
- 📊 Visualizations & Insights
- 📄 License

---

## 🧐 About The Project

The **Tourism Impact Analytics** project provides a Python framework for processing and visualizing the correlation between visitor volume, social media activity, search engine interest, and environmental factors.

By analyzing data across TikTok views, Instagram activity, Google search trends, seasonal traffic, and $CO_2$ levels, this tool helps uncover key drivers behind tourism peaks and their broader environmental effects.

---

## ✨ Key Features

- **Automated Data Pipeline**: Ingests traffic datasets, social media logs, and environmental data.
- **KPI Metrics Generator**: Computes core performance indicators for visitor volume and impact metrics.
- **Seasonal Traffic Breakdown**: Compares total visitors across Summer, Autumn, Spring, and Winter.
- **Social Media Impact Analysis**: Analyzes visitor correlation against TikTok views, Instagram engagement, and Google search trends.
- **Environmental Impact Tracking**: Visualizes the relationship between visitor traffic peaks and $CO_2$ emissions.
- **Correlation Heatmaps**: Maps feature relationships across all numeric variables in the dataset.

---

## 🛠️ Built With

- **Python 3**
- **Pandas** – Data loading and manipulation
- **NumPy** – Numerical operations
- **Matplotlib** – Core plotting framework
- **Seaborn** – Statistical data visualizations

---

## 📁 Project Structure

```
Tourism-Analytics-Project/
│
├── data/
│   ├── Tourism_Impact_Analytics_Dataset.csv
│   ├── social_media_activity.csv
│   └── tourism_traffic.csv
│
├── src/
│   ├── data_loader.py        # Loads and prepares datasets
│   ├── analysis.py           # Calculates and outputs KPIs
│   └── visualizations.py     # Contains charting routines
│
├── main.py                   # Main entry point to run pipeline
├── requirements.txt          # Python packages list
└── README.md                 # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

- Python **3.8+** installed on your system.

### Installation

1. **Clone the repository**
    
    ```bash
    git clone https://github.com/your-username/Tourism-Analytics-Project.git
    cd Tourism-Analytics-Project
    ```
    
2. **Install dependencies**
    
    ```bash
    pip install -r requirements.txt
    ```
    

---

## 💻 Usage

Execute `main.py` to run the data loader, output key statistics to the console, and render all visualization charts:

```bash
python main.py
```

---

## 📊 Visualizations & Insights

The pipeline executes the following visualization functions from `src/visualizations.py`:

| Chart Routine | Type | Description |
| --- | --- | --- |
| `line_chart(df)` | Line Plot | Displays visitor trends and traffic changes over time. |
| `bar_chart(df)` | Bar Chart | Summarizes total visitors grouped by season (Summer, Autumn, Spring, Winter). |
| `heatmap(df)` | Correlation Heatmap | Evaluates correlation metrics across social activity, traffic, and environmental metrics. |
| `scatter_tiktok(df)` | Scatter Plot | Plots TikTok Views (in millions) vs. total visitor count per season. |
| `scatter_instagram(df)` | Scatter Plot | Measures Instagram engagement levels against visitor volume. |
| `scatter_google(df)` | Scatter Plot | Visualizes search interest vs. actual arrival counts. |
| `combo_co2(df)` | Combination Chart | Explores the connection between visitor density and $CO_2$ emissions. |

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
