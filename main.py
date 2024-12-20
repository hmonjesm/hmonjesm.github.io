html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home - My Info Table</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        header {
            background-color: white;
            color: black;
            padding: 10px 0;
            text-align: center;
            width: 100%;
            border-bottom: 1px solid #ccc;
        }
        nav {
            display: flex;
            justify-content: center;
            background-color: white;
            border-bottom: 1px solid #ccc;
            width: 100%;
            padding: 10px 0;
        }
        nav a {
            color: black;
            text-decoration: none;
            padding: 10px 20px;
        }
        nav a:hover {
            background-color: #f0f0f0;
        }
        h2 {
            margin-top: 20px;
        }
        table {
            width: 50%;
            border-collapse: collapse;
            margin: 20px 0;
        }
        table, th, td {
            border: 1px solid black;
        }
        th, td {
            padding: 10px;
            text-align: center;
        }
    </style>
</head>
<body>

<nav>
    <a href="index.html">Home</a>
    <a href="ethics.html">Ethics</a>
</nav>

<h2>My Introduction Table</h2>

<table>
    <tr>
        <td><strong>Name</strong></td>
        <td>Hugo Monjes</td>
    </tr>
    <tr>
        <td><strong>Introduction</strong></td>
        <td>Hello, I am a junior in the BS IT program. I enjoy learning more about Python.</td>
    </tr>
    <tr>
        <td><strong>Hobbies</strong></td>
        <td>Some of my hobbies are cooking, playing sports, and programming.</td>
    </tr>
</table>

</body>
</html>"""