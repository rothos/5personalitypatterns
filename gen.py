import pandas as pd

def csv_to_html_table(csv_file, html_file):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)
    df.rename(columns={'Unnamed: 0': ''}, inplace=True)
    
    # Convert the DataFrame to an HTML table with custom styling
    html_table = df.to_html(index=False, border=0, classes='table', escape=False)
    html_table = html_table.replace("Compensated merging:", "<br/><i>Compensated merging:</i>")

    # Create the full HTML content with custom styling
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <!-- Google tag (gtag.js) -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=G-VSL74PME4G"></script>
        <script>
          window.dataLayer = window.dataLayer || [];
          function gtag(){{dataLayer.push(arguments);}}
          gtag('js', new Date());

          gtag('config', 'G-VSL74PME4G');
        </script>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>5 Personality Patterns</title>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Lato:wght@400;700&display=swap" rel="stylesheet">
        <style>
            body {{
                font-family: 'Lato', sans-serif;
                font-size: .88em;
                background-color: #f8f9fa;
                margin: 40px;
            }}
            h1 {{
                text-align: center;
                margin-bottom: 20px;
            }}
            .container {{
                max-width: 900px;
                margin: auto;
            }}
            table {{
                width: 900px;
                border-collapse: collapse;
                margin: auto;
                text-align: left;
                position: relative;
                border: 1px solid #ccc;
            }}
            th {{
                background-color: #f2f2f2;
                font-weight: bold;
                text-align: left;
                position: sticky;
                top: 0;
                z-index: 1;
                border: 1px solid #ccc;
                border-left: 0;
                border-right: 0;
            }}
            td, th {{
                padding: 8px 12px;
                border: 1px solid #ccc;
            }}
            th:after,
            th:before {{
              content: '';
              position: absolute;
              left: 0;
              width: 100%;
            }}

            th:before {{
              top: -1px;
              border-top: 1px solid #ccc;
            }}

            th:after {{
              bottom: -1px;
              border-bottom: 1px solid #ccc;
            }}
            tbody tr:nth-child(even) {{
                background-color: #f9f9f9;
            }}
            tbody tr:nth-child(odd) {{
                background-color: #fff;
            }}
            tbody td:first-child {{
                font-weight: bold;
            }}
            tbody tr:first-child th {{
                font-weight: bold;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>5 Personality Patterns</h1>
            {html_table}
        </div>
    </body>
    </html>
    """
    
    # Write the HTML content to the specified file
    with open(html_file, 'w') as file:
        file.write(html_content)
    
    print(f"HTML file '{html_file}' has been generated successfully.")

# Example usage
csv_to_html_table('chart.csv', 'index.html')
