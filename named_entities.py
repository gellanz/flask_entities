import spacy

class SpanishNER():
    def __init__(self) -> None:
        self.model = spacy.load("es_core_news_sm")

    def get_ner(self, sentence):
        info = self.model(sentence)
        result = {"oracion": sentence,
                  "entidades": {ent.text: ent.label_ for ent in info.ents}
                }
        return result


a = SpanishNER()
text = "Apple Inc. is a technology company headquartered in Cupertino, California."

b = a.get_ner(text)
print(b)