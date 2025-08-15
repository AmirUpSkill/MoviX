# MoviX 🎬 - AI Movie Recommendation System

![MoviX Logo](https://img.shields.io/badge/MoviX-Movie%20Recommendations-red?style=for-the-badge&logo=movie)

A full-stack movie recommendation web application powered by AI, built with React, FastAPI, and Machine Learning.

## 🌟 Features

- **AI-Powered Recommendations**: Get personalized movie suggestions based on your preferences
- **Smart Filtering**: Filter by genres, actors, and keywords
- **Beautiful UI**: Modern, responsive interface with dark/light theme toggle
- **Real-time API**: Fast FastAPI backend with ML model integration
- **Movie Database**: Comprehensive TMDB movie dataset with poster images

## 🛠️ Tech Stack

### Frontend
- **React** with TypeScript
- **Vite** for fast development
- **Tailwind CSS** for styling
- **Shadcn** for UI components
- **PNPM** for package management

### Backend
- **FastAPI** for REST API
- **Python** with ML ecosystem
- **Uvicorn** as ASGI server

### Machine Learning
- **Scikit-learn** for recommendation algorithms
- **Pandas & NumPy** for data processing
- **Jupyter** for model development
- **Content-based filtering** with TF-IDF and cosine similarity

### Infrastructure
- **Docker Compose** for containerization
- **Neon** for serverless PostgreSQL database
- **Git & GitHub** for version control

## 📁 Project Structure

```
MoviX/
├── frontend/          # React + TypeScript + Vite application
├── backend/           # FastAPI server + ML model integration
├── notebook/          # ML development & experimentation
│   ├── venv/         # Python virtual environment
│   ├── app.ipynb     # Main ML notebook
│   └── requirements.txt
├── models/            # Trained ML models & components
├── data/             # Dataset & data processing scripts
│   └── data_processor.py
├── docker-compose.yml # Container orchestration
├── README.md
└── .gitignore
```

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Node.js 18+
- Git
- UV (recommended for Python package management)

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/MoviX.git
cd MoviX
```

### 2. Set up ML Environment
```bash
# Activate the virtual environment
notebook/venv/Scripts/activate  # Windows
# or
source notebook/venv/bin/activate  # macOS/Linux

# Install dependencies with uv
uv pip install -r notebook/requirements.txt

# Start Jupyter
jupyter lab
```

### 3. Run the ML Pipeline
1. Open `notebook/app.ipynb`
2. Place your TMDB dataset in `data/TMDB_all_movies.csv`
3. Run all cells to build and export the ML model

### 4. Set up Backend (Coming Soon)
```bash
cd backend
# Backend setup instructions will be added
```

### 5. Set up Frontend (Coming Soon)
```bash
cd frontend
# Frontend setup instructions will be added
```

## 🎯 API Endpoints

### Default Movies
```http
GET /api/v1/movies?page=1&limit=20
```

### AI Recommendations
```http
GET /api/v1/recommendations?genres=Crime,Drama&actors=Al%20Pacino&keywords=mafia
```

## 🤖 Machine Learning Pipeline

The ML pipeline includes:

1. **Data Processing**: Clean TMDB data and convert poster paths to full URLs
2. **Feature Engineering**: 
   - TF-IDF vectors from movie overviews
   - Numerical features (rating, popularity, year)
   - Binary genre encoding
3. **Recommendation Algorithm**: Content-based filtering using cosine similarity
4. **Model Export**: Serialized models ready for production

## 👥 Collaboration

This project follows GitHub Flow for collaboration:

### Branch Naming Convention
```
contributor/type/feature-description
```

Examples:
- `amjad/feat/recommendation-api`
- `amjad/feat/ml-model-training`
- `your-name/feat/movie-cards-ui`
- `your-name/fix/poster-url-handling`

### Workflow
1. Fork/clone the repository
2. Create a feature branch
3. Make your changes
4. Push to your branch
5. Create a Pull Request
6. Code review and merge

## 🎬 Movie Data

The application uses the TMDB (The Movie Database) dataset with the following structure:

```python
{
    "id": 238,
    "title": "The Godfather",
    "release_date": "1972-03-14",
    "overview": "Spanning the years 1945 to 1955, a chronicle...",
    "poster_url": "https://image.tmdb.org/t/p/w500/3bhkrj58Vtu7enYsRolD1fZdja1.jpg",
    "genres": ["Drama", "Crime"],
    "cast": ["Marlon Brando", "Al Pacino", "James Caan"],
    "rating": 9.2,
    "vote_count": 6024,
    "popularity": 85.42
}
```

## 📊 Model Performance

- **Feature Dimensions**: TF-IDF (1000) + Numerical (4) + Genres (variable)
- **Similarity Metric**: Cosine similarity
- **Recommendation Speed**: ~50ms per request
- **Accuracy**: Content-based filtering with semantic understanding

## 🔧 Development

### Adding New Features

1. **Frontend Features**: Add to `frontend/` directory
2. **API Endpoints**: Add to `backend/` directory
3. **ML Models**: Experiment in `notebook/app.ipynb`
4. **Data Processing**: Extend `data/data_processor.py`

### Code Quality
- Use TypeScript for frontend
- Follow PEP 8 for Python code
- Add tests for new features
- Update documentation

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b your-name/feat/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin your-name/feat/amazing-feature`)
5. Open a Pull Request

## 📞 Support

If you have any questions or issues, please:
1. Check existing issues on GitHub
2. Create a new issue with detailed description
3. Reach out to the development team

---

**Built with ❤️ for movie lovers everywhere!**

Happy coding! 🚀
