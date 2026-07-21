# 📄 AI Document Summarizer

An AI-powered document summarization application built with **Python**, **Streamlit**, and **Groq LLM**. Upload PDF or TXT documents and instantly generate concise, accurate summaries using state-of-the-art large language models.

---

## 🚀 Features

- 📂 Upload PDF and TXT files
- 📖 Automatic text extraction
- 🤖 AI-powered document summarization
- 📝 Multiple summary modes
  - Short
  - Medium
  - Detailed
- 📄 View original document text
- 📋 View AI-generated summary
- ⬇️ Download summary as a TXT file
- 🎨 Clean and responsive Streamlit interface

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| Streamlit | User Interface |
| Groq API | Large Language Model |
| Llama 3.3 70B | AI Summarization |
| PyPDF2 | PDF Text Extraction |
| python-dotenv | Environment Variable Management |

---

## 📁 Project Structure

```text
AI-Document-Summarizer/
│
├── app.py
├── summarizer.py
├── pdf_reader.py
├── requirements.txt
├── .env.example
├── README.md
└── assets/
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/your-username/AI-Document-Summarizer.git
```

```bash
cd AI-Document-Summarizer
```

### Create a virtual environment

**Windows**

```bash
python -m venv venv
```

Activate it

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

or

```bash
python -m streamlit run app.py
```

---

## 📸 Screenshots

Add screenshots here after running the project.

Example:

```
assets/home.png

assets/result.png
```

---

## 📚 How It Works

1. Upload a PDF or TXT document.
2. The application extracts the document text.
3. Select the desired summary length.
4. Click **Generate Summary**.
5. The Groq LLM processes the document.
6. The generated summary is displayed.
7. Download the summary as a text file.

---

## 📌 Example Use Cases

- Research Paper Summarization
- Student Notes
- Meeting Minutes
- Business Reports
- Technical Documentation
- Articles and Blogs
- Study Material
- Project Documentation

---

## 🔮 Future Enhancements

- Multiple document support
- DOCX file support
- AI-generated keywords
- Reading time estimation
- Export summary as PDF
- Multilingual summarization
- Voice summary generation
- Semantic search over uploaded documents
- Chat with uploaded documents (RAG)

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new feature branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**K Katta Sai Swaroop**

- GitHub: https://github.com/saiswaroop66
- LinkedIn: *(Add your LinkedIn profile URL)*

---

⭐ If you found this project useful, please consider giving it a **Star** on GitHub!
