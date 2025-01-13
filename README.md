## Setup (Windows)

#### 1. Install Python 3.10.11

```bash
winget install --id Python.Python.3.10
```
#### 2. Install FFMPEG with Chocolatey

```bash
choco install ffmpeg
```
#### 3. Install OpenAI Whisper

```bash
pip install openai-whisper
```
#### 4. Create a virtual environment

```bash
python -m venv whisper-env
```
## Usage

#### 1. Activate the virtual environment:

```bash
.\whisper-env\Scripts\activate
```
#### 2. Run python script
   
```bash
python transcribe.py
```
