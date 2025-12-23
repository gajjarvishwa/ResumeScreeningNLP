import io
from pdfminer.high_level import extract_text as pdf_extract_text
import docx
import spacy

nlp = None

def load_spacy():
    global nlp
    if nlp is None:
        try:
            nlp = spacy.load('en_core_web_sm')
        except Exception:
            raise RuntimeError('SpaCy model en_core_web_sm not found. Run: python -m spacy download en_core_web_sm')
    return nlp

def extract_text_from_file(f, filename):
    lower = filename.lower()
    if lower.endswith('.pdf'):
        return pdf_extract_text(io.BytesIO(f))
    elif lower.endswith('.docx'):
        doc = docx.Document(io.BytesIO(f))
        return '\n'.join(p.text for p in doc.paragraphs)
    else:
        try:
            return f.decode('utf-8', errors='ignore')
        except Exception:
            return ''

def extract_skills_from_text(text):
    nlp = load_spacy()
    doc = nlp(text)
    tokens = [
        token.lemma_.lower()
        for token in doc
        if token.pos_ in ('NOUN', 'PROPN', 'VERB', 'ADJ')
        and not token.is_stop and token.is_alpha
    ]
    freq = {}
    for t in tokens:
        freq[t] = freq.get(t, 0) + 1
    skills = sorted(freq.items(), key=lambda x: -x[1])[:40]
    return [s[0] for s in skills]
