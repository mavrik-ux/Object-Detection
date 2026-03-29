# 🎯 Object Detection with Voice Output

A real-time computer vision project that detects objects using YOLOv8 and announces their names using text-to-speech.

---

## 🚀 Features

* 🎥 Real-time object detection using webcam
* 🟩 Bounding boxes with labels and confidence
* 🔊 Voice output for detected objects
* 🚫 No repeated announcements (speaks each object only once)
* 🎛️ Controls to toggle voice and reset detection

---

## 🧠 Technologies Used

* Python 3.13
* OpenCV
* YOLOv8 (Ultralytics)
* pyttsx3 (offline text-to-speech)

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/object-detection-voice.git
cd object-detection-voice
```

Install dependencies:

```bash
pip install ultralytics opencv-python pyttsx3
```

---

## ▶️ Usage

Run the script:

```bash
python your_script_name.py
```

---

## 🎮 Controls

| Key     | Action               |
| ------- | -------------------- |
| **V**   | Toggle voice ON/OFF  |
| **R**   | Reset spoken objects |
| **ESC** | Exit application     |

---

## 🔊 How It Works

1. YOLOv8 detects objects in the webcam feed
2. Bounding boxes and labels are drawn on screen
3. Detected object names are converted to speech
4. Each object is spoken only once (until reset)

---

## 📸 Example Objects Detected

* Person
* Bottle
* Mobile Phone
* Laptop
* Chair
* Book

---

## ⚠️ Notes

* Ensure your webcam is accessible
* Voice output is offline (no internet required)
* Works best in good lighting conditions

---

## 💡 Future Improvements

* 🎤 Full sentence voice output
* 🎯 Object tracking
* 📱 Mobile app version
* 🧠 Smart prioritization of objects

---

## 🤝 Contributing

Feel free to fork this repository and improve it. Pull requests are welcome!

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👤 Author

Developed by **Anas**

---

⭐ If you like this project, give it a star on GitHub!
