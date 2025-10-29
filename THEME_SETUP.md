# Setting Up Streamlit Dark Theme

## 📁 Create .streamlit Directory

In your project root (where app.py is located), create a `.streamlit` folder:

### On Mac/Linux:
```bash
mkdir .streamlit
```

### On Windows (Command Prompt):
```cmd
mkdir .streamlit
```

### On Windows (PowerShell):
```powershell
New-Item -ItemType Directory -Path .streamlit
```

---

## 📝 Create config.toml File

Inside the `.streamlit` folder, create a file named `config.toml`:

### On Mac/Linux:
```bash
touch .streamlit/config.toml
```

### On Windows:
Create the file manually or use:
```cmd
type nul > .streamlit\config.toml
```

---

## ⚙️ Add Theme Configuration

Open `.streamlit/config.toml` in a text editor and add:

```toml
[theme]
primaryColor = "#2196f3"
backgroundColor = "#000000"
secondaryBackgroundColor = "#1a1a1a"
textColor = "#ffffff"
font = "sans serif"

[client]
showSidebarNavigation = false
```

### Theme Settings Explained:

- **primaryColor**: Blue color for buttons and interactive elements
- **backgroundColor**: Main background color (black)
- **secondaryBackgroundColor**: Sidebar and secondary elements (dark gray)
- **textColor**: Text color (white)
- **font**: Font family for the app

---

## 🚀 Restart the Application

After creating the config file:

1. **Stop** the Streamlit server (Ctrl + C in terminal)
2. **Restart** with: `streamlit run app.py`
3. The dark theme will now be **locked** regardless of system settings!

---

## ✅ Verification

After restart, you should see:
- Black background everywhere
- Dark gray sidebar
- White text
- Blue buttons
- Theme stays consistent in light/dark system mode

---

## 🎨 Customization Options

You can customize the theme by changing values in config.toml:

### Example - Different Color Schemes:

**Purple Theme:**
```toml
[theme]
primaryColor = "#9c27b0"
backgroundColor = "#000000"
secondaryBackgroundColor = "#1a1a1a"
textColor = "#ffffff"
```

**Green Theme:**
```toml
[theme]
primaryColor = "#4caf50"
backgroundColor = "#000000"
secondaryBackgroundColor = "#1a1a1a"
textColor = "#ffffff"
```

**Red Theme:**
```toml
[theme]
primaryColor = "#f44336"
backgroundColor = "#000000"
secondaryBackgroundColor = "#1a1a1a"
textColor = "#ffffff"
```

---

## 📚 Additional Resources

- [Streamlit Theme Documentation](https://docs.streamlit.io/library/advanced-features/theming)
- [Streamlit Configuration](https://docs.streamlit.io/library/advanced-features/configuration)

---

## 🐛 Troubleshooting

**Problem:** Theme not applying
**Solution:** Make sure `.streamlit/config.toml` is in the project root directory (same level as app.py)

**Problem:** Still seeing white background
**Solution:** 
1. Completely stop the Streamlit server (Ctrl + C)
2. Clear browser cache
3. Restart Streamlit
4. Hard refresh browser (Ctrl + Shift + R)

**Problem:** Config file not found
**Solution:** Verify the file path is correct:
```
your-project/
├── .streamlit/
│   └── config.toml
├── app.py
├── chatbot.py
└── .env
```