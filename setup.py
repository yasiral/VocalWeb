from setuptools import setup, find_packages

setup(
    name='VocalWeb',
    version='1.0.0',
    author='Yasir Altaf',
    author_email='',
    description='A Web-to-Audio converter that extracts, summarizes, and narrates web articles.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yasiral/VocalWeb',
    packages=find_packages(where="src"),
    package_dir={'': 'src'},  # Ensures src/ is the root package directory
    include_package_data=True,  # Includes non-Python files like .md, .txt, etc.
    install_requires=[
        "gradio",
        "transformers",
        "kokoro==0.7.11",
		"torch",
		"langdetect",
		"numpy",
		"spacy",
        "nltk",
		"pillow",
		"stanza",
        "trafilatura",
        "markitdown",
        "soundfile",
        "matplotlib",
        "wordcloud",
        "pytest",  # For testing
        "gliner",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Multimedia :: Sound/Audio :: Speech",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    python_requires='>=3.8',
    entry_points={
        "console_scripts": [
            "VocalWeb=main:main",  # CLI entry point
        ]
    },
    keywords="audio web scraper tts gradio summarization",
    project_urls={
        "Bug Tracker": "https://github.com/yasiral/VocalWeb/issues",
        "Documentation": "https://github.com/yasiral/VocalWeb/wiki",
        "Source Code": "https://github.com/yasiral/VocalWeb",
    }
)
