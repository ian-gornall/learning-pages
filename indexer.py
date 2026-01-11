import os
import pathlib

def generate_index(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Skip directories starting with a dot
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]
        # Skip existing index.html file to avoid recursive inclusion
        filenames = [f for f in filenames if f.lower() != 'index.html']

        # Start building the HTML content
        html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Index of {pathlib.Path(dirpath).name}</title>
</head>
<body>
    <h1>Index of {pathlib.Path(dirpath).name}</h1>
    <ul>
"""
        # Add link to parent directory (if not the root)
        if dirpath != root_dir:
            html_content += f'<li><a href="../index.html">.. (Parent directory)</a></li>\n'

        # Sort directories and files for organized listing
        dirnames.sort()
        filenames.sort()

        # Add links to subdirectories
        for dirname in dirnames:
            html_content += f'<li><a href="{dirname}/index.html">{dirname}/</a></li>\n'

        # Add links to files
        for filename in filenames:
            html_content += f'<li><a href="{filename}">{filename}</a></li>\n'
        
        html_content += """
    </ul>
</body>
</html>
"""
        # Write the content to index.html in the current directory
        index_path = pathlib.Path(dirpath) / 'index.html'
        index_path.write_text(html_content, encoding='utf-8')

        print(f"Generated: {index_path}")

# Run the script starting from the current directory
if __name__ == "__main__":
    generate_index('.')
