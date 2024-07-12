# Movie Recommender System

This project is a Movie Recommender System built using Streamlit. The application recommends movies based on the similarity to a selected movie and displays the recommended movie posters.

## Features

- Interactive user interface using Streamlit.
- Recommends top 5 movies similar to the selected movie.
- Fetches and displays movie posters for better visualization.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/movie-recommender-system.git
    cd movie-recommender-system
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Ensure you have the following files in the project directory:
    - `movie_dict.pkl`
    - `similarity.pkl`

## Usage

1. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

2. Open your web browser and navigate to `http://localhost:8501`.

3. Select a movie from the dropdown menu and click on "Show Recommendation" to see the recommended movies and their posters.

## Project Structure

- `app.py`: Main application file containing the Streamlit code.
- `movie_dict.pkl`: Pickle file containing the movie data.
- `similarity.pkl`: Pickle file containing the similarity matrix.
- `requirements.txt`: File containing the list of dependencies.

## API

This project uses the TMDb API to fetch movie posters. You need to have a TMDb API key to access the API.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any bugs or enhancements.

