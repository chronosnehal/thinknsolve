# 🚀 ThinkNSolve

A comprehensive collection of **interview questions and solutions** for Python algorithms and GenAI problems. Each problem is designed as a complete, self-contained interview challenge with clear documentation, runnable code, and configurable LLM clients supporting OpenAI, Azure OpenAI, and OpenRouter.

**🎯 Purpose**: Sharpen your Python and AI skills through structured, time-bound challenges inspired by real interview and project scenarios.

**⏱️ Time Optimized**: All problems are carefully scoped to be solvable within **30-45 minutes maximum**, making them perfect for interview practice and focused learning sessions.

**🔧 Multi-LLM Support**: Unified interface for OpenAI, Azure OpenAI, and OpenRouter - switch providers seamlessly without code changes.

<!-- 
CRITICAL: DO NOT DELETE THE PROBLEMS CATALOG TABLE BELOW
This table must be preserved and only updated, never removed.
-->

## 📚 Problems Catalog

### 🤖 GenAI Problems
| Problem | Difficulty | Time | Key Concepts | Links |
|---------|------------|------|--------------|-------|
| Sentiment Analysis | Intermediate-Advanced | 30-45 min | Prompt Engineering, Batch Processing, JSON Output, Error Handling | [📝 Question](app/genai/sentiment_analysis/question_sentiment_analysis.md) \| [💻 Solution](app/genai/sentiment_analysis/sentiment_analysis.py) |
| Code Generation | Intermediate | 30-45 min | Code Generation, Code Review, Multi-language Support, Educational Explanations | [📝 Question](app/genai/code_generation/question_code_generation.md) \| [💻 Solution](app/genai/code_generation/code_generation.py) |
| Creative Writing | Intermediate | 20-30 min | Content Generation, Parameter Control, Style/Tone Adaptation, Multi-format Output | [📝 Question](app/genai/creative_writing/question_creative_writing.md) \| [💻 Solution](app/genai/creative_writing/creative_writing.py) |
| Data Analysis | Intermediate | 30-40 min | SQL Generation, Business Intelligence, Data Insights, Report Creation | [📝 Question](app/genai/data_analysis/question_data_analysis.md) \| [💻 Solution](app/genai/data_analysis/data_analysis.py) |
| Question Answering | Intermediate | 30-40 min | Context Handling, Information Extraction, Fact-checking, Quiz Generation | [📝 Question](app/genai/question_answering/question_question_answering.md) \| [��� Solution](app/genai/question_answering/question_answering.py) |
| Text Summarizer | Beginner-Intermediate | 20-30 min | Text Summarization, Content Compression, Variable Length Output, Executive Summaries | [📝 Question](app/genai/text_summarizer/question_text_summarizer.md) \| [💻 Solution](app/genai/text_summarizer/text_summarizer.py) |

### 🐍 Python Problems  
| Problem | Difficulty | Time | Key Concepts | Links |
|---------|------------|------|--------------|-------|
| Binary Search | Intermediate | 30-45 min | Search Algorithms, Array Manipulation, Time Complexity, Edge Cases, Algorithm Variations | [📝 Question](app/python/binary_search/question_binary_search.md) \| [💻 Solution](app/python/binary_search/binary_search.py) |
| Web Scraper | Intermediate | 30-40 min | HTTP Requests, API Integration, JSON Parsing, HTML Scraping, Error Handling, Retry Logic | [📝 Question](app/python/web_scraper/question_web_scraper.md) \| [💻 Solution](app/python/web_scraper/web_scraper.py) |
| Data Analysis | Intermediate | 35-45 min | Pandas Operations, Data Cleaning, Aggregations, Pivot Tables, Data Merging, Business Intelligence | [📝 Question](app/python/data_analysis/question_data_analysis.md) \| [💻 Solution](app/python/data_analysis/data_analysis.py) |
| ML Training | Intermediate | 35-45 min | Scikit-learn, Model Training, Feature Engineering, Cross-validation, Model Evaluation, Classification Algorithms | [📝 Question](app/python/ml_training/question_ml_training.md) \| [💻 Solution](app/python/ml_training/ml_training.py) |

<!-- END OF PROTECTED PROBLEMS CATALOG TABLE -->

## 🏗️ Project Structure

The repository follows a strict structure optimized for interview preparation:

```
thinknsolve/
├── README.md                  # Project documentation
├── requirements.in            # Core dependency specifications  
├── requirements.txt           # Locked dependencies with exact versions
├── LICENSE                    # Project license
├── app/
│   ├── datasets/              # Real-world datasets for analysis problems
│   ├── genai/                 # GenAI Problems
│   │   ├── sentiment_analysis/
│   │   ├── code_generation/ 
│   │   ├── creative_writing/
│   │   ├── data_analysis/
│   │   ├── question_answering/
│   │   └── text_summarizer/
│   ├── python/                # Python Problems
│   │   ├── binary_search/
│   │   ├── web_scraper/
│   │   ├── data_analysis/
│   │   └── ml_training/
│   └── utils/
│       └── config.py          # Multi-provider LLM client configuration
```

### File Structure Rules
Each problem follows a **mandatory 2-file structure**:
- `question_<problem>.md` - Complete problem statement with examiner guide
- `<problem>.py` - Runnable solution implementation with examples

### Naming Conventions
- **Directory names**: Maximum 2 words, snake_case (e.g., `text_summarizer`, `binary_search`)
- **File names**: Follow template patterns exactly
- **Problem classification**: Clear separation between GenAI and Python problems

## ⚡ Quick Start

### Prerequisites
- **Python 3.8+** (tested with Python 3.12.11)
- Virtual environment recommended

```bash
# Check Python version
python3 --version

# Create virtual environment (recommended)
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Environment Setup
Create a `.env` file in the root directory with your API keys:

```bash
# Required for GenAI problems
# Choose one or more providers:

# OpenRouter (Recommended - access to multiple models)
OPENROUTER_API_KEY=your_openrouter_api_key_here
OPENROUTER_MODEL=google/gemma-2-9b-it:free

# OpenAI (Direct access to GPT models)
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-3.5-turbo

# Azure OpenAI (Enterprise deployment)
AZURE_OPENAI_API_KEY=your_azure_key_here
AZURE_OPENAI_ENDPOINT=your_azure_endpoint_here
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-35-turbo
AZURE_OPENAI_API_VERSION=2024-02-15-preview

# Set default provider (optional)
DEFAULT_LLM_PROVIDER=openrouter
```

### Running Examples

**Run any problem using Python module syntax:**
```bash
# GenAI Problems (require API keys)
python3 -m app.genai.<problem_name>.<problem_name>

# Python Problems (no API keys needed)  
python3 -m app.python.<problem_name>.<problem_name>
```

**Examples:**
```bash
# Try a GenAI problem
python3 -m app.genai.sentiment_analysis.sentiment_analysis

# Try a Python problem
python3 -m app.python.ml_training.ml_training
```

**Test Your Setup:**
```bash
# Verify imports and configuration
python3 -c "from app.utils.config import ExampleConfig; print('✅ Setup complete!')"
```

## ⚙️ Multi-LLM Configuration

The project provides a **unified interface** for multiple LLM providers:

### Supported Providers
1. **OpenRouter** (default) - Access to 100+ models through one API
2. **OpenAI** - Direct access to GPT-3.5, GPT-4, and newer models  
3. **Azure OpenAI** - Enterprise deployment with enhanced security

### Usage Examples
```python
from app.utils.config import ExampleConfig

# Use default provider (OpenRouter)
client = ExampleConfig.create_client("openrouter")

# Switch providers easily
openai_client = ExampleConfig.create_client("openai")
azure_client = ExampleConfig.create_client("azure")

# All clients use the same interface
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
]
response = client.chat(messages)
```

### Provider Configuration
Each provider is automatically configured from environment variables:
- **Graceful fallbacks** if packages aren't installed
- **Clear error messages** for missing API keys
- **Consistent interface** across all providers

## ⏱️ Time Management & Interview Focus

### Design Philosophy
Every problem is meticulously designed for **realistic interview scenarios**:

- **30-minute problems** (preferred): Core functionality with basic testing
- **45-minute problems** (maximum): Comprehensive implementation with edge cases
- **Never exceed 50 minutes**: Includes reading, planning, coding, and testing

### Problem Scope Guidelines
- **Start Simple**: Core functionality first, enhancements if time permits
- **Clear Requirements**: Exactly what must be implemented vs. nice-to-have
- **Modular Design**: Independent functions for incremental development
- **Realistic Complexity**: Achievable within time constraints

### Time Breakdown Example (30-min problem)
- **5 minutes**: Read and understand requirements
- **5 minutes**: Plan approach and identify key functions
- **15 minutes**: Core implementation
- **5 minutes**: Testing and validation

## 🎯 For Interviewers & Educators

### Complete Interview Package
Each problem provides everything needed for a professional interview:

- **📋 Problem Statement**: Clear, realistic requirements
- **🎯 Examiner Guide**: Difficulty level, timing, key concepts being tested
- **💡 Hints**: Strategic guidance if candidates need help
- **📝 Solution Approach**: Step-by-step implementation plan
- **✅ Example I/O**: Clear input/output demonstrations
- **🔍 Evaluation Criteria**: What to look for in candidate solutions

### Key Concepts Covered

**GenAI Problems:**
- Prompt engineering and optimization
- Error handling for API interactions
- JSON output formatting and validation
- Streaming vs. batch processing
- Multi-provider abstraction patterns

**Python Problems:**
- Algorithm design and optimization
- Time/space complexity analysis
- Edge case handling
- Clean code principles
- Test-driven development patterns

### Assessment Framework
- **Technical Skills**: Algorithm knowledge, code quality, debugging
- **Problem Solving**: Approach, planning, incremental development
- **Communication**: Code clarity, documentation, explanation ability
- **Time Management**: Working efficiently within constraints

## 🛠️ Development Standards

### Code Quality Requirements
Following the comprehensive standards:

✅ **Type Hints**: All function parameters and return values  
✅ **Docstrings**: Complete Args/Returns documentation  
✅ **Error Handling**: Robust exception management (especially GenAI)  
✅ **Testing**: Comprehensive main() demonstration with multiple test cases  
✅ **PEP 8**: Consistent Python style conventions  
✅ **Modular Design**: Single responsibility principle  
✅ **Time Scoping**: Realistic complexity for 30-45 minute completion  

### Templates & Patterns
The project provides standardized templates for:
- **Problem statements** with examiner guides
- **Solution implementations** with proper structure
- **LLM message formatting** for consistent interactions
- **Error handling patterns** for robust applications
- **Test case organization** for comprehensive validation

### Contributing Guidelines
When adding new problems:

1. **Classify**: Determine if it's a GenAI or Python problem
2. **Name**: Use 2 words maximum, snake_case format
3. **Structure**: Create exactly 2 files (question + solution)
4. **Time Scope**: Ensure 30-45 minute completion time
5. **Document**: Follow templates exactly
6. **Test**: Validate with real interview timing
7. **Update Table**: Add to Problems Catalog (never replace the table)

## 📚 Educational Value

### Learning Outcomes
- **Interview Readiness**: Practice with realistic technical challenges
- **Prompt Engineering**: Master effective LLM interaction patterns
- **Code Architecture**: Learn production-ready implementation patterns
- **API Integration**: Understand multi-provider abstraction techniques
- **Time Management**: Develop skills for working within constraints

### Use Cases
- **Technical Interview Preparation**: Both as candidate and interviewer
- **Prompt Engineering Training**: Learn effective LLM communication
- **Code Quality Reference**: Study well-documented implementations
- **AI Integration Learning**: Understand practical LLM application patterns
- **Algorithm Practice**: Reinforce fundamental computer science concepts

---

**🚀 Ready to start?** Pick a problem from the catalog above and challenge yourself to complete it within the time limit!

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Copyright (c) 2025 Snehal Bhasakhetre**

The MIT License is a permissive license that allows for:
- ✅ Commercial use
- ✅ Modification
- ✅ Distribution
- ✅ Private use

**Attribution Required**: Please include the original copyright notice and license text in any copies or substantial portions of the software.
