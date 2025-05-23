# YouTube Trending Videos Pipeline

## Overview
This project builds an automated data pipeline to extract, store, process, and visualize trending YouTube videos data. It fetches daily trending video data using the YouTube Data API v3, stores it in a PostgreSQL database, processes it with Pandas, and visualizes insights using Streamlit. The pipeline is scheduled using cron jobs for automation, making it a lightweight, cost-free solution for tracking YouTube trends.

### Goals
- Extract daily trending YouTube videos (titles, views, likes, categories, etc.).
- Store and manage data in a structured PostgreSQL database.
- Clean and transform data for analysis.
- Automate the pipeline for daily updates.
- Visualize trends via an interactive dashboard.
- Create a portfolio-worthy project with clear documentation.

### Tools Used
- **Python**: Core scripting language.
- **YouTube Data API v3**: Data source for trending videos (free with Google Cloud account).
- **PostgreSQL**: Relational database for data storage.
- **Pandas**: Data cleaning and transformation.
- **Streamlit**: Interactive dashboard for visualization.
- **Cron Jobs**: Scheduling daily pipeline runs.
- **Google Colab / Local Machine**: Development environment.

## Project Structure
```
youtube-trending-pipeline/
├── scripts/
│   ├── youtube_data_ingestion.py        # Fetches data from YouTube API
│   ├── postgres_setup.py      # Loads data into PostgreSQL
│   ├── data-cleaning-transform.py        # Cleans and enriches data
│   ├── dashboard.py        # Streamlit dashboard
│   ├── run_pipeline.sh         # Bash script for cron scheduling
├── dataset/                # Generated Dataset
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
```

## Setup Instructions

### Prerequisites
- Python 3.8+
- Google Cloud account with YouTube Data API v3 enabled
- PostgreSQL installed locally or hosted (e.g., free tier on services like Heroku or Supabase)
- Git

### Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/youtube-trending-pipeline.git
   cd youtube-trending-pipeline
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   *Note*: Ensure `psycopg2` or `psycopg2-binary` is included in `requirements.txt` for PostgreSQL connectivity.

3. **Set Up YouTube API**:
   - Create a Google Cloud project: [Google Cloud Console](https://console.cloud.google.com/).
   - Enable the YouTube Data API v3.
   - Generate an API key and store it securely in a `.env` file:
     ```env
     YOUTUBE_API_KEY=your-api-key-here
     ```

4. **Set Up PostgreSQL**:
   - Install PostgreSQL locally or use a hosted service.
   - Create a database (e.g., `youtube_trending`):
     ```bash
     psql -U postgres -c "CREATE DATABASE youtube_trending;"
     ```
   - Configure database credentials in a `.env` file:
     ```env
     DB_HOST=localhost
     DB_NAME=youtube_trending
     DB_USER=your-username
     DB_PASSWORD=your-password
     DB_PORT=5432
     ```
   - Run `postgres_setup.py` to create tables (`videos`, `categories`, `fetch_log`) and load data.

5. **Optional: Scheduling**:
   - Set up a cron job to run the pipeline daily:
     ```bash
     crontab -e
     ```
   - Add the following line to run `schedule.sh` daily at 1 AM:
     ```bash
     0 1 * * * /path/to/youtube-trending-pipeline/scripts/schedule.sh
     ```

## Usage
1. **Fetch Data**:
   - Run the ingestion script to fetch trending videos:
     ```bash
     python scripts/youtube_data_ingestion.py
     ```
   - Output: Raw data saved in `dataset/`.

2. **Load Data**:
   - Load raw data into the PostgreSQL database:
     ```bash
     python scripts/postgres_setup.py
     ```

3. **Transform Data**:
   - Clean and enrich data using Pandas:
     ```bash
     python scripts/data-cleaning-transform.py
     ```
   - Output: Processed data saved in `dataset/`.

4. **Visualize Data**:
   - Launch the Streamlit dashboard:
     ```bash
     streamlit run scripts/dashboard.py
     ```
   - View insights like top 10 trending videos, category trends, and view/like ratios.

5. **Automate Pipeline**:
   - Use `schedule.sh` to run all scripts sequentially:
     ```bash
     bash scripts/run_pipeline.sh
     ```

## Sample Output
- **Database**: PostgreSQL database `youtube_trending` contains tables (`videos`, `categories`, `fetch_log`) with structured data.
- **Visualizations**: Charts in show trends like:
  - Top 10 videos by views.
  - Trending categories over time.
  - View/like ratio analysis.
- **Dashboard**: Interactive Streamlit app at `http://localhost:8501` (default).

## Example Visualizations
![Top 10 Trending Videos](outputs/charts/top_videos.png)
![Category Trends](outputs/charts/category_trends.png)

## Future Improvements
- Add support for multiple regions using the `regionCode` API parameter.
- Implement error handling for API rate limits with exponential backoff.
- Enhance the dashboard with filters for date ranges or categories.
- Store historical trends for long-term analysis.

## Contributing
Feel free to fork this repository, submit issues, or create pull requests with improvements. Ensure to follow the coding style and include tests for new features.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For questions or feedback, reach out via [GitHub Issues](https://github.com/your-username/youtube-trending-pipeline/issues).