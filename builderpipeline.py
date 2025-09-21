import os
import sys

def create_directory_structure(base_path):
    """Create NLP project directory structure"""
    
    # Define the structure as a dictionary
    structure = {
        'data': {
            'raw': {},
            'processed': {}
        },
        'experiments': {},
        'docs': {},
        'notebooks': {},
        'src': {
            '__init__.py': '',
            'config': {},
            'data': {},
            'features': {},
            'models': {},
            'eval': {},
            'utils': {},
            'api': {},
            'train.py': '',
            'inference.py': ''
        },
        'tests': {},
        'ci': {},
        'Dockerfile': 'FROM python:3.9-slim\n',
        'docker-compose.yml': 'version: "3.8"\n',
        'requirements.txt': '',
        'Makefile': '''train:
    python src/train.py

eval:
    python src/eval/evaluate.py
''',
        'README.md': '# NLP Project\n\nAdd project description here.'
    }

    def create_structure(current_path, structure):
        for name, content in structure.items():
            path = os.path.join(current_path, name)
            
            if isinstance(content, dict):
                os.makedirs(path, exist_ok=True)
                create_structure(path, content)
            else:
                with open(path, 'w') as f:
                    f.write(content)

    try:
        # Create the base directory
        os.makedirs(base_path, exist_ok=True)
        
        # Create the structure
        create_structure(base_path, structure)
        
        print(f"✅ Project structure created successfully at: {base_path}")
        
    except Exception as e:
        print(f"❌ Error creating project structure: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    project_name = input("Sentimentsocringpipeline")
    base_path = os.path.join(os.getcwd(), project_name)
    create_directory_structure(base_path)