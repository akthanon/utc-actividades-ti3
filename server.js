// server.js
const express = require("express");
const path = require("path");
const app = express();
const PORT = 80;

// Middleware para servir archivos estáticos desde /public
app.use(express.static(path.join(__dirname, "public")));

// Rutas directas opcionales (cada página HTML)
app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "index.html"));
});

app.get("/ej01", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "ejercicio_01_javascript_mysql.html"));
});

app.get("/ej02", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "ejercicio_02_tkinter_python.html"));
});

app.get("/ej03", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "ejercicio_03_html.html"));
});

app.get("/ej04", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "ejercicio_04_html_css_javascript.html"));
});

app.get("/ej05", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "ejercicio_05_pygame.html"));
});

app.get("/ej06", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "ejercicio_06_flask.html"));
});

app.get("/ej07", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "ejercicio_07_node_mysql.html"));
});

app.get("/ej08", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "ejercicio_08_django.html"));
});

app.get("/ej09", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "ejercicio_09_godot.html"));
});

app.get("/ej10", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "ejercicio_10_csharp.html"));
});

app.get("/ej11", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "ejercicio_11_unity.html"));
});


app.listen(PORT, () => {
  console.log(`Servidor corriendo en http://localhost:${PORT}`);
});
