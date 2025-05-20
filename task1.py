<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Responsive Landing Page</title>
  <style>
    body, html {
      margin: 0;
      padding: 0;
      scroll-behavior: smooth;
      font-family: Arial, sans-serif;
    }

    /* Navigation styles */
    .navbar {
      position: fixed;
      top: 0;
      width: 100%;
      background-color: transparent;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 15px 30px;
      transition: background-color 0.3s, box-shadow 0.3s;
      z-index: 1000;
    }

    .navbar.scrolled {
      background-color: #333;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
    }

    .navbar a {
      color: white;
      text-decoration: none;
      margin-left: 20px;
      transition: color 0.3s, transform 0.3s;
    }

    .navbar a:hover {
      color: #ffd700;
      transform: scale(1.1);
    }

    .logo {
      font-size: 1.5em;
      font-weight: bold;
      color: white;
    }

    /* Sections */
    section {
      padding: 100px 30px;
      height: 100vh;
    }

    #home {
      background-color: #1abc9c;
    }

    #about {
      background-color: #3498db;
    }

    #contact {
      background-color: #9b59b6;
    }
  </style>
</head>
<body>

  <nav class="navbar" id="navbar">
    <div class="logo">MySite</div>
    <div>
      <a href="#home">Home</a>
      <a href="#about">About</a>
      <a href="#contact">Contact</a>
    </div>
  </nav>

  <section id="home"><h1>Welcome to My Landing Page</h1></section>
  <section id="about"><h1>About Us</h1></section>
  <section id="contact"><h1>Contact</h1></section>

  <script>
    const navbar = document.getElementById('navbar');
    window.addEventListener('scroll', () => {
      if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
      } else {
        navbar.classList.remove('scrolled');
      }
    });
  </script>
</body>
</html>
