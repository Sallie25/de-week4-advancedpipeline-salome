# Omnicart Pipeline

This project implements an advanced data pipeline with custom pagination and data enrichment.

## Pagination Strategy
The Omnicart API does not natively support query-based pagination (e.g., `?page=` or `?limit=`).  
To handle large datasets efficiently, a **manual pagination mechanism** was implemented within the `api_client.py` module.

### Custom Pagination Approach
Since the site’s API returns all data at once, we simulate pagination by:
- **Batch slicing:** Breaking the full dataset into smaller chunks (e.g., 100 records per batch) using list slicing or generators.  
- **Offset tracking:** Maintaining an index or offset counter (`start_index`, `end_index`) to mimic the behavior of a paginated API.  
- **Incremental fetching:** Iterating through these slices sequentially to process data in manageable portions — preventing memory overload and improving performance.  
- **Checkpointing (optional):** Storing the last processed index or timestamp to allow the pipeline to resume from where it stopped if interrupted.

This ensures efficient data ingestion and transformation even without native pagination support.

##  Data Enrichment Logic
The `data_enricher.py` module enhances raw API data with computed and standardized fields such as:

- **Derived metrics:** e.g., calculating total order value, average basket size, or delivery cost per order.  
- **Data normalization:** e.g., cleaning category names or standardizing date/time formats.  
- **Reference joining:** e.g., enriching transactions with product or regional metadata.  
- **Quality checks:** Ensuring each enriched record conforms to schema and business validation rules.

These steps produce cleaner, richer, and more reliable data for downstream analytics.

---

## Tools Used
| Tool / Library | Purpose |
|-----------------|----------|
| **Python 3.10+** | Core programming language |
| **requests** | API calls and data retrieval |
| **pandas** | Data manipulation and analysis |
| **json** | Configuration and schema management |
| **pytest** | Unit and integration testing |
| **logging** | Pipeline monitoring and error tracking |
| **Git & GitHub** | Version control and collaboration |

---

##  Project Structure
omnicart_pipeline/
├── pipeline/
│ ├── init.py
│ ├── config.py
│ ├── api_client.py
│ ├── data_enricher.py
│ ├── data_analyzer.py
│ └── pipeline.py
├── tests/
│ ├── init.py
│ └── ... (test files)
├── main.py
├── pipeline.cfg
├── requirements.txt
├── .gitignore
└── README.md


---

##  How to Run

```bash
#  Create and activate virtual environment
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows

#  Install dependencies
pip install -r requirements.txt

#  Run the main pipeline
python main.py

---

Author
Salome Akpan
Data Epic Intern
GitHub: @Sallie25

---