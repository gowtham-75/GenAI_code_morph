import re
mermaid_js = "https://cdn.jsdelivr.net/npm/mermaid@latest/dist/mermaid.min.js"

def generateDiagram(mermaid_diagram_code):

    downloadMermaidDiagram = """
            <div style="text-align: center;">
            <button onclick="downloadMermaidDiagram()">Download Diagram</button>
            <script>
            function downloadMermaidDiagram() {
                const diagramElement = document.getElementById('mermaid-diagram');

                mermaid.initialize({ startOnLoad: false });  
                mermaid.init(diagramElement); 

                const svgData = diagramElement.querySelector('svg').outerHTML;
                const blob = new Blob([svgData], { type: 'image/svg+xml;charset=utf-8' });
                const link = document.createElement('a');
                link.href = URL.createObjectURL(blob);
                link.download = 'mermaid_diagram.svg';
                link.click();
            }
            </script>"""

    html_string = f"""
            <script src="{mermaid_js}"></script>
            <div class="mermaid" id="mermaid-diagram" style="text-align:center;">
            {mermaid_diagram_code}
            </div>
            <br>
            <br>
            """+downloadMermaidDiagram
    return html_string