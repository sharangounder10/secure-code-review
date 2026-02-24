const express = require("express");
const app = express();

// 1. Hardcoded API key (Security Hotspot)
const API_KEY = "sk_test_123456";

// 2. SQL Injection (Vulnerability)
app.get("/user", (req, res) => {
  const userId = req.query.id;
  const query = "SELECT * FROM users WHERE id = " + userId;
  res.send(query);
});

// 3. Cross-Site Scripting (Vulnerability)
app.get("/search", (req, res) => {
  res.send("<h1>" + req.query.q + "</h1>");
});

// 4. Weak random generator (Security Hotspot)
function generateToken() {
  return Math.random().toString(36);
}

// 5. Console log in production (Code Smell)
console.log("Server started");

app.listen(3000);