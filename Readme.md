
# 🎨 CreatiVision: AI-Powered Marketing Asset Generator

CreatiVision is an AI-driven tool built for the **GenAI Exchange Hackathon** (Google Cloud), addressing **Big Basket's** marketing automation challenge. It enables effortless creation of **banners** (and soon videos) from product images using powerful generative AI models.

---

## 🌟 Key Features

* 🖼️ **Banner Generator** – Generate stunning promotional banners from uploaded images.
* 🎬 **Video Generator** *(Coming Soon)* – Auto-generate short video ads.
* 🧠 **AI-Powered** – Uses Google Gemini, Imagen, and Hugging Face models for content generation.
* 🎯 **Customizable** – Add promotional offers, themes, and color palettes.


---

## ⚙️ Local Setup & Run

### 🛠 Backend (Flask)

1. **Clone the repo**

   ```bash
   git clone https://github.com/your-repo/CreatiVision.git
   cd CreatiVision
   ```

2. **Create virtual environment & install dependencies**

   ```bash
   python3 -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Set environment variables (optional)**
   Create a `.env` file in the root directory if needed:

   ```
   GOOGLE_CLOUD_PROJECT_ID=your_project_id
   HUGGING_FACE_API_KEY=your_hf_key
   GOOGLE_APPLICATION_CREDENTIALS=your_json_file_path

   ```

4. **Run the Flask server**

   ```bash
   export FLASK_APP=app      # On Windows: set FLASK_APP=app
   flask run
   ```

   The backend will be available at `http://127.0.0.1:5000`.

---

### 🧩 Frontend (Vue.js)

1. **Navigate to the frontend directory**

   ```bash
   cd frontend
   ```

2. **Install dependencies**

   ```bash
   npm install
   ```

3. **Start the development server**

   ```bash
   npm run serve
   ```

   The frontend will run at `http://localhost:8080` and should connect to the Flask backend automatically.


---

## 🧪 Usage

1. Upload 1–2 product images (`.png` or `.jpg`)
2. Enter your promotional offer (e.g., “35% Off!”)
3. Choose a theme and color palette (e.g., “Valentine's Day”, “Red and Pink”)
4. Pick image generation model (`Google Imagen` or `Hugging Face`)
5. Hit “Generate Banner”
6. Review the banner, warnings, fallback info, and download result

---

## 💡 Tips for Optimal Results

* Use high-resolution product images
* Keep inputs minimal for better AI coherence
* Try varying themes and colors for multiple creatives

---

## 📦 API Notes

The `/generate_banner` API handles:

* Caption generation (fallback if APIs fail)
* Prompt crafting with Gemini
* Image synthesis using Google Imagen / Hugging Face
* File storage and final return

---

## 🖼️ Sample Banners

| Prompt                             | Output                                                                                      |
| ---------------------------------- | ------------------------------------------------------------------------------------------- |
| *"Interstellar theme for Pepsi"*   | ![Banner1](https://github.com/user-attachments/assets/a07cf5d6-961a-454b-939c-13ca3270d2f1) |
| *"Football world cup theme for Lays"* | ![Banner2](https://github.com/user-attachments/assets/737d0ccc-7529-4da6-b9d7-252635d98934) |

---

## 🔮 Future Roadmap

* [ ] Video ad generation from product clips
* [ ] Improved UI with real-time preview
* [ ] Template-based banner styles
* [ ] Better captioning using multimodal APIs

---

## 🔒 Security Notice

This hackathon build has **minimal security**. Planned security updates include:

* ✅ Authentication and rate limiting
* ✅ Input validation
* ✅ API key masking and usage quotas
* ✅ HTTPS + secure storage handling

---

## 🛠️ Responsible Use

We encourage ethical use:

* 📸 Use only copyright-free or owned images
* ✍️ Keep content brand-safe and appropriate
* 🧑‍🎨 Don’t misuse outputs for harmful automation

---

## 🌐 Hosting

CreatiVision is currently hosted on **Render**. Plans to move to scalable options (like Google Cloud Run or GKE) are in progress.

---

## 🏆 GenAI Exchange Hackathon

CreatiVision was built for the [GenAI Exchange Hackathon](https://genai.devpost.com), showcasing rapid prototyping and applied AI in digital marketing.

---

## 🤝 Feedback & Contributions

Open issues, fork, or raise pull requests:

* 📂 GitHub: [Monitor Repo](https://github.com/prateeks007/Monitor)
* 📬 Suggestions welcome via Issues tab

---

### CreatiVision – Empowering marketers with AI-driven creativity. 🚀

---


