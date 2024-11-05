def _create_side_panel(options):
    div = f"""<div id="sidebar">
        <h3>Select Content</h3>"""
    choosable = ""
    for option in options:
        print(option)
        choosable += f"""\n<button onclick="loadContent('{option}.html')">{option}</button>"""
    div += choosable + "\n</div>"
    return div

def create_index_page(filename , options):
    content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Interface</title>
        <style>
            body {{
                display: flex;
                margin: 0;
                font-family: Arial, sans-serif;
            }}
            #sidebar {{
                width: 200px;
                background-color: #f3f3f3;
                padding: 20px;
                border-left: 2px solid #ddd;
                display: flex;
                flex-direction: column;
                align-items: center;
            }}
            #content {{
                flex: 1;
                display: flex;
                justify-content: center;
                align-items: center;
            }}
            iframe {{
                width: 100%;
                height: 100vh;
                border: none;
            }}
            button {{
                margin-top: 10px;
                padding: 10px 20px;
                cursor: pointer;
                width: 100%;
            }}
        </style>
    </head>
    <body>
        {_create_side_panel(options)}
        <div id="content">
            <iframe id="viewer" src=""></iframe>
        </div>
        <script>
            function loadContent(filename) {{
                document.getElementById('viewer').src = filename;
            }}
        </script>
    </body>
    </html>
    """
    with open(filename + ".html", "w") as file:
        file.write(content)
