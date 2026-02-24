const express = require("express");
const app = express();

app.get("/login", function (req, res) {
  // ❌ Hardcoded secret
  const apiKey = "12345-secret-key";

  // ❌ XSS vulnerability
  res.send("<h1>" + req.query.user + "</h1>");
});

app.listen(3000);