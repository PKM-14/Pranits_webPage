f = open('Pranit_malhotra.html', 'w')

html_template = """<html>

<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>This is Pranit Malhotra</title>
<style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: Arial, sans-serif;
        }
        .navbar {
            background-color: #000000;
            overflow: hidden;
            position: fixed;
            top: 0;
            width: 100%;
            display: flex;
            justify-content: space-between;
            padding: 10px 20px;
        }
        .navbar a {
            color: white;
            text-decoration: none;
            padding: 14px 20px;
            display: block;
        }
        .navbar a:hover {
            background-color: #575757;
        }
        .nav-links {
            display: flex;
        }
        @media screen and (max-width: 600px) {
            .nav-links {
                flex-direction: column;
                width: 100%;
                display: none;
            }
            .nav-links.active {
                display: flex;
            }
        }
    </style>
    <style>
    html, body {
      height: 100%;
      margin: 0;
   
    .footer {
      height: 550px;
      background-color: #111111;
      line-height: 30px;


  </style>
</head>



<body style="background-image: url('C:/Users/kulde/OneDrive/Python and HTML codeing/Add Ons for coding ie photos ext/photo-1557682260-96773eb01377.jpg'); width:1480; background-attachment: fixed; background-size: cover;">


    <div class="navbar">
    <img src="C:/Users/kulde/OneDrive/Python and HTML codeing/Add Ons for coding ie photos ext/Screenshot 2025-03-02 101253.png" style="width:60px;height:70px;">
    <h1 style="color:white ;text-align:center;"Centered Heading; "font-family:century schoolbook;">This is Pranit Malhotra</h1>
        <div class="nav-links">
            <a href="#about">About</a>
            <a href="#services">Certificates</a>
            <a href="#contact">Contact</a>
        </div>
    </div>
    <div style="margin-top:50px; padding:20px;">



</div>






    
<h1 style="text-align:center;"Centered Heading; "font-family:century schoolbook;">This is Pranit Malhotra</h1>
<h2 style="text-align:center;"Centered Heading;>This page is about me, going into my profesional and personal life.</h2>
<div id="about" style="padding:100px;">

    <h1><em>About me (Profesional)</em></h1>
    <p> Hi there, I am Pranit Malhotra from Saint Olaves Grammar School in Orpington and I am passionate about Physics, Maths, and Chemistry more so in the field of Aerodynamics
and Aerospace Engineering. My strength includes my academic success including entering the olympiad of the junior and intermediate math challenges (UKMT) and top 100 Gold in the BPho
(Physics Challenge). My key characteristics are my Leadership, kindness, and determination. My endeavors through Aerodynamics and Aerospace Engineering led me to participate in the F1
in Schools competition (Now known as STEM Racing) in the team known as Blitz. This experience made me realise my talents and where they lie for example I have discovered a new and
unkindled passion for manufacturing the car, applying great precision. I have also learned, experienced, and broken through the difficulties of teamwork while also using it as a strength
, driving us to strive for success. Furthermore, I have had many experiences in sports such as being the captain for the U13,14 and 15 rugby B teams and soon after moving to the U15 A
team and through this I have learned how to use individual strength in a team and build on it which lead us to thrive in matches. Taking on a leadership role has also made me come to the
difficulties of keeping people together but I soon learned to overcome this by truly understanding my teammates and connecting to them on an emotional level. 
    </p>

<h1><em>About me (Personal)</em></h1>

<img src="C:/Users/kulde/OneDrive/Python and HTML codeing/Add Ons for coding ie photos ext/Screenshot 2025-03-01 114447.png" style="width:500px;height:300px;">


    </div>



</div>


















<div id="services" style="padding:100px;">
    <h1>Certificates</h1>
    <p>This is where im going to keep track of all my major acheivements throughout the years</p>
    <p> Nationals 3rd place boissssssssss!!!!</p>
    <img src="C:/Users/kulde/OneDrive/Pictures/Nats 3rd place photo.jpg" style="width:800px;height:500px;">    
    <img src="C:/Users/kulde/OneDrive/Python and HTML codeing/Add Ons for coding ie photos ext/77706285_1737741803200348_r.webp" style="width:800px;height:500px;">
    <img src="C:/Users/kulde/OneDrive/Python and HTML codeing/Add Ons for coding ie photos ext/Screenshot 2025-03-03 202557.png" style="width:800px;height:500px;">
    <img src="C:/Users/kulde/OneDrive/Pictures/jmc.png" style="width:800px;height:300px;">
   
    




</div>
<p> </p>

</div>
  <div class="footer">
    <div id="contact" style="padding:100px;">
    <h1 style= "color:white;text-align:center;">Contact Me</h1>
   
    <p><h2 style="color:white;">These are links to me:</h2>
<a href="https://www.linkedin.com/in/pranit-malhotra-2504ba338/">Visit My LinkedIn</a>
<p style="color:white;">____________________</p>
<a href="https://www.instagram.com/14pranitmalhotra/">Visit My Instagram</a>
<p style="color:white;">____________________</p>
<a href="https://www.instagram.com/team_blitz8/">Visit Team Blitz Instagram</a>
<p style="color:white;">____________________</p>
<a href="https://www.gofundme.com/f/team-blitz8/donations">Visit Team Blitz GoFundMe</a></p>

 <img src="C:/Users/kulde/OneDrive/Python and HTML codeing/Add Ons for coding ie photos ext/Screenshot 2025-03-03 191631.png" >
</div>
  </div>

</body>



</html>

"""
f.write(html_template)

f.close()



